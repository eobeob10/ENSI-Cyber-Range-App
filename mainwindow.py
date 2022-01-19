import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QListWidgetItem
from PySide6.QtCore import QFile, QIODevice, Slot
from NetworkScanner.networkScanner import scanner

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "form.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    targets = set()

    @Slot()
    def scan():
        print("Scanner begin")
        listHosts = scanner()
        window.listWidget.clear()
        print(listHosts)
        for host in listHosts:
            listWidgetItem = QListWidgetItem(host["ip"]+' : '+host["mac"])
            window.listWidget.addItem(listWidgetItem)
    
    @Slot()
    def addTargetClicked() :
        targets.add(window.listWidget.selectedItems()[0].text())
        print(window.listWidget.selectedItems()[0].text() + " added to your targets list")
    


    window.scan.clicked.connect(scan)
    window.addTarget.clicked.connect(addTargetClicked)
    
    

    

    window.show()

    sys.exit(app.exec_())
