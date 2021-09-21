from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# Packages external
from modules import Ui_Ticket, Ui_Resolver, Ui_User
import modules
from modules.functions import *

class MenuApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MenuApp, self).__init__(parent=parent)
        self.setFixedSize(300, 200)
        self.setWindowTitle("Sistema de Tickets")
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")

        self.styles.setStyleSheet("#styles{background-color: rgb(40, 44, 52)}")
        
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        
        self.btnTickets = QPushButton("Tickets", self)
        self.btnTickets.setGeometry(30, 30, 100, 40)

        self.mainTicket = Ui_Ticket()
        UiTickets_Function.setFunctionsTicket(self.mainTicket)

        self.btnTickets.clicked.connect(lambda: self.mainTicket.show())

        self.btnUsers = QPushButton("Usuarios", self)
        self.btnUsers.setGeometry(160, 30, 100, 40)
        self.mainUser = Ui_User()
        UiTickets_Function.setFunctionUser(self.mainUser)
        self.btnUsers.clicked.connect(lambda: self.mainUser.show())
        

        self.btnResolver = QPushButton("Resolver", self)
        self.btnResolver.setGeometry(95, 80, 100, 40)
        self.mainResolver = Ui_Resolver()
        UiResolver_Function(self.mainResolver)
        
        self.btnResolver.clicked.connect(lambda: self.mainResolver.show())


        self.setCentralWidget(self.styles)

if __name__ == '__main__':
    app = QApplication([])
    window = MenuApp()
    window.show()
    app.exec_()