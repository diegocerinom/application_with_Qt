# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindows.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 565)
        MainWindow.setMinimumSize(QSize(40, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 40))
        self.Header.setMaximumSize(QSize(16777215, 40))
        self.Header.setLayoutDirection(Qt.LeftToRight)
        self.Header.setAutoFillBackground(False)
        self.Header.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(372, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.Header)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"borde:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"borde:5px solid #aa00ff;\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_restore = QPushButton(self.Header)
        self.btn_restore.setObjectName(u"btn_restore")
        self.btn_restore.setStyleSheet(u"QPushButton{\n"
"borde:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"borde:5px solid #aa00ff;\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restore.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_restore)

        self.btn_maximize = QPushButton(self.Header)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"borde:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"borde:5px solid #aa00ff;\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_exit = QPushButton(self.Header)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setStyleSheet(u"QPushButton{\n"
"borde:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"borde:5px solid #aa00ff;\n"
"	background-color: rgb(144, 144, 144);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.Header)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_side = QFrame(self.Content)
        self.menu_side.setObjectName(u"menu_side")
        self.menu_side.setMinimumSize(QSize(95, 0))
        self.menu_side.setMaximumSize(QSize(250, 16777215))
        self.menu_side.setLayoutDirection(Qt.LeftToRight)
        self.menu_side.setAutoFillBackground(False)
        self.menu_side.setStyleSheet(u"background-color: rgb(79, 79, 79);")
        self.menu_side.setFrameShape(QFrame.StyledPanel)
        self.menu_side.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.menu_side)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_menu = QPushButton(self.menu_side)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"borde:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"borde:5px solid #aa00ff;\n"
"background-color: rgb(144, 144, 144);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/option.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon4)
        self.btn_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.btn_menu)

        self.pushButton = QPushButton(self.menu_side)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.menu_side)

        self.viwe_pages = QFrame(self.Content)
        self.viwe_pages.setObjectName(u"viwe_pages")
        self.viwe_pages.setFrameShape(QFrame.StyledPanel)
        self.viwe_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.viwe_pages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.viwe_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.viwe_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_minimize.setText("")
        self.btn_restore.setText("")
        self.btn_maximize.setText("")
        self.btn_exit.setText("")
        self.btn_menu.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"*", None))
    # retranslateUi

