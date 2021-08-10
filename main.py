from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import tickets, users

class MenuApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MenuApp, self).__init__(parent=parent)
        self.setFixedSize(300, 200)
        self.setWindowTitle("Sistema de Tickets")
        
        self.btnTickets = QPushButton("New TICKETS", self)
        self.btnTickets.setGeometry(30, 30, 100, 30)
        # print(f"Ancho {btn.frameGeometry().width()} \nAlto: {btn.frameGeometry().height()}")
        
        
        self.btnTickets.clicked.connect(lambda: self.mainTickets())

        self.btnUsers = QPushButton("Usuarios", self)
        self.btnUsers.setGeometry(160, 30, 100, 30)
        self.btnUsers.clicked.connect(lambda: self.mainUsers())


    def mainTickets(self):
        mainTicket = tickets.MainApp()
        return mainTicket.show()
    
    def mainUsers(self):
        usersMain = users.UsersApp()
        return usersMain.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MenuApp()
    window.show()
    app.exec_()