from datetime import datetime
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QSizeGrip, QTableWidgetItem
from . bdsql import *

def showUsers(comboBox):
    """
    The function adds items to the comoboBox (Informado)
    Parameters:
        comboBox: A combobox where you want to add the values of the names
    """
    list = sql_table_show("Users")
    for a in range(len(list)):
        comboBox.addItem(list[a][1])

def showDateNow():
    """
    The function return date now
    Returns:
        datetime: The current date - example 05/08/2021 07:57:24
    """
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def showTicketOpen():
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
    for a in list:
        if a[1] == "Abierto":
            return a[0]
            break
    return "Sin tickets abiertos"

def cerrarTicket(Noticket, DescripcionResuelto, CerradoDia):
    return tableResueltoWrite(Noticket, DescripcionResuelto, CerradoDia)

# class BtnDefault:
#     self.cerrarBtn.clicked.connect(lambda: self.close())


class UiTickets_Function:
    def setFunctionsTicket(self):
        self.buttonCerrar.clicked.connect(lambda: self.close())
        self.cerrarBtn.clicked.connect(lambda: self.close())
        showUsers(self.usuariosBox)

        self.msg = QMessageBox(self.styles)
        QSizeGrip(self.verticalFrame1)
        
                
        def moveWindows(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPos)
                self.clickPos = event.globalPos()
                event.accept()

        self.leftTitle.mouseMoveEvent = moveWindows

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
    

class UiUser_Function:
    def setFunctionUser(self):
        self.buttonCerrar.clicked.connect(lambda: self.close())
        self.cerrarBtn.clicked.connect(lambda: self.close())
        self.buttonAddUsers.clicked.connect(lambda: self.centerContPage.setCurrentWidget(self.page))

        self.msg = QMessageBox(self.styles)
        QSizeGrip(self.verticalFrame)
        
        
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
        
        UiResolver.cerrarBtn.clicked.connect(lambda: UiResolver.close())
        
        def moveWindows(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                UiResolver.move(UiResolver.pos() + event.globalPos() - UiResolver.clickPos)
                UiResolver.clickPos = event.globalPos()
                event.accept()

        UiResolver.topCont.mouseMoveEvent = moveWindows
        UiResolver.label.mouseMoveEvent = moveWindows
        QSizeGrip(UiResolver.verticalFrame) 
        

        NoTick = showTicketOpen()
        msg = QMessageBox(UiResolver.styles)
        msg.setObjectName(u"msg")
        PrioColor = {
            'Baja': "<span style='color:green'> Baja </span>",
            'Media': "<span style='color:orange'> Media </span>",
            'Alta': "<span style='color:red'> Alta </span>"
        }
        if NoTick is None:
            msg.setText("No hay tickets")
            msg.exec_()
            UiResolver.label.setText("No hay ticket")
            UiResolver.labelDescripcion.setText("Descripcion: N/A")
            UiResolver.labelPrioridad.setText("Prioridad: N/A")
            UiResolver.labelInformado.setText("Informado: N/A")
        else:
            UiResolver.label.setText(f"TICKET# {showTicketOpen()}")
            UiResolver.labelDescripcion.setText(f"Descripcion: <p style='color:red'>{searchTicket(showLastTicket())[3]}</p>")
            try:
                UiResolver.labelPrioridad.setText(f"Prioridad: {PrioColor[searchTicket(showTicketOpen())[2]]}")
            except:
                UiResolver.labelPrioridad.setText("Prioridad: N/A")
            
            UiResolver.labelInformado.setText(f"Informado: {searchTicket(NoTick)[5]}")

        
