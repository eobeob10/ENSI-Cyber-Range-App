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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scan = QPushButton(self.centralwidget)
        self.scan.setObjectName(u"scan")
        self.scan.setGeometry(QRect(30, 170, 151, 51))
        self.wireshark = QPushButton(self.centralwidget)
        self.wireshark.setObjectName(u"wireshark")
        self.wireshark.setGeometry(QRect(30, 450, 151, 51))
        self.console = QTextBrowser(self.centralwidget)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(30, 540, 631, 81))
        self.copyrights = QTextBrowser(self.centralwidget)
        self.copyrights.setObjectName(u"copyrights")
        self.copyrights.setGeometry(QRect(230, 630, 671, 61))
        self.copyrights.setAutoFillBackground(False)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(190, 140, 221, 381))
        self.deleteTarget = QPushButton(self.centralwidget)
        self.deleteTarget.setObjectName(u"deleteTarget")
        self.deleteTarget.setGeometry(QRect(30, 310, 151, 51))
        self.addTarget = QPushButton(self.centralwidget)
        self.addTarget.setObjectName(u"addTarget")
        self.addTarget.setGeometry(QRect(30, 380, 151, 51))
        self.startAttack = QPushButton(self.centralwidget)
        self.startAttack.setObjectName(u"startAttack")
        self.startAttack.setGeometry(QRect(680, 540, 181, 81))
        self.stopAttack = QPushButton(self.centralwidget)
        self.stopAttack.setObjectName(u"stopAttack")
        self.stopAttack.setGeometry(QRect(870, 540, 191, 81))
        self.appName = QTextBrowser(self.centralwidget)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(260, 30, 561, 81))
        self.attacks = QComboBox(self.centralwidget)
        self.attacks.addItem("")
        self.attacks.addItem("")
        self.attacks.addItem("")
        self.attacks.setObjectName(u"attacks")
        self.attacks.setGeometry(QRect(420, 240, 641, 41))
        self.target1 = QTextBrowser(self.centralwidget)
        self.target1.setObjectName(u"target1")
        self.target1.setGeometry(QRect(420, 140, 311, 81))
        self.target2 = QTextBrowser(self.centralwidget)
        self.target2.setObjectName(u"target2")
        self.target2.setGeometry(QRect(750, 140, 311, 81))
        self.logoensi = QLabel(self.centralwidget)
        self.logoensi.setObjectName(u"logoensi")
        self.logoensi.setGeometry(QRect(80, 10, 111, 121))
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, -1, 1101, 731))
        self.cyberrange = QLabel(self.centralwidget)
        self.cyberrange.setObjectName(u"cyberrange")
        self.cyberrange.setGeometry(QRect(900, 10, 111, 111))
        self.clearList = QPushButton(self.centralwidget)
        self.clearList.setObjectName(u"clearList")
        self.clearList.setGeometry(QRect(30, 240, 151, 51))
        self.description = QTextBrowser(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(420, 290, 641, 231))
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.scan.raise_()
        self.wireshark.raise_()
        self.console.raise_()
        self.copyrights.raise_()
        self.listWidget.raise_()
        self.deleteTarget.raise_()
        self.addTarget.raise_()
        self.startAttack.raise_()
        self.stopAttack.raise_()
        self.appName.raise_()
        self.attacks.raise_()
        self.target1.raise_()
        self.target2.raise_()
        self.logoensi.raise_()
        self.cyberrange.raise_()
        self.clearList.raise_()
        self.description.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1096, 25))
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
        self.wireshark.setText(QCoreApplication.translate("MainWindow", u"Wireshark", None))
        self.console.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Console</p></body></html>", None))
        self.copyrights.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright \u00a9 2022, Ecole Nationale Des Sciences de l'informatique</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Boubakri Ibrahim - Hmissa Adem</p></body></html>", None))
        self.deleteTarget.setText(QCoreApplication.translate("MainWindow", u"Delete Target", None))
        self.addTarget.setText(QCoreApplication.translate("MainWindow", u"Add Target", None))
        self.startAttack.setText(QCoreApplication.translate("MainWindow", u"Start Attack", None))
        self.stopAttack.setText(QCoreApplication.translate("MainWindow", u"Stop Attack", None))
        self.appName.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Cyber Range App</span></p></body></html>", None))
        self.attacks.setItemText(0, QCoreApplication.translate("MainWindow", u"ARP spoofing", None))
        self.attacks.setItemText(1, QCoreApplication.translate("MainWindow", u"DHCP starving", None))
        self.attacks.setItemText(2, QCoreApplication.translate("MainWindow", u"SYN flooding", None))

        self.target1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Select Target 1</span></p></body></html>", None))
        self.target2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Select Target 2</span></p></body></html>", None))
        self.logoensi.setText("")
        self.background.setText("")
        self.cyberrange.setText("")
        self.clearList.setText(QCoreApplication.translate("MainWindow", u"Clear list", None))
        self.description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">L'ARP spoofing, \u00e9galement appel\u00e9 ARP poisoning, est une attaque de type &quot;Man in the Middle&quot; (MitM) qui permet aux attaquants d'intercepter les communications entre les p\u00e9riph\u00e9riques r\u00e9seau.</span></p></body></html>", None))
    # retranslateUi

