from datetime import datetime

from PyQt5 import QtCore
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


def setTextContUsers(self):
        self.labelTitle.setText("AGREGAR USUARIOS")
        self.labelCedula.setText("Cedula")
        self.labelUsuario.setText("Usuario")
        self.labelNombre.setText("Nombre")
        self.labelEquipo.setText("Equipo")
        self.labelExt.setText("Ext")
        self.labelBy.setText("By: De la Hoz")
        self.buttonAgregar.setText("Agregar")
        self.buttonCerrar.setText("Cerrar")
        self.buttonAddUsers.setText("Add Users")
        self.buttonEditUsers.setText("Edit Users")
        self.buttonEditar.setText("Editar")
        self.buttonEliminar.setText("Eliminar")

class UiTickets_Function:
    def setFunctions(self):
        self.buttonCerrar.clicked.connect(lambda: self.close())
        self.cerrarBtn.clicked.connect(lambda: self.close())
        showUsers(self.usuariosBox)
        
        def moveWindows(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPos)
                self.clickPos = event.globalPos()
                event.accept()

        self.leftTitle.mouseMoveEvent = moveWindows

    def addTitle(self):
        self.titulo.setText(f"{showLastTicket()+1}# Tickets {showDateNow()} ")

       
        

        




def functionAgregar(self):
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