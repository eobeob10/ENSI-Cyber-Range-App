# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1093, 662)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scan = QPushButton(self.centralwidget)
        self.scan.setObjectName(u"scan")
        self.scan.setGeometry(QRect(30, 70, 151, 51))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 250, 151, 141))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 10, 131, 26))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 40, 131, 26))
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 70, 131, 26))
        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 100, 131, 26))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 400, 151, 51))
        self.console = QTextBrowser(self.centralwidget)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(30, 470, 631, 81))
        self.copyrights = QTextBrowser(self.centralwidget)
        self.copyrights.setObjectName(u"copyrights")
        self.copyrights.setGeometry(QRect(230, 560, 671, 61))
        self.copyrights.setAutoFillBackground(False)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(200, 70, 191, 381))
        self.deleteTarget = QPushButton(self.centralwidget)
        self.deleteTarget.setObjectName(u"deleteTarget")
        self.deleteTarget.setGeometry(QRect(30, 190, 151, 51))
        self.addTarget = QPushButton(self.centralwidget)
        self.addTarget.setObjectName(u"addTarget")
        self.addTarget.setGeometry(QRect(30, 140, 151, 41))
        self.startAttack = QPushButton(self.centralwidget)
        self.startAttack.setObjectName(u"startAttack")
        self.startAttack.setGeometry(QRect(680, 510, 181, 41))
        self.stopAttack = QPushButton(self.centralwidget)
        self.stopAttack.setObjectName(u"stopAttack")
        self.stopAttack.setGeometry(QRect(870, 510, 191, 41))
        self.appName = QTextBrowser(self.centralwidget)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(290, 10, 511, 51))
        self.attacks = QComboBox(self.centralwidget)
        self.attacks.addItem("")
        self.attacks.addItem("")
        self.attacks.addItem("")
        self.attacks.setObjectName(u"attacks")
        self.attacks.setGeometry(QRect(680, 470, 381, 31))
        self.target1 = QTextBrowser(self.centralwidget)
        self.target1.setObjectName(u"target1")
        self.target1.setGeometry(QRect(420, 70, 311, 81))
        self.target2 = QTextBrowser(self.centralwidget)
        self.target2.setObjectName(u"target2")
        self.target2.setGeometry(QRect(750, 70, 311, 81))
        self.boxattacks = QGroupBox(self.centralwidget)
        self.boxattacks.setObjectName(u"boxattacks")
        self.boxattacks.setGeometry(QRect(420, 160, 631, 281))
        self.interfaceAttack = QTextBrowser(self.boxattacks)
        self.interfaceAttack.setObjectName(u"interfaceAttack")
        self.interfaceAttack.setGeometry(QRect(60, 10, 491, 111))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1093, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.groupBox.setTitle("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Wireshark", None))
        self.console.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Console</span></p></body></html>", None))
        self.copyrights.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Copyright \u00a9 2022, Ecole Nationale Des Sciences de l'informatique</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Boubakri Ibrahim - Hmissa Adem</span></p></body></html>", None))
        self.deleteTarget.setText(QCoreApplication.translate("MainWindow", u"Delete Target", None))
        self.addTarget.setText(QCoreApplication.translate("MainWindow", u"Add Target", None))
        self.startAttack.setText(QCoreApplication.translate("MainWindow", u"Start Attack", None))
        self.stopAttack.setText(QCoreApplication.translate("MainWindow", u"Stop Attack", None))
        self.appName.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt;\">Cyber Range App</span></p></body></html>", None))
        self.attacks.setItemText(0, QCoreApplication.translate("MainWindow", u"ARP spoofing", None))
        self.attacks.setItemText(1, QCoreApplication.translate("MainWindow", u"DHCP starving", None))
        self.attacks.setItemText(2, QCoreApplication.translate("MainWindow", u"SYN flooding", None))

        self.target1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt;\">Select Target 1</span></p></body></html>", None))
        self.target2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:18pt;\">Select Target 2</span></p></body></html>", None))
        self.boxattacks.setTitle("")
        self.interfaceAttack.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:22pt;\">Interface des attaques</span></p></body></html>", None))
    # retranslateUi

