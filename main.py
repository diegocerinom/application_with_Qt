import sys
from ui_design.ui_mainWindows import *
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation

class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.ui.Header.mouseMoveEvent = self.move_windows

        self.ui.btn_minimize.clicked.connect(self.set_minimize)
        self.ui.btn_restore.clicked.connect(self.set_restore)
        self.ui.btn_maximize.clicked.connect(self.set_maximize)
        self.ui.btn_exit.clicked.connect(lambda: self.close())
        self.ui.btn_restore.hide()
        
        self.ui.checkBox_1.stateChanged.connect(self.option)
        self.ui.checkBox_2.stateChanged.connect(self.option)
        self.ui.checkBox_3.stateChanged.connect(self.option)
        self.checkGroup_previous_state = [self.ui.checkBox_1.isChecked(), self.ui.checkBox_2.isChecked(), self.ui.checkBox_3.isChecked()]


    def set_minimize(self):
        self.showMinimized()		
        
    def set_restore(self): 
        self.showNormal()
        self.ui.btn_restore.hide()
        self.ui.btn_maximize.show()
        
    def set_maximize(self):
        self.showMaximized()
        self.ui.btn_maximize.hide()
        self.ui.btn_restore.show()
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def move_windows(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

            if event.globalPos().y() <=20:
                self.showMaximized()
            else:
                self.showNormal()

    def menu_open(self):
        width = self.ui.menu_config.width()
        if width==2:
            extender = 210
            self.animacion = QPropertyAnimation(self.ui.menu_config, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def menu_close(self):
        width = self.ui.menu_config.width()
        if width>2:
            extender = 2
            self.animacion = QPropertyAnimation(self.ui.menu_config, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def option(self):
        checkGroup_actual_state = [self.ui.checkBox_1.isChecked(), self.ui.checkBox_2.isChecked(), self.ui.checkBox_3.isChecked()]
        #print(checkGroup_actual_state)
        thereAreOne = [x for x in range(len(checkGroup_actual_state)) if checkGroup_actual_state[x] ==True]
        if len(thereAreOne) > 1:
            #print("there is more than one")
            for p in thereAreOne:
                if checkGroup_actual_state[p] == self.checkGroup_previous_state[p]:
                    #print(i)
                    if p == 0:
                        self.ui.checkBox_1.setChecked(False)
                    if p == 1:
                        self.ui.checkBox_2.setChecked(False)
                    if p == 2:
                        self.ui.checkBox_3.setChecked(False)
                    break
        elif len(thereAreOne) == 1:
            self.checkGroup_previous_state = [self.ui.checkBox_1.isChecked(), self.ui.checkBox_2.isChecked(), self.ui.checkBox_3.isChecked()]
            if thereAreOne[0] == 0:
                self.ui.pg_configs.setCurrentWidget(self.ui.pg_config_1)
            if thereAreOne[0] == 1:
                self.ui.pg_configs.setCurrentWidget(self.ui.pg_config_2)
            if thereAreOne[0] == 2:
                self.ui.pg_configs.setCurrentWidget(self.ui.pg_config_3)
            self.menu_open()

        else:
            self.menu_close()

if __name__ == "__main__":
     application = QApplication(sys.argv)
     app = mainApp()
     app.show()
     sys.exit(application.exec_())
