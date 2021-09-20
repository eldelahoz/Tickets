from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from . bdsql import *

def showUsers(comboBox):
    """
    The function adds items to the comoboBox (Informado)
    Parameters:
        comboBox: A combobox where you want to add the values of the names
    """
    list = showUsersNoms()
    for a in range(len(list)):
        comboBox.addItem(list[a][0])

def showDateNow():
    """
    The function return date now
    Returns:
        datetime: The current date - example 05/08/2021 07:57:24
    """
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def showTickets():
    list = tableTickets()
    for a in list:
        if a[1] == "Abierto":
            return (a[0])

def searchTicket(NoTicket):
    list = tableTickets()
    for a in list:
        if a[0] == NoTicket:
            return a
        
def ticketAbierto():
    list = tableTickets()
    for a in list:
        if a[1] == "Abierto":
            return a[0]
            break
    return "Sin tickets abiertos"

def cerrarTicket(Noticket, DescripcionResuelto, CerradoDia):
    return tableResueltoWrite(Noticket, DescripcionResuelto, CerradoDia)

class MoveWindows_UI:
    def __init__(self) -> None:
        def moveWindows(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPos)
                self.clickPos = event.globalPos()
                event.accept()


class UiTickets_Function(MoveWindows_UI):
    def setFunctionsTicket(self):
        self.buttonCerrar.clicked.connect(lambda: self.close())
        self.cerrarBtn.clicked.connect(lambda: self.close())
        showUsers(self.usuariosBox)
                

        self.leftTitle.mouseMoveEvent = MoveWindows_UI

        def functionAgregar():
            if self.textDescripcion.toPlainText() != "":
                if tableTicketsAdd(self.prioridadBox.currentText(),self.textDescripcion.toPlainText(),showDateNow(),self.usuariosBox.currentText()) is None:
                    self.msg.setText("Ticket agregado correctamente")
                    self.msg.setWindowTitle("TICKET AGREGADO")
                    self.textDescripcion.clear()
                else:
                    self.msg.setWindowTitle("NO SE AGREGO EL TICKET")
                    self.msg.setText("No se pudo agregar el ticket")
            else:
                self.msg.setWindowTitle("NO SE AGREGO EL TICKET")
                self.msg.setText("No puede agregar un ticket <span style='color:red'>sin descripcion</span>.")

            if self.msg.exec_() == 0:
                self.close()

        self.buttonAgregar.clicked.connect(lambda: functionAgregar())

    def addTitle(self):
        self.titulo.setText(f"{showLastTicket()+1}# Tickets {showDateNow()} ")
    
    def setFunctionUser(self):
        self.buttonCerrar.clicked.connect(lambda: self.close())
        self.cerrarBtn.clicked.connect(lambda: self.close())
        self.buttonAddUsers.clicked.connect(lambda: self.centerContPage.setCurrentWidget(self.page))
        
        
        def moveWindows(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPos)
                self.clickPos = event.globalPos()
                event.accept()

        self.topCont.mouseMoveEvent = moveWindows
       
        def agregarUser():
            a = tableUsersWrite(self.lineEditCedula.text(), self.lineEditNombre.text(), self.lineEditUsuario.text(), self.lineEditEquipo.text(), self.lineEditExt.text())
            
            if(a is None):
                self.lineEditCedula.clear()
                self.lineEditUsuario.clear()
                self.lineEditNombre.clear()
                self.lineEditEquipo.clear()
                self.lineEditExt.clear()
                self.msg.setWindowTitle("AGREGAR")
                self.msg.setText("USUARIO AGREGADO")
                img = QtGui.QPixmap("images/icons/agregar-usuario.png").scaledToHeight(32)
                self.msg.setIconPixmap(img)
                self.msg.setText("Usuario fue agregado con exito")
            else:
                self.msg.setWindowTitle("AGREGAR")
                self.msg.setText(f"El usuario con este numero de cedula {self.lineEditCedula.text()} ya existe")
        
            self.msg.exec_()

        self.buttonAgregar.clicked.connect(lambda: agregarUser())

        def showViewUser():
            self.tableWidget.setRowCount(showCountUser())
            for i in range(showCountUser()):
                for j in range(5):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(sql_table_show("Users")[i][j]))
            self.centerContPage.setCurrentWidget(self.page_2)
        
        self.buttonEditUsers.clicked.connect(lambda: showViewUser())

class UiResolver_Function:

    def __init__(self, UiResolver):
        UiResolver.buttonCerrar.clicked.connect(lambda: UiResolver.close())

