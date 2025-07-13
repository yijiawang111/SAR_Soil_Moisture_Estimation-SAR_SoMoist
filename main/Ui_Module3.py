# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Module3.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_TimeSeries(object):
    def setupUi(self, TimeSeries):
        if not TimeSeries.objectName():
            TimeSeries.setObjectName(u"TimeSeries")
        TimeSeries.resize(1090, 797)
        self.verticalLayout_3 = QVBoxLayout(TimeSeries)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(TimeSeries)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(249, 249, 249);")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Out_path_select_6 = QPushButton(TimeSeries)
        self.Out_path_select_6.setObjectName(u"Out_path_select_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Out_path_select_6.sizePolicy().hasHeightForWidth())
        self.Out_path_select_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.Out_path_select_6.setFont(font)
        self.Out_path_select_6.setStyleSheet(u"#Out_path_select_6{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 13pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#Out_path_select_6:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#Out_path_select_6:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.verticalLayout.addWidget(self.Out_path_select_6)

        self.textBrowser_t = QTextBrowser(TimeSeries)
        self.textBrowser_t.setObjectName(u"textBrowser_t")
        sizePolicy.setHeightForWidth(self.textBrowser_t.sizePolicy().hasHeightForWidth())
        self.textBrowser_t.setSizePolicy(sizePolicy)
        self.textBrowser_t.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"color:rgb(100,100,150);\n"
"border-radius:3px;\n"
"border:1px solid rgb(220,220,220);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout.addWidget(self.textBrowser_t)

        self.TimeSeries_2 = QPushButton(TimeSeries)
        self.TimeSeries_2.setObjectName(u"TimeSeries_2")
        sizePolicy.setHeightForWidth(self.TimeSeries_2.sizePolicy().hasHeightForWidth())
        self.TimeSeries_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.TimeSeries_2.setFont(font1)
        self.TimeSeries_2.setStyleSheet(u"#TimeSeries_2{\n"
"background-color: rgb(255, 130, 100);\n"
"color: rgb(245, 245,245);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#TimeSeries_2:hover{\n"
"background-color: rgb(255, 100, 80);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#TimeSeries_2:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.verticalLayout.addWidget(self.TimeSeries_2)

        self.pushButton_TSA = QPushButton(TimeSeries)
        self.pushButton_TSA.setObjectName(u"pushButton_TSA")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_TSA.sizePolicy().hasHeightForWidth())
        self.pushButton_TSA.setSizePolicy(sizePolicy1)
        self.pushButton_TSA.setStyleSheet(u"#pushButton_TSA{\n"
"background-color: rgb(255, 130, 100);\n"
"color: rgb(245, 245,245);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#pushButton_TSA:hover{\n"
"background-color: rgb(255, 100, 80);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#pushButton_TSA:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_TSA)

        self.pushButton_csv = QPushButton(TimeSeries)
        self.pushButton_csv.setObjectName(u"pushButton_csv")
        sizePolicy1.setHeightForWidth(self.pushButton_csv.sizePolicy().hasHeightForWidth())
        self.pushButton_csv.setSizePolicy(sizePolicy1)
        self.pushButton_csv.setStyleSheet(u"#pushButton_csv{\n"
"background-color: rgb(255, 130, 100);\n"
"color: rgb(245, 245,245);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#pushButton_csv:hover{\n"
"background-color: rgb(255, 100, 80);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#pushButton_csv:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_csv)

        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 15)
        self.verticalLayout.setStretch(2, 20)
        self.verticalLayout.setStretch(3, 10)
        self.verticalLayout.setStretch(4, 10)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(TimeSeries)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.graphicsView_6 = QGraphicsView(TimeSeries)
        self.graphicsView_6.setObjectName(u"graphicsView_6")
        self.graphicsView_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(200,200,200);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.graphicsView_6)

        self.horizontalLayout.setStretch(0, 27)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 100)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(TimeSeries)

        QMetaObject.connectSlotsByName(TimeSeries)
    # setupUi

    def retranslateUi(self, TimeSeries):
        TimeSeries.setWindowTitle(QCoreApplication.translate("TimeSeries", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("TimeSeries", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:14pt; font-weight:700; color:#d23d2f;\">Module-3 Time Series Analysis</span></p></body></html>", None))
        self.Out_path_select_6.setText(QCoreApplication.translate("TimeSeries", u"Set the file path you \n"
"  want to analyze here!  ", None))
        self.textBrowser_t.setPlaceholderText(QCoreApplication.translate("TimeSeries", u"The path to your file will be displayed here!", None))
        self.TimeSeries_2.setText(QCoreApplication.translate("TimeSeries", u"TimeSeries Analysis", None))
        self.pushButton_TSA.setText(QCoreApplication.translate("TimeSeries", u"Save Analysis Images\n"
" To Folder", None))
        self.pushButton_csv.setText(QCoreApplication.translate("TimeSeries", u"Save Data To Csv", None))
    # retranslateUi

