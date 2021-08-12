from datetime import datetime
from . import bdsql


def showUsers(comboBox):
    """
    The function adds items to the comoboBox (Informado)
    Parameters:
        comboBox: A combobox where you want to add the values of the names
    """
    list = bdsql.showUsersNoms()
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
    list = bdsql.tableTickets()
    for a in list:
        if a[1] == "Abierto":
            return (a[0])

def searchTicket(NoTicket):
    list = bdsql.tableTickets()
    for a in list:
        if a[0] == NoTicket:
            return a
        
def ticketAbierto():
    list = bdsql.tableTickets()
    for a in list:
        if a[1] == "Abierto":
            return a[0]
            break
    return "Sin tickets abiertos"

def cerrarTicket(Noticket, DescripcionResuelto, CerradoDia):
    return bdsql.tableResueltoWrite(Noticket, DescripcionResuelto, CerradoDia)


def setTextCont(self):
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