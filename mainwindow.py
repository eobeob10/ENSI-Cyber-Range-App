from os import remove
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem
from PySide6.QtCore import QFile, QIODevice, Slot
from NetworkScanner.networkScanner import scanner
targets = set()
scanning = False
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "form.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.console.setText("")

    @Slot()
    def scan(scanning):
        if(scanning==False) :
            print("Scanner begin")
            scanning = True
            listHosts = scanner()
            window.listWidget.clear()
            print(listHosts)
            for host in listHosts:
                listWidgetItem = QListWidgetItem(host["ip"]+' : '+host["mac"])
                window.listWidget.addItem(listWidgetItem)
            scanning = False
        else :
            window.console.append("Already scanning !")
    @Slot()
    def addTargetClicked() :
        try :
            targets.add(window.listWidget.selectedItems()[0].text())
            output = window.listWidget.selectedItems()[0].text() + " added to your targets list"
            print (output)
            window.console.append(output)
        except IndexError:
            window.console.append("You didn't select a target")
    @Slot()
    def deleteTargetClicked() :
        try :
            targ = window.listWidget.selectedItems()[0].text()
            if (targ in targets) :
                targets.remove(targ)
            else :
                window.console.append("This target doesn't exist in the list of selected targets")
        except IndexError :
            window.console.append("You didn't select a target")



    window.scan.clicked.connect(scan)
    window.addTarget.clicked.connect(addTargetClicked)
    window.deleteTarget.clicked.connect(deleteTargetClicked)
    

    

    window.show()

    sys.exit(app.exec_())
