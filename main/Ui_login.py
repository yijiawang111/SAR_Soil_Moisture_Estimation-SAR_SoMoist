# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

from qfluentwidgets import (HyperlinkButton, LineEdit, PrimaryPushButton)
import Icon_qrc_rc
import Icon_qrc_rc
import Icon_qrc_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1040, 536)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -20, 671, 561))
        self.label.setStyleSheet(u"border-image: url(:/icon/NISAR_AutoC.jpeg);")
        self.label.setPixmap(QPixmap(u":/icon/NISAR_AutoC.jpeg"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 631, 271))
        font = QFont()
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QFrame.Shadow.Plain)
        self.label_3.setTextFormat(Qt.TextFormat.RichText)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 510, 681, 20))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 1141, 551))
        self.frame.setStyleSheet(u"    background-color: rgb(251, 251, 251);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(900, 20, 61, 41))
        self.pushButton_2.setStyleSheet(u"#pushButton_2 {\n"
"    border: none;\n"
"    background-color: rgb(251, 251, 251);\n"
"    color: rgb(0, 0, 0); \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton_2:hover {\n"
"    background-color: rgb(240, 240, 240); \n"
"    color: rgb(0, 0, 0); \n"
"}\n"
"\n"
"#pushButton_2:pressed {\n"
"    background-color: rgb(200, 200, 200); \n"
"    color: rgb(0, 0, 0); \n"
"    padding-top: 3px;\n"
"    padding-left: 3px;\n"
"}")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(970, 20, 61, 41))
        self.pushButton.setStyleSheet(u"#pushButton {\n"
"    background-color: rgb(251, 251, 251); \n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"    background-color: rgb(240, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#pushButton:pressed {\n"
"    background-color: rgb(220, 50, 50);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(720, 40, 251, 151))
        self.label_2.setPixmap(QPixmap(u":/icon/sarmates.png"))
        self.label_2.setScaledContents(True)
        self.Main_exit = HyperlinkButton(self.frame)
        self.Main_exit.setObjectName(u"Main_exit")
        self.Main_exit.setGeometry(QRect(690, 460, 281, 31))
        self.Main_Login = PrimaryPushButton(self.frame)
        self.Main_Login.setObjectName(u"Main_Login")
        self.Main_Login.setGeometry(QRect(690, 410, 281, 31))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(700, 300, 121, 21))
        self.lineEdit = LineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(690, 250, 281, 31))
        self.lineEdit_2 = LineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(690, 330, 281, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(700, 220, 101, 31))
        self.label_2.raise_()
        self.Main_exit.raise_()
        self.Main_Login.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_7.raise_()

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.showMinimized)
        self.pushButton.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700; font-style:italic; color:#00ffff;\">SAR-SoMoist V.1.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#00ffff;\">A High-Reolution Soil Moisture Retrieval and Mapping "
                        "With SAR and Passive Microwave Remote Sensing Dataset Software</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">SARmates Group . The Ownership of SAR-SoMoist Software Lies in the Research Group of Dr.Hongtao Shi (2025)</span></p><p><br/></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u2573", None))
        self.label_2.setText("")
        self.Main_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.Main_Login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">PASSWORD</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Please enter username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Please enter password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">USER</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>", None))
    # retranslateUi

