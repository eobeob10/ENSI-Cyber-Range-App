from os import remove
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem
from PySide6.QtCore import QFile, QIODevice, Slot
from networkScanner.networkScanner import scanner
from manInTheMiddle.script import startSpoof, stopSpoof


# Global variables
targets = []
scanning = False


# Functions to start and stop attacking 
def attacking(name) :
    if (name == "ARP spoofing") :
        victim1IP,victim1Mac = targets[0].split(" : ")
        victim2IP,victim2Mac = targets[1].split(" : ")
        startSpoof(victim1IP,victim2IP,victim1Mac)

def stopAttacking(name) :
    if (name == "ARP spoofing") :
        victim1IP,victim1Mac = targets[0].split(" : ")
        victim2IP,victim2Mac = targets[1].split(" : ")
        stopSpoof(victim1IP,victim2IP,victim1Mac, victim2Mac)
        
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
            listHosts = scanner()
            window.listWidget.clear()
            print("Scanned list = ",listHosts)
            for host in listHosts:
                listWidgetItem = QListWidgetItem(host["ip"]+' : '+host["mac"])
                window.listWidget.addItem(listWidgetItem)
            scanning = False
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
            attackName = window.attacks.currentText()
            window.console.append(attackName + " attack started")
            attacking(attackName)
        else :
            window.console.append("You should stop the running attack first")

    @Slot()
    def stopAttackClicked() :
        global attackName
        if (attackName != "None") : 
            window.console.append(attackName + " attack stopped")
            stopAttacking(attackName)
            attackName = "None"
        else :
            window.console.append("You should start the attack first")


    window.scan.clicked.connect(scan)
    window.addTarget.clicked.connect(addTargetClicked)
    window.deleteTarget.clicked.connect(deleteTargetClicked)
    window.startAttack.clicked.connect(startAttackClicked)
    window.stopAttack.clicked.connect(stopAttackClicked)
    

    

    window.show()

    sys.exit(app.exec_())
