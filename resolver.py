from modules.bdsql import tableUsersWrite
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from modules import functions
from css import stylescss

class ResolverApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(ResolverApp, self).__init__(parent=parent)
        self.resize(800, 500)
        self.setWindowTitle("Tickets")
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(stylescss.stylesincss())
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        
        # Ocultar los bordes de ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.contenidoBox = QFrame(self.styles)
        self.contenidoBox.setObjectName(u"contenidoBox")
        self.contenidoBoxLayout = QVBoxLayout(self.contenidoBox)
        self.contenidoBoxLayout.setObjectName(u"contenidoBoxLayout")
        self.topCont = QFrame(self.contenidoBox)
        self.topCont.setObjectName(u"topCont")
        self.topCont.setMinimumSize(QtCore.QSize(0, 50))
        self.topCont.setMaximumSize(QtCore.QSize(16777215, 50))
        self.topContLayout = QHBoxLayout(self.topCont)
        self.topContLayout.setObjectName(u"topContLayout")
        # Move Windows
        def moveWindows(event):
            if self.isMaximized() == False:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPos)
                    self.clickPos = event.globalPos()
                    event.accept()
        self.topCont.mouseMoveEvent = moveWindows

        self.leftTitle = QFrame(self.topCont)
        self.leftTitle.setObjectName(u"leftTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTitle.sizePolicy().hasHeightForWidth())
        self.leftTitle.setSizePolicy(sizePolicy)
        self.leftTitleLayout = QHBoxLayout(self.leftTitle)
        self.leftTitleLayout.setObjectName(u"leftTitleLayout")
        self.label = QLabel(self.leftTitle)
        self.label.setObjectName(u"label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.leftTitleLayout.addWidget(self.label)


        self.topContLayout.addWidget(self.leftTitle)

        self.buttonRight = QFrame(self.topCont)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setMinimumSize(QtCore.QSize(0, 28))
        self.buttonRightLayout = QHBoxLayout(self.buttonRight)
        self.buttonRightLayout.setObjectName(u"buttonRightLayout")
        self.buttonRightLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizarBtn = QPushButton(self.buttonRight)
        self.minimizarBtn.setObjectName(u"minimizarBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimizarBtn.sizePolicy().hasHeightForWidth())
        self.minimizarBtn.setSizePolicy(sizePolicy1)
        self.minimizarBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.minimizarBtn.setMaximumSize(QtCore.QSize(28, 28))
        icon = QtGui.QIcon()
        icon.addFile(u"images/icons/icon_minimize.png")
        self.minimizarBtn.setIcon(icon)
        self.minimizarBtn.setIconSize(QtCore.QSize(20, 16))

        self.buttonRightLayout.addWidget(self.minimizarBtn)

        self.maximizarBtn = QPushButton(self.buttonRight)
        self.maximizarBtn.setObjectName(u"maximizarBtn")
        self.maximizarBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.maximizarBtn.setMaximumSize(QtCore.QSize(28, 28))
        icon1 = QtGui.QIcon()
        icon1.addFile(u"images/icons/icon_maximize.png")
        self.maximizarBtn.setIcon(icon1)
        self.maximizarBtn.setIconSize(QtCore.QSize(20, 20))

        self.buttonRightLayout.addWidget(self.maximizarBtn)

        self.cerrarBtn = QPushButton(self.buttonRight)
        self.cerrarBtn.setObjectName(u"cerrarBtn")
        self.cerrarBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.cerrarBtn.setMaximumSize(QtCore.QSize(28, 28))
        icon2 = QtGui.QIcon()
        icon2.addFile(u"images/icons/icon_close.png")
        self.cerrarBtn.setIcon(icon2)
        self.cerrarBtn.setIconSize(QtCore.QSize(20, 20))
        self.cerrarBtn.clicked.connect(lambda: self.close())

        self.buttonRightLayout.addWidget(self.cerrarBtn)


        self.topContLayout.addWidget(self.buttonRight)


        self.contenidoBoxLayout.addWidget(self.topCont)

        self.bottomCont = QFrame(self.contenidoBox)
        self.bottomCont.setObjectName(u"bottomCont")
        self.bottomCont.setMinimumSize(QtCore.QSize(0, 50))
        self.bottomContLayout = QVBoxLayout(self.bottomCont)
        self.bottomContLayout.setObjectName(u"bottomContLayout")
        self.labelDescripcion = QLabel(self.bottomCont)
        self.labelDescripcion.setObjectName(u"labelDescripcion")

        self.bottomContLayout.addWidget(self.labelDescripcion)

        self.mediumCont = QFrame(self.bottomCont)
        self.mediumCont.setObjectName(u"mediumCont")
        self.mediumContLayout = QHBoxLayout(self.mediumCont)
        self.mediumContLayout.setObjectName(u"mediumContLayout")
        self.leftmediumCont = QFrame(self.mediumCont)
        self.leftmediumCont.setObjectName(u"leftmediumCont")
        self.leftmediumContLayout = QVBoxLayout(self.leftmediumCont)
        self.leftmediumContLayout.setObjectName(u"leftmediumContLayout")
        self.labelPrioridad = QLabel(self.leftmediumCont)
        self.labelPrioridad.setObjectName(u"labelPrioridad")

        self.leftmediumContLayout.addWidget(self.labelPrioridad)


        self.mediumContLayout.addWidget(self.leftmediumCont)

        self.rightmediumCont = QFrame(self.mediumCont)
        self.rightmediumCont.setObjectName(u"rightmediumCont")
        self.rightmediumContLayout = QVBoxLayout(self.rightmediumCont)
        self.rightmediumContLayout.setObjectName(u"rightmediumContLayout")
        self.labelInformado = QLabel(self.rightmediumCont)
        self.labelInformado.setObjectName(u"labelInformado")

        self.rightmediumContLayout.addWidget(self.labelInformado)


        self.mediumContLayout.addWidget(self.rightmediumCont)


        self.bottomContLayout.addWidget(self.mediumCont)

        self.textEdit = QTextEdit(self.bottomCont)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        
        self.bottomContLayout.addWidget(self.textEdit)

        self.buttonsEnd = QFrame(self.bottomCont)
        self.buttonsEnd.setObjectName(u"buttonsEnd")
        self.buttonsEnd.setMinimumSize(QtCore.QSize(0, 80))
        self.buttonsEnd.setMaximumSize(QtCore.QSize(16777215, 80))
        self.buttonsEnd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonsEndLayout = QVBoxLayout(self.buttonsEnd)
        self.buttonsEndLayout.setObjectName(u"buttonsEndLayout")
        self.buttonsEnd2 = QFrame(self.buttonsEnd)
        self.buttonsEnd2.setObjectName(u"buttonsEnd2")
        self.buttonsEndLayout_2 = QHBoxLayout(self.buttonsEnd2)
        self.buttonsEndLayout_2.setObjectName(u"buttonsEndLayout_2")
        self.buttonAgregar = QPushButton(self.buttonsEnd2)
        self.buttonAgregar.setObjectName(u"buttonAgregar")
        self.buttonAgregar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonAgregar.setMaximumSize(QtCore.QSize(125, 50))
        self.buttonAgregar.clicked.connect(lambda: self.agregarResolver())

        self.buttonsEndLayout_2.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsEnd2)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QtCore.QSize(125, 50))
        self.buttonCerrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonCerrar.clicked.connect(lambda: self.close())

        self.buttonsEndLayout_2.addWidget(self.buttonCerrar)


        self.buttonsEndLayout.addWidget(self.buttonsEnd2)


        self.bottomContLayout.addWidget(self.buttonsEnd)

        self.labelBy = QLabel(self.bottomCont)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelBy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.bottomContLayout.addWidget(self.labelBy)


        self.contenidoBoxLayout.addWidget(self.bottomCont)


        self.stylesLayout.addWidget(self.contenidoBox)

        self.setTextResolver()
        self.ticketActual()
        self.setCentralWidget(self.styles)
    
    def setTextResolver(self):
        self.labelBy.setText("By: De la Hoz")
        self.buttonAgregar.setText("Agregar")
        self.buttonCerrar.setText("Cerrar")
        
    def ticketActual(self):
        NoTick = functions.showTickets()
        msg = QMessageBox(self.styles)
        if NoTick is None:
            msg.setText("No hay tickets")
            msg.exec_()
            self.label.setText("No hay ticket")
            self.labelDescripcion.setText("Descripcion: N/A")
            self.labelPrioridad.setText("Prioridad: N/A")
            self.labelInformado.setText("Informado: N/A")
        else:
            self.label.setText(f"TICKET# {functions.showTickets()}")
            self.labelDescripcion.setText(f"Descripcion: {functions.searchTicket(functions.showTickets())[3]}")
            self.labelPrioridad.setText(f"Prioridad: {functions.searchTicket(functions.showTickets())[2]}")
            self.labelInformado.setText(f"Informado: {functions.searchTicket(functions.showTickets())[5]}")
        
        

    def agregarResolver(self):
        msg = QMessageBox(self.styles)
        ticket = functions.showTickets()
        if ticket is not None:
            a = functions.cerrarTicket(functions.showTickets(), self.textEdit.toPlainText(), functions.showDateNow())
            if a is None:
                msg.setText(f"El Ticket # {ticket} fue cerrado")
        else:
            msg.setText(f"No se pudo cerrar el ticket")
        msg.exec_()

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        self.clickPos = a0.globalPos()
        
if __name__ == '__main__':
    app = QApplication([])
    window = ResolverApp()
    window.show()
    app.exec_()