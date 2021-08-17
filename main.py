from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import tickets, users, resolver
from css import stylescss

class MenuApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MenuApp, self).__init__(parent=parent)
        self.setFixedSize(300, 200)
        self.setWindowTitle("Sistema de Tickets")
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        self.styles.setStyleSheet(stylescss.stylesincss())
        self.btnTickets = QPushButton("New TICKETS", self)
        self.btnTickets.setGeometry(30, 30, 100, 40)     
        self.btnTickets.clicked.connect(lambda: self.mainTickets())

        self.btnUsers = QPushButton("Usuarios", self)
        self.btnUsers.setGeometry(160, 30, 100, 40)
        self.btnUsers.clicked.connect(lambda: self.mainUsers())

        self.btnResolver = QPushButton("Resolver", self)
        self.btnResolver.setGeometry(95, 80, 100, 40)
        self.btnResolver.clicked.connect(lambda: self.mainResolver())

        self.setCentralWidget(self.styles)

    def mainTickets(self):
        mainTicket = tickets.MainApp()
        return mainTicket.show()
    
    def mainUsers(self):
        usersMain = users.UsersApp()
        return usersMain.show()

    def mainResolver(self):
        resolverMain = resolver.ResolverApp()
        return resolverMain.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MenuApp()
    window.show()
    app.exec_()