import sys, time, traceback
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem
from PySide6.QtCore import QFile, QIODevice, QObject, Slot, Signal, QRunnable, QThreadPool
from networkScanner.networkScanner import scanner
from manInTheMiddle.script import stopSpoof, spoofer


# Global variables
targets = []
scanning = False
attacking = True

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
    global attacking
    attacking = True
    if (name == "ARP spoofing") :
        victim1IP,victim1Mac = targets[0].split(" : ")
        victim2IP,victim2Mac = targets[1].split(" : ")
        packets = 0
        while (attacking) :
            spoofer(victim1IP,victim2IP,victim1Mac)
            spoofer(victim2IP,victim1IP,victim1Mac)
            printed = "[+] Sent packets "+ str(packets)
            print(printed)
            window.console.append(printed)
            sys.stdout.flush()
            packets +=2
            time.sleep(2)
        print("End attacking")

def stopAttacking(name) :
    if (name == "ARP spoofing") :
        victim1IP,victim1Mac = targets[0].split(" : ")
        victim2IP,victim2Mac = targets[1].split(" : ")
        stopSpoof(victim1IP,victim2IP,victim1Mac, victim2Mac)


def scanning_complete():
    print("scanning COMPLETE!")

def scanning_output(output):
    listHosts = output
    window.listWidget.clear()
    print("Scanned list = ",listHosts)
    for host in listHosts:
        listWidgetItem = QListWidgetItem(host["ip"]+' : '+host["mac"])
        window.listWidget.addItem(listWidgetItem)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "form.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.console.setText("")
    window.setWindowTitle("Cyber Range App")
    attackName = "None"

    @Slot()
    def scan(scanning):
        if(scanning==False) :
            window.console.append("Scanner begin")
            print("Scanner begin") 
            scanning = True
            #listHosts = scanner()

            scanThread = Worker(scanner)
            scanThread.signals.result.connect(scanning_output)
            scanThread.signals.finished.connect(scanning_complete)

            window.threadpool.start(scanThread)
            

            
        else :
            window.console.append("Already scanning !")
    @Slot()
    def addTargetClicked() :
        try :
            newtar = window.listWidget.selectedItems()[0].text()
            if (len(targets) < 2) :
                if (newtar not in targets):
                    targets.append(newtar)
                    if (len(targets) == 1):
                        window.target1.setText("Target 1\n" + newtar.split(" : ")[0] + "\n" + newtar.split(" : ")[1])
                    elif (len(targets) == 2) :
                        window.target2.setText("Target 2\n" + newtar.split(" : ")[0] + "\n" + newtar.split(" : ")[1])
                else :
                    window.console.append("Targets already added !")
            else : 
                window.console.append("Number of targets exceeded !")
            

            print ("targets = ",targets)
            output = newtar + " added to your targets list"
            print (output)
            window.console.append(output)
        except IndexError:
            window.console.append("You didn't select a target")
    @Slot()
    def deleteTargetClicked() :
        if (len(targets)>0) :
            targets.clear()
            window.console.append("Targets cleared")
            window.target1.setText("Select Target 1")
            window.target2.setText("Select Target 2")
        else :
            window.console.append("List already cleared")
    @Slot()
    def startAttackClicked() :
        global attackName
        if (attackName == "None") : 
            if (len(targets) == 2) :
                attackName = window.attacks.currentText()
                window.console.append(attackName + " attack started")
                #attacking(attackName)
                startAttackThread = Worker(attacking, attackName)
                startAttackThread.signals.result.connect(attacking_output)
                startAttackThread.signals.finished.connect(attacking_complete)

                window.threadpool.start(startAttackThread)
            else :
                mess = "You have to select two targets first"
                print(mess)
                window.console.append(mess)

        else :
            mess = "You should stop the running attack first"
            print(mess)
            window.console.append(mess)

    @Slot()
    def stopAttackClicked() :
        global attackName
        if (attackName != "None") : 
            window.console.append(attackName + " attack stopped")
            #stopAttacking(attackName)
            
            global attacking
            attacking = False

            stopAttackThread = Worker(stopAttacking, attackName)
            stopAttackThread.signals.result.connect(stoppingAttack_output)
            stopAttackThread.signals.finished.connect(stoppingAttack_complete)

            window.threadpool.start(stopAttackThread)            

            attackName = "None"

        else :
            window.console.append("You should start the attack first")


    window.scan.clicked.connect(scan)
    window.addTarget.clicked.connect(addTargetClicked)
    window.deleteTarget.clicked.connect(deleteTargetClicked)
    window.startAttack.clicked.connect(startAttackClicked)
    window.stopAttack.clicked.connect(stopAttackClicked)
    

    window.threadpool = QThreadPool()

    window.show()

    sys.exit(app.exec_())