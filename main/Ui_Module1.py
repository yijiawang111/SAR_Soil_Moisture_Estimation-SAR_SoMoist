# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Module1.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)
import Icon_qrc_rc

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(1097, 829)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainwindow.sizePolicy().hasHeightForWidth())
        mainwindow.setSizePolicy(sizePolicy)
        mainwindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(mainwindow)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 3)
        self.label_18 = QLabel(mainwindow)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border-image: url(:/icon/sarmates.png);\n"
"background-color: rgb(246, 250, 252);")

        self.horizontalLayout_4.addWidget(self.label_18)

        self.label = QLabel(mainwindow)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(246, 250, 252);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 35)
        self.horizontalLayout_4.setStretch(2, 5)

        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(mainwindow)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"#textBrowser{\n"
"background-color:rgb(245,245,245);\n"
"color:rgb(100,100,150);\n"
"border-radius:3px;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.textBrowser_2 = QTextBrowser(mainwindow)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setStyleSheet(u"#textBrowser_2{\n"
"background-color:rgb(245,245,245);\n"
"color:rgb(100,100,150);\n"
"border-radius:3px;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.textBrowser_2)

        self.textBrowser_4 = QTextBrowser(mainwindow)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setStyleSheet(u"#textBrowser_4{\n"
"background-color:rgb(245,245,245);\n"
"color:rgb(100,100,150);\n"
"border-radius:3px;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.textBrowser_4)

        self.textBrowser_3 = QTextBrowser(mainwindow)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setStyleSheet(u"#textBrowser_3{\n"
"background-color:rgb(245,245,245);\n"
"color:rgb(100,100,150);\n"
"border-radius:3px;\n"
"border:1px solid rgb(200,200,200);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.textBrowser_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SAR_path_select = QPushButton(mainwindow)
        self.SAR_path_select.setObjectName(u"SAR_path_select")
        self.SAR_path_select.setMinimumSize(QSize(60, 30))
        self.SAR_path_select.setStyleSheet(u"#SAR_path_select{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"	font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#SAR_path_select:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#SAR_path_select:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_2.addWidget(self.SAR_path_select)

        self.Passive_path_select_2 = QPushButton(mainwindow)
        self.Passive_path_select_2.setObjectName(u"Passive_path_select_2")
        self.Passive_path_select_2.setMinimumSize(QSize(60, 30))
        self.Passive_path_select_2.setStyleSheet(u"#Passive_path_select_2{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#Passive_path_select_2:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#Passive_path_select_2:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_2.addWidget(self.Passive_path_select_2)

        self.Passive_path_select_3 = QPushButton(mainwindow)
        self.Passive_path_select_3.setObjectName(u"Passive_path_select_3")
        self.Passive_path_select_3.setMinimumSize(QSize(60, 30))
        self.Passive_path_select_3.setStyleSheet(u"#Passive_path_select_3{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#Passive_path_select_3:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#Passive_path_select_3:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_2.addWidget(self.Passive_path_select_3)

        self.SARINC_path_select_3 = QPushButton(mainwindow)
        self.SARINC_path_select_3.setObjectName(u"SARINC_path_select_3")
        self.SARINC_path_select_3.setMinimumSize(QSize(60, 30))
        self.SARINC_path_select_3.setStyleSheet(u"#SARINC_path_select_3{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#SARINC_path_select_3:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"#SARINC_path_select_3:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_2.addWidget(self.SARINC_path_select_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.verticalLayout_13.addLayout(self.horizontalLayout_18)

        self.line = QFrame(mainwindow)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(mainwindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(246, 250, 252);color: rgb(255, 85, 0);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.SAR_max = QLineEdit(mainwindow)
        self.SAR_max.setObjectName(u"SAR_max")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SAR_max.sizePolicy().hasHeightForWidth())
        self.SAR_max.setSizePolicy(sizePolicy3)
        self.SAR_max.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_6.addWidget(self.SAR_max)

        self.horizontalLayout_6.setStretch(0, 9)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.graphicsView = QGraphicsView(mainwindow)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(200,200,200);\n"
"border-radius:10px;")

        self.horizontalLayout_9.addWidget(self.graphicsView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(mainwindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border-image: url(:/icon/parula_part_2.png);")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.horizontalLayout_9.setStretch(0, 14)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.Pseudo_color_rendering_1 = QPushButton(mainwindow)
        self.Pseudo_color_rendering_1.setObjectName(u"Pseudo_color_rendering_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Pseudo_color_rendering_1.sizePolicy().hasHeightForWidth())
        self.Pseudo_color_rendering_1.setSizePolicy(sizePolicy4)
        self.Pseudo_color_rendering_1.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_7.addWidget(self.Pseudo_color_rendering_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.SAR_min = QLineEdit(mainwindow)
        self.SAR_min.setObjectName(u"SAR_min")
        sizePolicy3.setHeightForWidth(self.SAR_min.sizePolicy().hasHeightForWidth())
        self.SAR_min.setSizePolicy(sizePolicy3)
        self.SAR_min.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_7.addWidget(self.SAR_min)

        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 11)
        self.horizontalLayout_7.setStretch(2, 3)
        self.horizontalLayout_7.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line_3 = QFrame(mainwindow)
        self.line_3.setObjectName(u"line_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy5)
        self.line_3.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(mainwindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(246, 250, 252);color: rgb(255, 85, 0);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.Passive_max = QLineEdit(mainwindow)
        self.Passive_max.setObjectName(u"Passive_max")
        sizePolicy3.setHeightForWidth(self.Passive_max.sizePolicy().hasHeightForWidth())
        self.Passive_max.setSizePolicy(sizePolicy3)
        self.Passive_max.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_8.addWidget(self.Passive_max)

        self.horizontalLayout_8.setStretch(0, 9)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.graphicsView_3 = QGraphicsView(mainwindow)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(200,200,200);\n"
"border-radius:10px;")

        self.horizontalLayout_13.addWidget(self.graphicsView_3)

        self.label_4 = QLabel(mainwindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border-image: url(:/icon/parula_part_2.png);")

        self.horizontalLayout_13.addWidget(self.label_4)

        self.horizontalLayout_13.setStretch(0, 14)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.Pseudo_color_rendering_2 = QPushButton(mainwindow)
        self.Pseudo_color_rendering_2.setObjectName(u"Pseudo_color_rendering_2")
        sizePolicy4.setHeightForWidth(self.Pseudo_color_rendering_2.sizePolicy().hasHeightForWidth())
        self.Pseudo_color_rendering_2.setSizePolicy(sizePolicy4)
        self.Pseudo_color_rendering_2.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_10.addWidget(self.Pseudo_color_rendering_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.Passive_min = QLineEdit(mainwindow)
        self.Passive_min.setObjectName(u"Passive_min")
        sizePolicy3.setHeightForWidth(self.Passive_min.sizePolicy().hasHeightForWidth())
        self.Passive_min.setSizePolicy(sizePolicy3)
        self.Passive_min.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_10.addWidget(self.Passive_min)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 11)
        self.horizontalLayout_10.setStretch(2, 3)
        self.horizontalLayout_10.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3.setStretch(0, 60)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 60)

        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(mainwindow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy5)
        self.line_2.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(mainwindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(246, 250, 252);color: rgb(255, 85, 0);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_7)

        self.Passive_max_2 = QLineEdit(mainwindow)
        self.Passive_max_2.setObjectName(u"Passive_max_2")
        sizePolicy3.setHeightForWidth(self.Passive_max_2.sizePolicy().hasHeightForWidth())
        self.Passive_max_2.setSizePolicy(sizePolicy3)
        self.Passive_max_2.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_14.addWidget(self.Passive_max_2)

        self.horizontalLayout_14.setStretch(0, 9)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.graphicsView_10 = QGraphicsView(mainwindow)
        self.graphicsView_10.setObjectName(u"graphicsView_10")
        self.graphicsView_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(200,200,200);\n"
"border-radius:10px;")

        self.horizontalLayout_15.addWidget(self.graphicsView_10)

        self.label_3 = QLabel(mainwindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-image: url(:/icon/parula_part_2.png);")

        self.horizontalLayout_15.addWidget(self.label_3)

        self.horizontalLayout_15.setStretch(0, 14)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.Pseudo_color_rendering_3 = QPushButton(mainwindow)
        self.Pseudo_color_rendering_3.setObjectName(u"Pseudo_color_rendering_3")
        sizePolicy4.setHeightForWidth(self.Pseudo_color_rendering_3.sizePolicy().hasHeightForWidth())
        self.Pseudo_color_rendering_3.setSizePolicy(sizePolicy4)
        self.Pseudo_color_rendering_3.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_11.addWidget(self.Pseudo_color_rendering_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.Passive_min_2 = QLineEdit(mainwindow)
        self.Passive_min_2.setObjectName(u"Passive_min_2")
        sizePolicy3.setHeightForWidth(self.Passive_min_2.sizePolicy().hasHeightForWidth())
        self.Passive_min_2.setSizePolicy(sizePolicy3)
        self.Passive_min_2.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_11.addWidget(self.Passive_min_2)

        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(1, 11)
        self.horizontalLayout_11.setStretch(2, 3)
        self.horizontalLayout_11.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 5)
        self.verticalLayout_5.setStretch(2, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.line_5 = QFrame(mainwindow)
        self.line_5.setObjectName(u"line_5")
        sizePolicy5.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy5)
        self.line_5.setStyleSheet(u"background-color:rgb(245,245,245);\n"
"border:none;\n"
"")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(mainwindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgb(246, 250, 252);color: rgb(255, 85, 0);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.SARInc_max = QLineEdit(mainwindow)
        self.SARInc_max.setObjectName(u"SARInc_max")
        sizePolicy3.setHeightForWidth(self.SARInc_max.sizePolicy().hasHeightForWidth())
        self.SARInc_max.setSizePolicy(sizePolicy3)
        self.SARInc_max.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_16.addWidget(self.SARInc_max)

        self.horizontalLayout_16.setStretch(0, 9)
        self.horizontalLayout_16.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.graphicsView_2 = QGraphicsView(mainwindow)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(200,200,200);\n"
"border-radius:10px;")

        self.horizontalLayout_17.addWidget(self.graphicsView_2)

        self.label_9 = QLabel(mainwindow)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border-image: url(:/icon/parula_part_2.png);")

        self.horizontalLayout_17.addWidget(self.label_9)

        self.horizontalLayout_17.setStretch(0, 14)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.Pseudo_color_rendering_4 = QPushButton(mainwindow)
        self.Pseudo_color_rendering_4.setObjectName(u"Pseudo_color_rendering_4")
        sizePolicy4.setHeightForWidth(self.Pseudo_color_rendering_4.sizePolicy().hasHeightForWidth())
        self.Pseudo_color_rendering_4.setSizePolicy(sizePolicy4)
        self.Pseudo_color_rendering_4.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,190,190);\n"
"color:rgb(255,255,255);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 167,179);\n"
"color:rgb(240,240,240)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-top:3px;\n"
"padding-left:3px;}\n"
"")

        self.horizontalLayout_12.addWidget(self.Pseudo_color_rendering_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.SARInc_min = QLineEdit(mainwindow)
        self.SARInc_min.setObjectName(u"SARInc_min")
        sizePolicy3.setHeightForWidth(self.SARInc_min.sizePolicy().hasHeightForWidth())
        self.SARInc_min.setSizePolicy(sizePolicy3)
        self.SARInc_min.setStyleSheet(u"background-color: rgb(246, 250, 252);border: 1px solid #CCCCCC;")

        self.horizontalLayout_12.addWidget(self.SARInc_min)

        self.horizontalLayout_12.setStretch(0, 3)
        self.horizontalLayout_12.setStretch(1, 11)
        self.horizontalLayout_12.setStretch(2, 3)
        self.horizontalLayout_12.setStretch(3, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 5)
        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.horizontalLayout_5.setStretch(0, 60)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 60)

        self.verticalLayout_13.addLayout(self.horizontalLayout_5)

        self.verticalLayout_13.setStretch(0, 5)
        self.verticalLayout_13.setStretch(1, 9)
        self.verticalLayout_13.setStretch(2, 3)
        self.verticalLayout_13.setStretch(4, 2)
        self.verticalLayout_13.setStretch(5, 30)
        self.verticalLayout_13.setStretch(6, 2)
        self.verticalLayout_13.setStretch(7, 30)

        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"Form", None))
        self.label_18.setText("")
        self.label.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p><span style=\" font-family:'.AppleSystemUIFont'; font-size:14pt; font-weight:700; color:#d23d2f;\">Module-1 Input Data</span></p></body></html>", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("mainwindow", u"Step-1:Set the file path of SAR datasets here! (The path to your file will be displayed here!)", None))
        self.textBrowser_2.setPlaceholderText(QCoreApplication.translate("mainwindow", u"Step-2 Set the file path of Maximum Passive data! (The path to your file will be displayed here!)", None))
        self.textBrowser_4.setPlaceholderText(QCoreApplication.translate("mainwindow", u"Step-3 Set the file path of Minimum Passive data! (The path to your file will be displayed here!)", None))
        self.textBrowser_3.setPlaceholderText(QCoreApplication.translate("mainwindow", u"Step-4 Set the file path of incidence angle dataset! (The path to your file will be displayed here!)", None))
#if QT_CONFIG(tooltip)
        self.SAR_path_select.setToolTip(QCoreApplication.translate("mainwindow", u"Click here to select your data file!", None))
#endif // QT_CONFIG(tooltip)
        self.SAR_path_select.setText(QCoreApplication.translate("mainwindow", u"Step-1", None))
#if QT_CONFIG(tooltip)
        self.Passive_path_select_2.setToolTip(QCoreApplication.translate("mainwindow", u"Click here to select your data file!", None))
#endif // QT_CONFIG(tooltip)
        self.Passive_path_select_2.setText(QCoreApplication.translate("mainwindow", u"Step-2", None))
#if QT_CONFIG(tooltip)
        self.Passive_path_select_3.setToolTip(QCoreApplication.translate("mainwindow", u"Click here to select your data file!", None))
#endif // QT_CONFIG(tooltip)
        self.Passive_path_select_3.setText(QCoreApplication.translate("mainwindow", u"Step-3", None))
#if QT_CONFIG(tooltip)
        self.SARINC_path_select_3.setToolTip(QCoreApplication.translate("mainwindow", u"Click here to select your data file!", None))
#endif // QT_CONFIG(tooltip)
        self.SARINC_path_select_3.setText(QCoreApplication.translate("mainwindow", u"Step-4", None))
        self.label_5.setText(QCoreApplication.translate("mainwindow", u"Step-1:The results to your file will be displayed below!", None))
        self.label_2.setText("")
        self.Pseudo_color_rendering_1.setText(QCoreApplication.translate("mainwindow", u"    Pseudo color rendering    ", None))
        self.label_6.setText(QCoreApplication.translate("mainwindow", u"Step-2:The results to your file will be displayed below!", None))
        self.label_4.setText("")
        self.Pseudo_color_rendering_2.setText(QCoreApplication.translate("mainwindow", u"    Pseudo color rendering    ", None))
        self.label_7.setText(QCoreApplication.translate("mainwindow", u"Step-3:The results to your file will be displayed below!", None))
        self.label_3.setText("")
        self.Pseudo_color_rendering_3.setText(QCoreApplication.translate("mainwindow", u"    Pseudo color rendering    ", None))
        self.label_8.setText(QCoreApplication.translate("mainwindow", u"Step-4:The results to your file will be displayed below!", None))
        self.label_9.setText("")
        self.Pseudo_color_rendering_4.setText(QCoreApplication.translate("mainwindow", u"    Pseudo color rendering    ", None))
    # retranslateUi

