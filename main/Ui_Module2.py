# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Module2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import Icon_qrc_rc

class Ui_retrieval(object):
    def setupUi(self, retrieval):
        if not retrieval.objectName():
            retrieval.setObjectName(u"retrieval")
        retrieval.resize(1139, 839)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(retrieval.sizePolicy().hasHeightForWidth())
        retrieval.setSizePolicy(sizePolicy)
        retrieval.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(retrieval)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(retrieval)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(246, 250, 252);border-image: url(:/icon/sarmates.png);")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_4 = QLabel(retrieval)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(246, 250, 252);")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 35)
        self.horizontalLayout_3.setStretch(2, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line = QFrame(retrieval)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, 0)
        self.Out_path_select_4 = QPushButton(retrieval)
        self.Out_path_select_4.setObjectName(u"Out_path_select_4")
        sizePolicy.setHeightForWidth(self.Out_path_select_4.sizePolicy().hasHeightForWidth())
        self.Out_path_select_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.Out_path_select_4.setFont(font)
        self.Out_path_select_4.setStyleSheet(u"#Out_path_select_4{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#Out_path_select_4:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#Out_path_select_4:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.verticalLayout.addWidget(self.Out_path_select_4)

        self.textBrowser_5 = QTextBrowser(retrieval)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"color:rgb(100,100,150);\n"
"border-radius:3px;\n"
"border:1px solid rgb(200,200,200);\n"
"\n"
"")

        self.verticalLayout.addWidget(self.textBrowser_5)

        self.Retrieval_button = QPushButton(retrieval)
        self.Retrieval_button.setObjectName(u"Retrieval_button")
        sizePolicy.setHeightForWidth(self.Retrieval_button.sizePolicy().hasHeightForWidth())
        self.Retrieval_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.Retrieval_button.setFont(font1)
        self.Retrieval_button.setStyleSheet(u"#Retrieval_button{\n"
"    background-color: rgb(255, 130, 100);\n"
"color: rgb(245, 245,245);\n"
"    font: 700 14pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#Retrieval_button:hover{\n"
"	background-color: rgb(255, 100, 80);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#Retrieval_button:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}")

        self.verticalLayout.addWidget(self.Retrieval_button)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(retrieval)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(246, 250, 252);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.cmap_combo = QComboBox(retrieval)
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.setObjectName(u"cmap_combo")
        self.cmap_combo.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.cmap_combo)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(retrieval)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(246, 250, 252);")

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.View_Soil_Moisture_button = QPushButton(retrieval)
        self.View_Soil_Moisture_button.setObjectName(u"View_Soil_Moisture_button")
        sizePolicy.setHeightForWidth(self.View_Soil_Moisture_button.sizePolicy().hasHeightForWidth())
        self.View_Soil_Moisture_button.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.View_Soil_Moisture_button.setFont(font2)
        self.View_Soil_Moisture_button.setStyleSheet(u"#View_Soil_Moisture_button{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#View_Soil_Moisture_button:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#View_Soil_Moisture_button:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.verticalLayout.addWidget(self.View_Soil_Moisture_button)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 5)
        self.verticalLayout.setStretch(5, 5)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_3 = QFrame(retrieval)
        self.line_3.setObjectName(u"line_3")
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graphicsView_4 = QGraphicsView(retrieval)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(200,200,200);\n"
"border-radius:10px;")

        self.verticalLayout_6.addWidget(self.graphicsView_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SME_min = QLineEdit(retrieval)
        self.SME_min.setObjectName(u"SME_min")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SME_min.sizePolicy().hasHeightForWidth())
        self.SME_min.setSizePolicy(sizePolicy1)
        self.SME_min.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_2.addWidget(self.SME_min)

        self.label_10 = QLabel(retrieval)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border-image: url(:/icon/parula_part_2_1.png);")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.SME_max = QLineEdit(retrieval)
        self.SME_max.setObjectName(u"SME_max")
        sizePolicy1.setHeightForWidth(self.SME_max.sizePolicy().hasHeightForWidth())
        self.SME_max.setSizePolicy(sizePolicy1)
        self.SME_max.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_2.addWidget(self.SME_max)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.setStretch(0, 17)
        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 100)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(retrieval)
        self.line_2.setObjectName(u"line_2")
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.verticalLayout_3.setStretch(0, 9)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 120)
        self.verticalLayout_3.setStretch(3, 3)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.line_4 = QFrame(retrieval)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)


        self.retranslateUi(retrieval)

        QMetaObject.connectSlotsByName(retrieval)
    # setupUi

    def retranslateUi(self, retrieval):
        retrieval.setWindowTitle(QCoreApplication.translate("retrieval", u"Form", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("retrieval", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:14pt; font-weight:700; color:#d23d2f;\">Module-2 Soil Moisture Estimation</span></p></body></html>", None))
        self.Out_path_select_4.setText(QCoreApplication.translate("retrieval", u"  Set the file path and filename \n"
"of results (Click here!)", None))
        self.textBrowser_5.setPlaceholderText(QCoreApplication.translate("retrieval", u"Set the file path and filename of results\uff01", None))
        self.Retrieval_button.setText(QCoreApplication.translate("retrieval", u"Begining Retrieval\n"
"(Click Here!)", None))
        self.label_2.setText(QCoreApplication.translate("retrieval", u"               Pseudo-color rendering:", None))
        self.cmap_combo.setItemText(0, QCoreApplication.translate("retrieval", u"jet", None))
        self.cmap_combo.setItemText(1, QCoreApplication.translate("retrieval", u"viridis", None))
        self.cmap_combo.setItemText(2, QCoreApplication.translate("retrieval", u"hot", None))
        self.cmap_combo.setItemText(3, QCoreApplication.translate("retrieval", u"cool", None))
        self.cmap_combo.setItemText(4, QCoreApplication.translate("retrieval", u"rainbow", None))
        self.cmap_combo.setItemText(5, QCoreApplication.translate("retrieval", u"terrain", None))

        self.label_3.setText(QCoreApplication.translate("retrieval", u"             Select the smoothing level:", None))
        self.View_Soil_Moisture_button.setText(QCoreApplication.translate("retrieval", u"View Soil Moisture Results And \n"
" Pseudo color rendering     ", None))
        self.label_10.setText("")
    # retranslateUi

