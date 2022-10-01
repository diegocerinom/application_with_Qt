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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

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
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.Header)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setStyleSheet(u"*{\n"
"boede:0px;\n"
"}\n"
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
        self.menu_side_left = QFrame(self.Content)
        self.menu_side_left.setObjectName(u"menu_side_left")
        self.menu_side_left.setMinimumSize(QSize(0, 0))
        self.menu_side_left.setMaximumSize(QSize(250, 16777215))
        self.menu_side_left.setLayoutDirection(Qt.LeftToRight)
        self.menu_side_left.setAutoFillBackground(False)
        self.menu_side_left.setStyleSheet(u"")
        self.menu_side_left.setFrameShape(QFrame.StyledPanel)
        self.menu_side_left.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.menu_side_left)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QFrame(self.menu_side_left)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(50, 0))
        self.menu_bar.setMaximumSize(QSize(50, 16777215))
        self.menu_bar.setStyleSheet(u"border: none;\n"
"background-color: rgb(99, 99, 99);")
        self.menu_bar.setFrameShape(QFrame.StyledPanel)
        self.menu_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_bar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_1 = QCheckBox(self.menu_bar)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_1.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 47px;\n"
"    height: 47px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(images/icons/settings.png);\n"
"	border-left: 3px solid  rgb(99, 99, 99);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(images/icons/settings.png);\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-left: 3px solid #ffffff;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(images/icons/settings.png);\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-left: 3px solid #ffffff;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.menu_bar)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 47px;\n"
"    height: 47px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(images/icons/settings.png);\n"
"	border-left: 3px solid  rgb(99, 99, 99);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(images/icons/settings.png);\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-left: 3px solid #ffffff;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(images/icons/settings.png);\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-left: 3px solid #ffffff;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.menu_bar)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 47px;\n"
"    height: 47px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(images/icons/settings.png);\n"
"	border-left: 3px solid  rgb(99, 99, 99);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(images/icons/settings.png);\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-left: 3px solid #ffffff;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(images/icons/settings.png);\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-left: 3px solid #ffffff;\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.verticalSpacer = QSpacerItem(20, 399, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_account = QPushButton(self.menu_bar)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"images/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_account.setIcon(icon4)
        self.btn_account.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_account)

        self.btn_config = QPushButton(self.menu_bar)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"images/icons/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_config.setIcon(icon5)
        self.btn_config.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_config)

        self.label_2 = QLabel(self.menu_bar)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.menu_bar, 0, Qt.AlignLeft)

        self.menu_config = QFrame(self.menu_side_left)
        self.menu_config.setObjectName(u"menu_config")
        self.menu_config.setMinimumSize(QSize(0, 0))
        self.menu_config.setMaximumSize(QSize(210, 16777215))
        self.menu_config.setStyleSheet(u"borde:0px;\n"
"background-color: rgb(234, 234, 234);")
        self.menu_config.setFrameShape(QFrame.StyledPanel)
        self.menu_config.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menu_config)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pg_configs = QStackedWidget(self.menu_config)
        self.pg_configs.setObjectName(u"pg_configs")
        self.pg_config_1 = QWidget()
        self.pg_config_1.setObjectName(u"pg_config_1")
        self.label_3 = QLabel(self.pg_config_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 49, 16))
        self.pg_configs.addWidget(self.pg_config_1)
        self.pg_config_2 = QWidget()
        self.pg_config_2.setObjectName(u"pg_config_2")
        self.label_4 = QLabel(self.pg_config_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 49, 16))
        self.pg_configs.addWidget(self.pg_config_2)
        self.pg_config_3 = QWidget()
        self.pg_config_3.setObjectName(u"pg_config_3")
        self.label_8 = QLabel(self.pg_config_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 49, 16))
        self.pg_configs.addWidget(self.pg_config_3)
        self.pg_config_4 = QWidget()
        self.pg_config_4.setObjectName(u"pg_config_4")
        self.label_9 = QLabel(self.pg_config_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 49, 16))
        self.pg_configs.addWidget(self.pg_config_4)

        self.verticalLayout_4.addWidget(self.pg_configs)


        self.horizontalLayout_3.addWidget(self.menu_config, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.menu_side_left)

        self.viwe_pages = QFrame(self.Content)
        self.viwe_pages.setObjectName(u"viwe_pages")
        self.viwe_pages.setFrameShape(QFrame.StyledPanel)
        self.viwe_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.viwe_pages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.viwe_pages)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 49, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 49, 16))
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.viwe_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pg_configs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_minimize.setText("")
        self.btn_restore.setText("")
        self.btn_maximize.setText("")
        self.btn_exit.setText("")
        self.checkBox_1.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.btn_account.setText("")
        self.btn_config.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"config 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"config 2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"config 3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"config 4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"View 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"View 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

