from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import tickets, users

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)

        self.setFixedSize(500, 300)
        self.setWindowTitle("Tickets")
        numticket = 2
        label = QLabel("", self)
        label.setGeometry(0, 0, 500, 30)
        label.setStyleSheet("background:#424242; color:#fff")
        # QCoreApplication.translate("Tickets", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>"f"{numticket}", None)

        label.setText(f"<html><head/><body><p align=\"center\">Tickets # {numticket}</p></body></html>")
        # print(f"El ancho de este label es: {label.frameGeometry().width()} \nY el alto es: {label.frameGeometry().height()}")


        # Label Estado Ticket
        self.labelEstado = QLabel("", self)
        self.labelEstado.setGeometry(60, 40, 115, 30)
        self.labelEstado.setText("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Descripción</span></p></body></html>")
        # --------------------------------
        # Input Descripcion Ticket
        self.inputEstado = QTextEdit(self)
        self.inputEstado.setGeometry(180, 40, 200, 100)
        # --------------------------------
        # Label Abierto el Día
        self.labelAbierto = QLabel("", self)
        self.labelAbierto.setGeometry(60, 145, 115, 30)
        self.labelAbierto.setText("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abierto el día</span></p></body></html>")
        
        self.labelFecha = QLabel("", self)
        self.labelFecha.setGeometry(180, 145, 200, 30)
        self.labelFecha.setText(f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#29cc38;\">{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</span></p></body></html>")
        # self.labelEstado.setStyleSheet("border-color:#000; border-width: 1.2px; border-style: inset;")
        # self.labelAbierto.setStyleSheet("border-color:#000; border-width: 1.2px; border-style: inset;")
        # --------------------------------
        # Informado Label
        self.labelInformado = QLabel("", self)
        self.labelInformado.setGeometry(60, 175, 115, 30)
        self.labelInformado.setText("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Informado</span></p></body></html>")
        self.labelInformado.setStyleSheet("border-color:#000; border-width: 1.2px; border-style: inset;")

        self.comboboxInformado = QComboBox(self)
        self.comboboxInformado.setGeometry(180, 175, 200, 30)
        self.comboboxInformado.addItem("ANDRES DAVID NAVARRO DE LA HOZ")
        self.comboboxInformado.addItem("WILFREDO SNEIDER URIBE BETANCUR")
        self.comboboxInformado.addItem("BLANCA SUSANA GARCIA CASTRO")
        self.comboboxInformado.addItem("RAUL HUMBERTO  RUA MARTINEZ")
        # --------------------------------


        # self.btn = QPushButton("Presioname", self)
        # self.btn.setGeometry(0, 30, 100, 30)
        # # print(f"Ancho {btn.frameGeometry().width()} \nAlto: {btn.frameGeometry().height()}")
        # self.btn.clicked.connect(self.say_hello)
        

class MenuApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MenuApp, self).__init__(parent=parent)
        self.setFixedSize(300, 200)
        self.setWindowTitle("Sistema de Tickets")
        
        self.btnTickets = QPushButton("New TICKETS", self)
        self.btnTickets.setGeometry(30, 30, 100, 30)
        # print(f"Ancho {btn.frameGeometry().width()} \nAlto: {btn.frameGeometry().height()}")
        
        self.mainm = tickets.MainApp()
        self.btnTickets.clicked.connect(self.mainTickets)

        self.btnUsers = QPushButton("Usuarios", self)
        self.btnUsers.setGeometry(160, 30, 100, 30)
        self.btnUsers.clicked.connect(self.mainUsers)

        self.usersMain = users.UsersApp()

    def mainTickets(self):
        self.mainm.show()
    
    def mainUsers(self):
        self.usersMain.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MenuApp()
    window.show()
    app.exec_()