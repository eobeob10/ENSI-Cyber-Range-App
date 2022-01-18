import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from NetworkScanner.networkScanner import scanner

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "form.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()


    window.show()

    sys.exit(app.exec_())
