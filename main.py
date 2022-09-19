import sys
from ui_mainWindows import *
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
        
        self.ui.btn_menu.clicked.connect(self.move_menu)

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

    def move_menu(self):
        if True:			
            width = self.ui.menu_side.width()
            normal = 95
            if width==95:
                extender = 250
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.menu_side, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()



if __name__ == "__main__":
     application = QApplication(sys.argv)
     app = mainApp()
     app.show()
     sys.exit(application.exec_())
