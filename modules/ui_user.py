from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# Package external
from . css.stylescss import stylesincss

class Ui_User(QMainWindow):
    def __init__(self, parent=None, *args):
        super(Ui_User, self).__init__(parent=parent)
        self.resize(773, 554)
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(stylesincss())
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        self.contUsers = QWidget(self.styles)
        self.contUsers.setObjectName(u"contUsers")
        self.contUsersLayout = QVBoxLayout(self.contUsers)
        self.contUsersLayout.setObjectName(u"contUsersLayout")
        self.topCont = QWidget(self.contUsers)
        self.topCont.setObjectName(u"topCont")
        self.topCont.setMinimumSize(QSize(0, 50))
        self.topCont.setMaximumSize(QSize(16777215, 50))
        self.topContLayout = QHBoxLayout(self.topCont)
        self.topContLayout.setObjectName(u"topContLayout")
        self.topContLayout.setContentsMargins(-1, 5, -1, -1)
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
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.leftTitleLayout.addWidget(self.labelTitle)

        self.buttonAddUsers = QPushButton(self.leftTitle)
        self.buttonAddUsers.setObjectName(u"buttonAddUsers")
        self.buttonAddUsers.setMinimumSize(QSize(0, 23))
        self.buttonAddUsers.setMaximumSize(QSize(100, 23))

        self.leftTitleLayout.addWidget(self.buttonAddUsers)

        self.buttonEditUsers = QPushButton(self.leftTitle)
        self.buttonEditUsers.setObjectName(u"buttonEditUsers")
        self.buttonEditUsers.setMinimumSize(QSize(0, 23))
        self.buttonEditUsers.setMaximumSize(QSize(100, 23))

        self.leftTitleLayout.addWidget(self.buttonEditUsers)


        self.topContLayout.addWidget(self.leftTitle)

        self.buttonRight = QWidget(self.topCont)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setMinimumSize(QSize(0, 28))
        self.buttonRightLayout = QHBoxLayout(self.buttonRight)
        self.buttonRightLayout.setObjectName(u"buttonRightLayout")
        self.buttonRightLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizarBtn = QPushButton(self.buttonRight)
        self.minimizarBtn.setObjectName(u"minimizarBtn")
        self.minimizarBtn.setMinimumSize(QSize(28, 28))
        self.minimizarBtn.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizarBtn.setIcon(icon)
        self.minimizarBtn.setIconSize(QSize(20, 20))

        self.buttonRightLayout.addWidget(self.minimizarBtn)

        self.maximizarBtn = QPushButton(self.buttonRight)
        self.maximizarBtn.setObjectName(u"maximizarBtn")
        self.maximizarBtn.setMinimumSize(QSize(28, 28))
        self.maximizarBtn.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizarBtn.setIcon(icon1)
        self.maximizarBtn.setIconSize(QSize(20, 20))

        self.buttonRightLayout.addWidget(self.maximizarBtn)

        self.cerrarBtn = QPushButton(self.buttonRight)
        self.cerrarBtn.setObjectName(u"cerrarBtn")
        self.cerrarBtn.setMinimumSize(QSize(28, 28))
        self.cerrarBtn.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u"images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarBtn.setIcon(icon2)
        self.cerrarBtn.setIconSize(QSize(20, 20))

        self.buttonRightLayout.addWidget(self.cerrarBtn)


        self.topContLayout.addWidget(self.buttonRight)


        self.contUsersLayout.addWidget(self.topCont)

        self.bottomContUsers = QWidget(self.contUsers)
        self.bottomContUsers.setObjectName(u"bottomContUsers")
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
        self.lineEditCedula.setStyleSheet(u"")

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
        self.buttonAgregar.setMinimumSize(QSize(0, 50))
        self.buttonAgregar.setMaximumSize(QSize(125, 50))

        self.buttonsUsersLayout.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsUsers)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QSize(125, 50))

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
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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
        self.buttonEditar.setMinimumSize(QSize(0, 50))
        self.buttonEditar.setMaximumSize(QSize(125, 50))

        self.row_3Layout.addWidget(self.buttonEditar)

        self.buttonEliminar = QPushButton(self.row_3)
        self.buttonEliminar.setObjectName(u"buttonEliminar")
        self.buttonEliminar.setMinimumSize(QSize(0, 50))
        self.buttonEliminar.setMaximumSize(QSize(125, 50))

        self.row_3Layout.addWidget(self.buttonEliminar)


        self.verticalLayout.addWidget(self.row_3)

        self.centerContPage.addWidget(self.page_2)

        self.bottomContLayout.addWidget(self.centerContPage)

        self.buttonsEnd = QFrame(self.bottomContUsers)
        self.buttonsEnd.setObjectName(u"buttonsEnd")
        self.buttonsEndlLayout = QVBoxLayout(self.buttonsEnd)
        self.buttonsEndlLayout.setObjectName(u"buttonsEndlLayout")

        self.bottomContLayout.addWidget(self.buttonsEnd)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelBy = QLabel(self.bottomContUsers)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMinimumSize(QSize(0, 20))
        self.labelBy.setMaximumSize(QSize(16777215, 20))
        self.labelBy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelBy)

        self.verticalFrame = QFrame(self.bottomContUsers)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(20, 50))

        self.horizontalLayout.addWidget(self.verticalFrame)


        self.bottomContLayout.addLayout(self.horizontalLayout)


        self.contUsersLayout.addWidget(self.bottomContUsers)


        self.stylesLayout.addWidget(self.contUsers)

        self.setCentralWidget(self.styles)

        self.retranslateUi(self)

        self.centerContPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">USERS PANEL</span></p></body></html>", None))
        self.buttonAddUsers.setText(QCoreApplication.translate("MainWindow", u"Add Users", None))
        self.buttonEditUsers.setText(QCoreApplication.translate("MainWindow", u"View Users", None))
        self.minimizarBtn.setText("")
        self.maximizarBtn.setText("")
        self.cerrarBtn.setText("")
        self.labelCedula.setText(QCoreApplication.translate("MainWindow", u"Cedula", None))
        self.labelNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.labelUsuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.labelEquipo.setText(QCoreApplication.translate("MainWindow", u"Equipo", None))
        self.labelExt.setText(QCoreApplication.translate("MainWindow", u"Ext", None))
        self.buttonAgregar.setText(QCoreApplication.translate("MainWindow", u"AGREGAR", None))
        self.buttonCerrar.setText(QCoreApplication.translate("MainWindow", u"CERRAR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cedula", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nueva columna", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Equipo", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ext", None));
        self.buttonEditar.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.buttonEliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.labelBy.setText(QCoreApplication.translate("MainWindow", u"By: De la Hoz", None))
    # retranslateUi




        # //////////////////////////////////
        self.msg = QMessageBox()
        grip = QSizeGrip(self.verticalFrame)


    def mousePressEvent(self, a0: QMouseEvent):
        self.clickPos = a0.globalPos()
