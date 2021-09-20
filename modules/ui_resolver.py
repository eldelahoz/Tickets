from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# Package external
from . css.stylescss import stylesincss
from . functions import showTickets, searchTicket

class Ui_Resolver(QMainWindow):
    def __init__(self, parent=None, *args):
        super(Ui_Resolver, self).__init__(parent=parent)
        self.resize(800, 496)
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(stylesincss())
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        self.contenidoBox = QFrame(self.styles)
        self.contenidoBox.setObjectName(u"contenidoBox")
        self.contenidoBoxLayout = QVBoxLayout(self.contenidoBox)
        self.contenidoBoxLayout.setObjectName(u"contenidoBoxLayout")
        self.topCont = QFrame(self.contenidoBox)
        self.topCont.setObjectName(u"topCont")
        self.topCont.setMinimumSize(QSize(0, 55))
        self.topCont.setMaximumSize(QSize(16777215, 55))
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
        self.label = QLabel(self.leftTitle)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.leftTitleLayout.addWidget(self.label)

        self.arrowLeft = QPushButton(self.leftTitle)
        self.arrowLeft.setObjectName(u"arrowLeft")
        self.arrowLeft.setMinimumSize(QSize(0, 25))
        self.arrowLeft.setMaximumSize(QSize(25, 16777215))
        icon = QIcon()
        icon.addFile(u"images/icons/up-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrowLeft.setIcon(icon)

        self.leftTitleLayout.addWidget(self.arrowLeft)

        self.arrowRight = QPushButton(self.leftTitle)
        self.arrowRight.setObjectName(u"arrowRight")
        self.arrowRight.setMinimumSize(QSize(0, 25))
        self.arrowRight.setMaximumSize(QSize(25, 16777215))
        self.arrowRight.setIcon(icon)

        self.leftTitleLayout.addWidget(self.arrowRight)


        self.topContLayout.addWidget(self.leftTitle)

        self.buttonRight = QFrame(self.topCont)
        self.buttonRight.setObjectName(u"buttonRight")
        self.buttonRight.setMinimumSize(QSize(0, 28))
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
        self.minimizarBtn.setMinimumSize(QSize(28, 28))
        self.minimizarBtn.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizarBtn.setIcon(icon1)
        self.minimizarBtn.setIconSize(QSize(20, 16))

        self.buttonRightLayout.addWidget(self.minimizarBtn)

        self.maximizarBtn = QPushButton(self.buttonRight)
        self.maximizarBtn.setObjectName(u"maximizarBtn")
        self.maximizarBtn.setMinimumSize(QSize(28, 28))
        self.maximizarBtn.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizarBtn.setIcon(icon2)
        self.maximizarBtn.setIconSize(QSize(20, 20))

        self.buttonRightLayout.addWidget(self.maximizarBtn)

        self.cerrarBtn = QPushButton(self.buttonRight)
        self.cerrarBtn.setObjectName(u"cerrarBtn")
        self.cerrarBtn.setMinimumSize(QSize(28, 28))
        self.cerrarBtn.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u"images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarBtn.setIcon(icon3)
        self.cerrarBtn.setIconSize(QSize(20, 20))

        self.buttonRightLayout.addWidget(self.cerrarBtn)


        self.topContLayout.addWidget(self.buttonRight)


        self.contenidoBoxLayout.addWidget(self.topCont)

        self.bottomCont = QFrame(self.contenidoBox)
        self.bottomCont.setObjectName(u"bottomCont")
        self.bottomCont.setMinimumSize(QSize(0, 50))
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
        self.textEdit.setMaximumSize(QSize(16777215, 200))
        self.textEdit.setTabChangesFocus(True)

        self.bottomContLayout.addWidget(self.textEdit)

        self.buttonsEnd = QFrame(self.bottomCont)
        self.buttonsEnd.setObjectName(u"buttonsEnd")
        self.buttonsEnd.setMinimumSize(QSize(0, 80))
        self.buttonsEnd.setMaximumSize(QSize(16777215, 80))
        self.buttonsEnd.setLayoutDirection(Qt.LeftToRight)
        self.buttonsEndLayout = QVBoxLayout(self.buttonsEnd)
        self.buttonsEndLayout.setObjectName(u"buttonsEndLayout")
        self.buttonsEnd2 = QFrame(self.buttonsEnd)
        self.buttonsEnd2.setObjectName(u"buttonsEnd2")
        self.buttonsEnd2Layout = QHBoxLayout(self.buttonsEnd2)
        self.buttonsEnd2Layout.setObjectName(u"buttonsEnd2Layout")
        self.buttonAgregar = QPushButton(self.buttonsEnd2)
        self.buttonAgregar.setObjectName(u"buttonAgregar")
        self.buttonAgregar.setMinimumSize(QSize(0, 50))
        self.buttonAgregar.setMaximumSize(QSize(125, 50))

        self.buttonsEnd2Layout.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsEnd2)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QSize(125, 50))
        self.buttonCerrar.setLayoutDirection(Qt.LeftToRight)

        self.buttonsEnd2Layout.addWidget(self.buttonCerrar)


        self.buttonsEndLayout.addWidget(self.buttonsEnd2)


        self.bottomContLayout.addWidget(self.buttonsEnd)

        self.horizontalFrame = QFrame(self.bottomCont)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelBy = QLabel(self.horizontalFrame)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMaximumSize(QSize(16777215, 16777215))
        self.labelBy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelBy)

        self.verticalFrame = QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(20, 0))
        self.verticalFrame.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout.addWidget(self.verticalFrame)


        self.bottomContLayout.addWidget(self.horizontalFrame)


        self.contenidoBoxLayout.addWidget(self.bottomCont)


        self.stylesLayout.addWidget(self.contenidoBox)

        self.setCentralWidget(self.styles)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.arrowLeft.setText("")
        self.arrowRight.setText("")
        self.minimizarBtn.setText("")
        self.maximizarBtn.setText("")
        self.cerrarBtn.setText("")
        self.labelDescripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.labelPrioridad.setText(QCoreApplication.translate("MainWindow", u"Prioridad", None))
        self.labelInformado.setText(QCoreApplication.translate("MainWindow", u"Informado", None))
        self.buttonAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buttonCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.labelBy.setText(QCoreApplication.translate("MainWindow", u"By:DelaHoz", None))
    # retranslateUi


    def show(self) -> None:
        self.ticketActual()
        return super().show()
    
    def setTextResolver(self):
        self.labelBy.setText("By: De la Hoz")
        self.buttonAgregar.setText("Agregar")
        self.buttonCerrar.setText("Cerrar")
        
    def ticketActual(self):
        NoTick = showTickets()
        msg = QMessageBox(self.styles)
        msg.setObjectName(u"msg")
        PrioColor = {
            'Baja': "<span style='color:green'> Baja </span>",
            'Media': "<span style='color:orange'> Media </span>",
            'Alta': "<span style='color:red'> Alta </span>"
        }
        if NoTick is None:
            msg.setText("No hay tickets")
            msg.exec_()
            self.label.setText("No hay ticket")
            self.labelDescripcion.setText("Descripcion: N/A")
            self.labelPrioridad.setText("Prioridad: N/A")
            self.labelInformado.setText("Informado: N/A")
        else:
            self.label.setText(f"TICKET# {showTickets()}")
            self.labelDescripcion.setText(f"Descripcion: <p style='color:red'>{searchTicket(showTickets())[3]}</p>")
            try:
                self.labelPrioridad.setText(f"Prioridad: {PrioColor[searchTicket(showTickets())[2]]}")
            except:
                self.labelPrioridad.setText("Prioridad: N/A")
            
            self.labelInformado.setText(f"Informado: {searchTicket(NoTick)[5]}")
        
        

    # def agregarResolver(self):
    #     msg = QMessageBox(self.styles)
    #     msg.setObjectName(u"msg")
    #     ticket = functions.showTickets()
    #     if ticket is not None:
    #         a = functions.cerrarTicket(functions.showTickets(), self.textEdit.toPlainText(), functions.showDateNow())
    #         if a is None:
    #             msg.setText(f"El Ticket # {ticket} fue cerrado")
    #             self.ticketActual()
    #             self.textEdit.clear()
    #             self.textEdit.setFocus()
    #     else:
    #         msg.setText(f"No se pudo cerrar el ticket")
    #     msg.exec_()

    def mousePressEvent(self, a0: QMouseEvent):
        self.clickPos = a0.globalPos()
        
