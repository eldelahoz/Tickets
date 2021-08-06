from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from modules import functions
from css import stylescss

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.resize(790, 600)
        self.setWindowTitle("Tickets")
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        self.styles.setStyleSheet(stylescss.stylesincss())
        # Ocultar los bordes de ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Contenedor contenido
        self.contenidoBox = QFrame(self.styles)
        self.contenidoBox.setObjectName(u"contenidoBox")
        self.contenidoBoxLayout = QVBoxLayout(self.contenidoBox)
        self.contenidoBoxLayout.setObjectName(u"contenidoBoxLayout")
        # Contenido top barra
        self.topCont = QFrame(self.contenidoBox)
        self.topCont.setObjectName(u"topCont")
        self.topCont.setMinimumSize(0, 50)
        self.topCont.setMaximumSize(16777215, 50)
        self.topContLayout = QHBoxLayout(self.topCont)
        self.topContLayout.setObjectName(u"topContLayout")
        self.leftTitle = QFrame(self.topCont)
        self.leftTitle.setObjectName(u"leftTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTitle.sizePolicy().hasHeightForWidth())
        self.leftTitle.setSizePolicy(sizePolicy)
        self.leftTitleLayout = QHBoxLayout(self.leftTitle)
        self.leftTitleLayout.setObjectName(u"leftTitleLayout")
        # Agregas el titlo izquiero al contenido de top bar
        self.topContLayout.addWidget(self.leftTitle)
        # Agregamos un label para el titulo izquierdo
        self.titulo = QLabel(self.leftTitle)
        self.titulo.setText(f"{functions.bdsql.showLastTicket()+1}# Tickets {functions.showDateNow()} ")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.leftTitleLayout.addWidget(self.titulo)
        # Bottones lado derecho top bar
        self.buttonRight = QFrame(self.topCont)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setMinimumSize(0, 28)
        self.buttonRightLayout = QHBoxLayout(self.buttonRight)
        self.buttonRightLayout.setObjectName(u"buttonRightLayout")
        self.buttonRightLayout.setContentsMargins(0,0,0,0)
        # Boton minimizar
        self.minimizarBtn = QPushButton(self.buttonRight)
        self.minimizarBtn.setObjectName(u"minimizarBtn")
        self.minimizarBtn.clicked.connect(lambda: self.showMinimized())
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimizarBtn.sizePolicy().hasHeightForWidth())
        self.minimizarBtn.setSizePolicy(sizePolicy1)
        self.minimizarBtn.setMinimumSize(28, 28)
        self.minimizarBtn.setMaximumSize(28, 28)
        #Icon boton minimizar
        minimizarIcon  = QtGui.QIcon()
        minimizarIcon.addFile("images/icons/icon_minimize.png")
        self.minimizarBtn.setIcon(minimizarIcon)
        self.minimizarBtn.setIconSize(QtCore.QSize(20,20))
        # Agregamos el boton de minizar
        self.buttonRightLayout.addWidget(self.minimizarBtn)
        # Boton maximizar
        self.maximizarBtn = QPushButton(self.buttonRight)
        self.maximizarBtn.setObjectName(u"maximizarBtn")
        self.maximizarBtn.setMinimumSize(28, 28)
        self.maximizarBtn.setMaximumSize(28, 28)
        self.maximizarBtn.clicked.connect(lambda: self.showMaximized())
        # Icon boton maximizar
        maximizarIcon = QtGui.QIcon()
        maximizarIcon.addFile("images/icons/icon_maximize.png")
        self.maximizarBtn.setIcon(maximizarIcon)
        self.maximizarBtn.setIconSize(QtCore.QSize(20,20))
        # Agregamos el boton de maximizar
        self.buttonRightLayout.addWidget(self.maximizarBtn)
        # Boton de cerrar
        self.cerrarBtn = QPushButton(self.buttonRight)
        self.cerrarBtn.setObjectName(u"cerrarBtn")
        self.cerrarBtn.setMinimumSize(28, 28)
        self.cerrarBtn.setMaximumSize(28, 28)
        self.cerrarBtn.clicked.connect(lambda: self.close())
        # Icon boton cerrar
        cerrarIcon = QtGui.QIcon()
        cerrarIcon.addFile("images/icons/icon_close.png")
        self.cerrarBtn.setIcon(cerrarIcon)
        self.cerrarBtn.setIconSize(QtCore.QSize(20,20))
        # Agregamos el boton de cerrar
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
        self.labelDescripcion.setText("Descripcion")

        self.bottomContLayout.addWidget(self.labelDescripcion)

        self.textDescripcion = QTextEdit(self.bottomCont)
        self.textDescripcion.setObjectName(u"textDescripcion")

        self.bottomContLayout.addWidget(self.textDescripcion)
        # ----------------Medium Contect---------------------
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
        self.labelPrioridad.setText("Prioridad")
        self.leftmediumContLayout.addWidget(self.labelPrioridad)

        self.prioridadBox = QComboBox(self.leftmediumCont)
        self.prioridadBox.addItem("Baja")
        self.prioridadBox.addItem("Media")
        self.prioridadBox.addItem("Alta")
        self.prioridadBox.setObjectName(u"prioridadBox")

        self.leftmediumContLayout.addWidget(self.prioridadBox)


        self.mediumContLayout.addWidget(self.leftmediumCont)

        self.rightmediumCont = QFrame(self.mediumCont)
        self.rightmediumCont.setObjectName(u"rightmediumCont")
        self.rightmediumContLayout = QVBoxLayout(self.rightmediumCont)
        self.rightmediumContLayout.setObjectName(u"rightmediumContLayout")
        self.labelInformado = QLabel(self.rightmediumCont)
        self.labelInformado.setObjectName(u"labelInformado")
        self.labelInformado.setText("Informado")
        self.rightmediumContLayout.addWidget(self.labelInformado)

        self.usuariosBox = QComboBox(self.rightmediumCont)
        self.usuariosBox.setObjectName(u"usuariosBox")
        functions.showUsers(self.usuariosBox)
        self.rightmediumContLayout.addWidget(self.usuariosBox)


        self.mediumContLayout.addWidget(self.rightmediumCont)


        self.bottomContLayout.addWidget(self.mediumCont)

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
        self.buttonAgregar.setText("Agregar")
        self.buttonAgregar.clicked.connect(lambda: self.functionAgregar())
        # self.buttonAgregar.clicked.connect(lambda: print(self.usuariosBox.currentText() + self.textDescripcion.toPlainText()))

        self.buttonsEndLayout_2.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsEnd2)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QtCore.QSize(125, 50))
        self.buttonCerrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonCerrar.setText("Cerrar")
        self.buttonCerrar.clicked.connect(lambda: self.close())

        self.buttonsEndLayout_2.addWidget(self.buttonCerrar)


        self.buttonsEndLayout.addWidget(self.buttonsEnd2)


        self.bottomContLayout.addWidget(self.buttonsEnd)

        self.labelBy = QLabel(self.bottomCont)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelBy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBy.setText("By: De la Hoz")

        self.bottomContLayout.addWidget(self.labelBy)


        self.contenidoBoxLayout.addWidget(self.bottomCont)


        self.stylesLayout.addWidget(self.contenidoBox)
        # Asignacion del widget central
        self.setCentralWidget(self.styles)

    def functionAgregar(self):
        msg = QMessageBox()
        if functions.bdsql.tableTicketsWrite(self.prioridadBox.currentText(),self.textDescripcion.toPlainText(),functions.showDateNow(),self.usuariosBox.currentText()) is None:
            msg.setText("Ticket agregado correctamente")
        else:
            msg.setText("No se pudo agregar el ticket")
        return msg.exec_()
        
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()