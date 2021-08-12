from modules.bdsql import tableUsersWrite
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from modules import functions
from css import stylescss

class UsersApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(UsersApp, self).__init__(parent=parent)
        self.resize(680, 250)
        self.setWindowTitle("Users")
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(stylescss.stylesincss())
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        self.contUsers = QWidget(self.styles)
        self.contUsers.setObjectName(u"contUsers")
        self.contUsersLayout = QVBoxLayout(self.contUsers)
        self.contUsersLayout.setObjectName(u"contUsersLayout")
        self.topCont = QWidget(self.contUsers)
        self.topCont.setObjectName(u"topCont")
        self.topCont.setMinimumSize(QtCore.QSize(0, 50))
        self.topCont.setMaximumSize(QtCore.QSize(16777215, 50))
        self.topContLayout = QHBoxLayout(self.topCont)
        self.topContLayout.setObjectName(u"topContLayout")
        self.leftTitle = QWidget(self.topCont)
        self.leftTitle.setObjectName(u"leftTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTitle.sizePolicy().hasHeightForWidth())
        self.leftTitle.setSizePolicy(sizePolicy)
        self.leftTitleLayout = QHBoxLayout(self.leftTitle)
        self.leftTitleLayout.setObjectName(u"leftTitleLayout")
        self.labelTitle = QLabel(self.leftTitle)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)

        self.leftTitleLayout.addWidget(self.labelTitle)


        self.topContLayout.addWidget(self.leftTitle)

        self.buttonRight = QWidget(self.topCont)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setMinimumSize(QtCore.QSize(0, 28))
        self.buttonRightLayout = QHBoxLayout(self.buttonRight)
        self.buttonRightLayout.setObjectName(u"buttonRightLayout")
        self.buttonRightLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizarBtn = QPushButton(self.buttonRight)
        self.minimizarBtn.setObjectName(u"minimizarBtn")
        self.minimizarBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.minimizarBtn.setMaximumSize(QtCore.QSize(28, 28))
        icon = QtGui.QIcon()
        icon.addFile(u"images/icons/icon_minimize.png")
        self.minimizarBtn.setIcon(icon)
        self.minimizarBtn.setIconSize(QtCore.QSize(20, 20))

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
        icon2.addFile("images/icons/icon_close.png")
        self.cerrarBtn.setIcon(icon2)
        self.cerrarBtn.setIconSize(QtCore.QSize(20, 20))
        self.cerrarBtn.clicked.connect(lambda: self.close())

        self.buttonRightLayout.addWidget(self.cerrarBtn)


        self.topContLayout.addWidget(self.buttonRight)


        self.contUsersLayout.addWidget(self.topCont)

        self.bottomCont = QWidget(self.contUsers)
        self.bottomCont.setObjectName(u"bottomCont")
        self.bottomContLayout = QVBoxLayout(self.bottomCont)
        self.bottomContLayout.setObjectName(u"bottomContLayout")
        self.centerCont = QFrame(self.bottomCont)
        self.centerCont.setObjectName(u"centerCont")
        self.centerContLayout = QHBoxLayout(self.centerCont)
        self.centerContLayout.setObjectName(u"centerContLayout")
        self.centerContLayout.setContentsMargins(9, 9, 9, 9)
        self.leftcenterCont = QFrame(self.centerCont)
        self.leftcenterCont.setObjectName(u"leftcenterCont")
        self.leftcenterContLayout = QVBoxLayout(self.leftcenterCont)
        self.leftcenterContLayout.setObjectName(u"leftcenterContLayout")
        self.leftcenterContLayout.setContentsMargins(9, 9, 9, 9)
        self.labelCedula = QLabel(self.leftcenterCont)
        self.labelCedula.setObjectName(u"labelCedula")

        self.leftcenterContLayout.addWidget(self.labelCedula)

        self.lineEditCedula = QLineEdit(self.leftcenterCont)
        self.lineEditCedula.setObjectName(u"lineEditCedula")
        self.lineEditCedula.setMinimumSize(300,0)

        self.leftcenterContLayout.addWidget(self.lineEditCedula)

        self.labelUsuario = QLabel(self.leftcenterCont)
        self.labelUsuario.setObjectName(u"labelUsuario")

        self.leftcenterContLayout.addWidget(self.labelUsuario)

        self.lineEditUsuario = QLineEdit(self.leftcenterCont)
        self.lineEditUsuario.setObjectName(u"lineEditUsuario")

        self.leftcenterContLayout.addWidget(self.lineEditUsuario)


        self.centerContLayout.addWidget(self.leftcenterCont)

        self.rightcenterCont = QFrame(self.centerCont)
        self.rightcenterCont.setObjectName(u"rightcenterCont")
        self.rightcenterContLayout = QVBoxLayout(self.rightcenterCont)
        self.rightcenterContLayout.setObjectName(u"rightcenterContLayout")
        self.rightcenterContLayout.setContentsMargins(9, 9, 9, 9)
        self.labelNombre = QLabel(self.rightcenterCont)
        self.labelNombre.setObjectName(u"labelNombre")

        self.rightcenterContLayout.addWidget(self.labelNombre)

        self.lineEditNombre = QLineEdit(self.rightcenterCont)
        self.lineEditNombre.setObjectName(u"lineEditNombre")
        self.lineEditNombre.setMinimumSize(300,0)

        self.rightcenterContLayout.addWidget(self.lineEditNombre)

        self.labelEquipo = QLabel(self.rightcenterCont)
        self.labelEquipo.setObjectName(u"labelEquipo")

        self.rightcenterContLayout.addWidget(self.labelEquipo)

        self.lineEditEquipo = QLineEdit(self.rightcenterCont)
        self.lineEditEquipo.setObjectName(u"lineEditEquipo")

        self.rightcenterContLayout.addWidget(self.lineEditEquipo)


        self.centerContLayout.addWidget(self.rightcenterCont)


        self.bottomContLayout.addWidget(self.centerCont)

        self.extCont = QFrame(self.bottomCont)
        self.extCont.setObjectName(u"extCont")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.extCont.sizePolicy().hasHeightForWidth())
        self.extCont.setSizePolicy(sizePolicy1)
        self.extCont.setMinimumSize(QtCore.QSize(0, 0))
        self.extCont.setMaximumSize(QtCore.QSize(16777215, 40))
        self.extContLayout = QHBoxLayout(self.extCont)
        self.extContLayout.setObjectName(u"extContLayout")
        self.extContLayout.setContentsMargins(9, 9, 9, 9)
        self.labelExt = QLabel(self.extCont)
        self.labelExt.setObjectName(u"labelExt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelExt.sizePolicy().hasHeightForWidth())
        self.labelExt.setSizePolicy(sizePolicy2)

        self.extContLayout.addWidget(self.labelExt)

        self.lineEditExt = QLineEdit(self.extCont)
        self.lineEditExt.setObjectName(u"lineEditExt")
        self.lineEditExt.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEditExt.setMaximumSize(QtCore.QSize(100, 16777215))

        self.extContLayout.addWidget(self.lineEditExt)

        self.bottomContLayout.addWidget(self.extCont)

        self.buttonsEnd = QFrame(self.bottomCont)
        self.buttonsEnd.setObjectName(u"buttonsEnd")
        self.buttonsEndlLayout = QVBoxLayout(self.buttonsEnd)
        self.buttonsEndlLayout.setObjectName(u"buttonsEndlLayout")
        self.buttonsEnd2 = QFrame(self.buttonsEnd)
        self.buttonsEnd2.setObjectName(u"buttonsEnd2")
        self.buttonsEnd2Layout = QHBoxLayout(self.buttonsEnd2)
        self.buttonsEnd2Layout.setObjectName(u"buttonsEnd2Layout")
        self.buttonAgregar = QPushButton(self.buttonsEnd2)
        self.buttonAgregar.setObjectName(u"buttonAgregar")
        self.buttonAgregar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonAgregar.setMaximumSize(QtCore.QSize(125, 50))
        self.msg = QMessageBox(self.buttonsEnd2)
        self.buttonAgregar.clicked.connect(lambda: self.agregarUser())

        self.buttonsEnd2Layout.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsEnd2)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QtCore.QSize(125, 50))
        self.buttonCerrar.clicked.connect(lambda: self.close())

        self.buttonsEnd2Layout.addWidget(self.buttonCerrar)


        self.buttonsEndlLayout.addWidget(self.buttonsEnd2)


        self.bottomContLayout.addWidget(self.buttonsEnd)

        self.labelBy = QLabel(self.bottomCont)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMinimumSize(QtCore.QSize(0, 20))
        self.labelBy.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelBy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.bottomContLayout.addWidget(self.labelBy)


        self.contUsersLayout.addWidget(self.bottomCont)


        self.stylesLayout.addWidget(self.contUsers)

        self.setTextCont()
        
        self.setCentralWidget(self.styles)

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

    def agregarUser(self):
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
            self.msg.setText("Usuario agregado con exito")
        else:
            self.msg.setWindowTitle("AGREGAR")
            self.msg.setText(f"El usuario con este numero de cedula {self.lineEditCedula.text()} ya existe")
       
        resp = self.msg.exec_()
        if resp == QMessageBox.Ok:
            self.close()
        
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = UsersApp()
    window.show()
    app.exec_()