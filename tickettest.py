from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from css import stylescss

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent=parent)
        self.resize(796, 553)
        self.setMinimumSize(785, 475)
        self.styles = QWidget(self)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(stylescss.stylesincss())
        self.stylesLayout = QVBoxLayout(self.styles)
        self.stylesLayout.setObjectName(u"stylesLayout")
        self.contenidoBox = QFrame(self.styles)
        self.contenidoBox.setObjectName(u"contenidoBox")
        self.contenidoBoxLayout = QVBoxLayout(self.contenidoBox)
        self.contenidoBoxLayout.setObjectName(u"contenidoBoxLayout")
        self.topCont = QFrame(self.contenidoBox)
        self.topCont.setObjectName(u"topCont")
        self.topCont.setMinimumSize(QSize(0, 50))
        self.topCont.setMaximumSize(QSize(16777215, 50))
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
        icon = QIcon()
        icon.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizarBtn.setIcon(icon)
        self.minimizarBtn.setIconSize(QSize(20, 16))

        self.buttonRightLayout.addWidget(self.minimizarBtn)

        self.maximizarBtn = QPushButton(self.buttonRight)
        self.maximizarBtn.setObjectName(u"maximizarBtn")
        self.maximizarBtn.setMinimumSize(QSize(28, 28))
        self.maximizarBtn.setMaximumSize(QSize(28, 28))
        self.maximizarBtn.clicked.connect(lambda: self.showMaximized())
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


        self.contenidoBoxLayout.addWidget(self.topCont)

        self.bottomCont = QFrame(self.contenidoBox)
        self.bottomCont.setObjectName(u"bottomCont")
        self.bottomCont.setMinimumSize(QSize(0, 50))
        self.bottomContLayout = QVBoxLayout(self.bottomCont)
        self.bottomContLayout.setObjectName(u"bottomContLayout")
        self.labelDescripcion = QLabel(self.bottomCont)
        self.labelDescripcion.setObjectName(u"labelDescripcion")

        self.bottomContLayout.addWidget(self.labelDescripcion)

        self.textDescripcion = QTextEdit(self.bottomCont)
        self.textDescripcion.setObjectName(u"textDescripcion")

        self.bottomContLayout.addWidget(self.textDescripcion)

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

        self.prioridadBox = QComboBox(self.leftmediumCont)
        self.prioridadBox.addItem("")
        self.prioridadBox.addItem("")
        self.prioridadBox.addItem("")
        self.prioridadBox.setObjectName(u"prioridadBox")

        self.leftmediumContLayout.addWidget(self.prioridadBox)


        self.mediumContLayout.addWidget(self.leftmediumCont)

        self.rightmediumCont = QFrame(self.mediumCont)
        self.rightmediumCont.setObjectName(u"rightmediumCont")
        self.rightmediumContLayout = QVBoxLayout(self.rightmediumCont)
        self.rightmediumContLayout.setObjectName(u"rightmediumContLayout")
        self.labelInformado = QLabel(self.rightmediumCont)
        self.labelInformado.setObjectName(u"labelInformado")

        self.rightmediumContLayout.addWidget(self.labelInformado)

        self.usuariosBox = QComboBox(self.rightmediumCont)
        self.usuariosBox.addItem("")
        self.usuariosBox.addItem("")
        self.usuariosBox.setObjectName(u"usuariosBox")

        self.rightmediumContLayout.addWidget(self.usuariosBox)


        self.mediumContLayout.addWidget(self.rightmediumCont)


        self.bottomContLayout.addWidget(self.mediumCont)

        self.buttonsEnd = QFrame(self.bottomCont)
        self.buttonsEnd.setObjectName(u"buttonsEnd")
        self.buttonsEnd.setMinimumSize(QSize(0, 80))
        self.buttonsEnd.setMaximumSize(QSize(16777215, 80))
        self.buttonsEnd.setLayoutDirection(Qt.LeftToRight)
        self.buttonsEndLayout = QVBoxLayout(self.buttonsEnd)
        self.buttonsEndLayout.setObjectName(u"buttonsEndLayout")
        self.buttonsEnd2 = QFrame(self.buttonsEnd)
        self.buttonsEnd2.setObjectName(u"buttonsEnd2")
        self.buttonsEndLayout_2 = QHBoxLayout(self.buttonsEnd2)
        self.buttonsEndLayout_2.setObjectName(u"buttonsEndLayout_2")
        self.buttonAgregar = QPushButton(self.buttonsEnd2)
        self.buttonAgregar.setObjectName(u"buttonAgregar")
        self.buttonAgregar.setMinimumSize(QSize(0, 50))
        self.buttonAgregar.setMaximumSize(QSize(125, 50))

        self.buttonsEndLayout_2.addWidget(self.buttonAgregar)

        self.buttonCerrar = QPushButton(self.buttonsEnd2)
        self.buttonCerrar.setObjectName(u"buttonCerrar")
        self.buttonCerrar.setMinimumSize(QSize(0, 50))
        self.buttonCerrar.setMaximumSize(QSize(125, 50))
        self.buttonCerrar.setLayoutDirection(Qt.LeftToRight)

        self.buttonsEndLayout_2.addWidget(self.buttonCerrar)


        self.buttonsEndLayout.addWidget(self.buttonsEnd2)


        self.bottomContLayout.addWidget(self.buttonsEnd)

        

        self.verticalFrame = QFrame(self.bottomCont)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.horizontalLayout = QHBoxLayout(self.verticalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelBy = QLabel(self.verticalFrame)
        self.labelBy.setObjectName(u"labelBy")
        self.labelBy.setMaximumSize(QSize(16777215, 16777215))
        self.labelBy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelBy)

        self.verticalFrame1 = QFrame(self.verticalFrame)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setMinimumSize(QSize(20, 0))
        self.verticalFrame1.setMaximumSize(QSize(20, 16777215))

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self.verticalFrame1)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)


        self.horizontalLayout.addWidget(self.verticalFrame1)


        self.bottomContLayout.addWidget(self.verticalFrame)


        self.contenidoBoxLayout.addWidget(self.bottomCont)


        self.stylesLayout.addWidget(self.contenidoBox)

        self.setCentralWidget(self.styles)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.minimizarBtn.setText("")
        self.maximizarBtn.setText("")
        self.cerrarBtn.setText("")
        self.labelDescripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.labelPrioridad.setText(QCoreApplication.translate("MainWindow", u"Prioridad", None))
        self.prioridadBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Baja", None))
        self.prioridadBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.prioridadBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Alta", None))

        self.labelInformado.setText(QCoreApplication.translate("MainWindow", u"Informado", None))
        self.usuariosBox.setItemText(0, QCoreApplication.translate("MainWindow", u"fadfadfa", None))
        self.usuariosBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ANDRES", None))

        self.buttonAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buttonCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.labelBy.setText(QCoreApplication.translate("MainWindow", u"By:DelaHoz", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()