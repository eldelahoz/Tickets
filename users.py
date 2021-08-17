from modules.bdsql import showCountUser, sql_table_show, tableUsersWrite
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
        # Ocultar los bordes de ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
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
        # Move Windows

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

        self.buttonAddUsers = QPushButton(self.leftTitle)
        self.buttonAddUsers.setObjectName(u"buttonAddUsers")
        self.buttonAddUsers.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonAddUsers.setMaximumSize(QtCore.QSize(100, 23))
        self.buttonAddUsers.clicked.connect(lambda: self.centerContPage.setCurrentWidget(self.page))

        self.leftTitleLayout.addWidget(self.buttonAddUsers)

        self.buttonEditUsers = QPushButton(self.leftTitle)
        self.buttonEditUsers.setObjectName(u"buttonEditUsers")
        self.buttonEditUsers.setMinimumSize(QtCore.QSize(0, 23))
        self.buttonEditUsers.setMaximumSize(QtCore.QSize(100, 23))
        self.buttonEditUsers.clicked.connect(lambda: self.centerContPage.setCurrentWidget(self.page_2))

        self.leftTitleLayout.addWidget(self.buttonEditUsers)


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
        icon2.addFile(u"images/icons/icon_close.png")
        self.cerrarBtn.setIcon(icon2)
        self.cerrarBtn.setIconSize(QtCore.QSize(20, 20))
        self.cerrarBtn.clicked.connect(lambda: self.close())

        self.buttonRightLayout.addWidget(self.cerrarBtn)


        self.topContLayout.addWidget(self.buttonRight)


        self.contUsersLayout.addWidget(self.topCont)

        self.bottomContUsers = QWidget(self.contUsers)
        self.bottomContUsers.setObjectName(u"bottomContUsers")
        self.bottomContUsers.setStyleSheet(u"")
        self.bottomContLayout = QVBoxLayout(self.bottomContUsers)
        self.bottomContLayout.setObjectName(u"bottomContLayout")
        self.centerContPage = QStackedWidget(self.bottomContUsers)
        self.centerContPage.setObjectName(u"centerContPage")
        self.centerContPage.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pageLayout = QVBoxLayout(self.page)
        self.pageLayout.setObjectName(u"pageLayout")
        self.row_1 = QFrame(self.page)
        self.row_1.setObjectName(u"row_1")
        self.row_1Layout = QVBoxLayout(self.row_1)
        self.row_1Layout.setSpacing(0)
        self.row_1Layout.setObjectName(u"row_1Layout")
        self.row_1Layout.setContentsMargins(0, 0, 0, 0)
        self.contInfoUsers = QFrame(self.row_1)
        self.contInfoUsers.setObjectName(u"contInfoUsers")
        self.contInfoUsersLayout = QVBoxLayout(self.contInfoUsers)
        self.contInfoUsersLayout.setObjectName(u"contInfoUsersLayout")
        self.labelCedula = QLabel(self.contInfoUsers)
        self.labelCedula.setObjectName(u"labelCedula")

        self.contInfoUsersLayout.addWidget(self.labelCedula)

        self.lineEditCedula = QLineEdit(self.contInfoUsers)
        self.lineEditCedula.setObjectName(u"lineEditCedula")
        self.lineEditCedula.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.contInfoUsersLayout.addWidget(self.lineEditCedula)

        self.labelNombre = QLabel(self.contInfoUsers)
        self.labelNombre.setObjectName(u"labelNombre")

        self.contInfoUsersLayout.addWidget(self.labelNombre)

        self.lineEditNombre = QLineEdit(self.contInfoUsers)
        self.lineEditNombre.setObjectName(u"lineEditNombre")

        self.contInfoUsersLayout.addWidget(self.lineEditNombre)

        self.labelUsuario = QLabel(self.contInfoUsers)
        self.labelUsuario.setObjectName(u"labelUsuario")

        self.contInfoUsersLayout.addWidget(self.labelUsuario)

        self.lineEditUsuario = QLineEdit(self.contInfoUsers)
        self.lineEditUsuario.setObjectName(u"lineEditUsuario")

        self.contInfoUsersLayout.addWidget(self.lineEditUsuario)

        self.labelEquipo = QLabel(self.contInfoUsers)
        self.labelEquipo.setObjectName(u"labelEquipo")

        self.contInfoUsersLayout.addWidget(self.labelEquipo)

        self.lineEditEquipo = QLineEdit(self.contInfoUsers)
        self.lineEditEquipo.setObjectName(u"lineEditEquipo")

        self.contInfoUsersLayout.addWidget(self.lineEditEquipo)

        self.labelExt = QLabel(self.contInfoUsers)
        self.labelExt.setObjectName(u"labelExt")

        self.contInfoUsersLayout.addWidget(self.labelExt)

        self.lineEditExt = QLineEdit(self.contInfoUsers)
        self.lineEditExt.setObjectName(u"lineEditExt")

        self.contInfoUsersLayout.addWidget(self.lineEditExt)


        self.row_1Layout.addWidget(self.contInfoUsers)


        self.pageLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.page)
        self.row_2.setObjectName(u"row_2")
        self.row_2Layout = QVBoxLayout(self.row_2)
        self.row_2Layout.setObjectName(u"row_2Layout")
        self.buttonsUsers = QFrame(self.row_2)
        self.buttonsUsers.setObjectName(u"buttonsUsers")
        self.buttonsUsersLayout = QHBoxLayout(self.buttonsUsers)
        self.buttonsUsersLayout.setObjectName(u"buttonsUsersLayout")
        self.buttonAgregar = QPushButton(self.buttonsUsers)
        self.buttonAgregar.setObjectName(u"buttonAgregar")
        self.buttonAgregar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonAgregar.setMaximumSize(QtCore.QSize(125, 50))
        self.buttonAgregar.clicked.connect(lambda: self.agregarUser())

        self.buttonsUsersLayout.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsUsers)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QtCore.QSize(125, 50))
        self.buttonCerrar.clicked.connect(lambda: self.close())
        self.buttonsUsersLayout.addWidget(self.buttonCerrar)


        self.row_2Layout.addWidget(self.buttonsUsers)


        self.pageLayout.addWidget(self.row_2)

        self.centerContPage.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row_4 = QFrame(self.page_2)
        self.row_4.setObjectName(u"row_4")
        self.row_4Layout = QVBoxLayout(self.row_4)
        self.row_4Layout.setObjectName(u"row_4Layout")
        self.tableWidget = QTableWidget(self.row_4)
        self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText("Cedula")
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText("Nombre")
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText("Usuario")
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setText("Equipo")
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setText("Ext")
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setRowCount(showCountUser())
        # Set item
        

        
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)

        self.row_4Layout.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_4)

        self.row_3 = QFrame(self.page_2)
        self.row_3.setObjectName(u"row_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.row_3.sizePolicy().hasHeightForWidth())
        self.row_3.setSizePolicy(sizePolicy1)
        self.row_3Layout = QHBoxLayout(self.row_3)
        self.row_3Layout.setObjectName(u"row_3Layout")
        self.buttonEditar = QPushButton(self.row_3)
        self.buttonEditar.setObjectName(u"buttonEditar")
        self.buttonEditar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonEditar.setMaximumSize(QtCore.QSize(125, 50))

        self.row_3Layout.addWidget(self.buttonEditar)

        self.buttonEliminar = QPushButton(self.row_3)
        self.buttonEliminar.setObjectName(u"buttonEliminar")
        self.buttonEliminar.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonEliminar.setMaximumSize(QtCore.QSize(125, 50))

        self.row_3Layout.addWidget(self.buttonEliminar)


        self.verticalLayout.addWidget(self.row_3)

        self.centerContPage.addWidget(self.page_2)

        self.bottomContLayout.addWidget(self.centerContPage)

        self.buttonsEnd = QFrame(self.bottomContUsers)
        self.buttonsEnd.setObjectName(u"buttonsEnd")
        self.buttonsEndlLayout = QVBoxLayout(self.buttonsEnd)
        self.buttonsEndlLayout.setObjectName(u"buttonsEndlLayout")

        self.bottomContLayout.addWidget(self.buttonsEnd)

        self.labelBy = QLabel(self.bottomContUsers)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMinimumSize(QtCore.QSize(0, 20))
        self.labelBy.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelBy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.bottomContLayout.addWidget(self.labelBy)


        self.contUsersLayout.addWidget(self.bottomContUsers)
        self.msg = QMessageBox(self.styles)
        self.insertItemsTable()
        self.stylesLayout.addWidget(self.contUsers)
        functions.setTextContUsers(self)
        self.setCentralWidget(self.styles)
        self.centerContPage.setCurrentIndex(0)

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
    
    def insertItemsTable(self):
        for i in range(showCountUser()):
            for j in range(5):
                self.tableWidget.setItem(i, j, QTableWidgetItem(sql_table_show("Users")[i][j]))
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = UsersApp()
    window.show()
    app.exec_()