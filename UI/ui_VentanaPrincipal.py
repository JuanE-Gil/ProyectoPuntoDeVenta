# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\IDAT\Ciclo - II\Estructura de Datos y POO\EDDPOO\ProyectoPuntoDeVenta\UI\VentanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 481)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 211, 481))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(242, 5, 5);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(5, 108, 242);\n"
"font: 10pt \"Comic Sans MS\";\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(5, 242, 242);\n"
"font: 10pt \"Comic Sans MS\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-30, 0, 261, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/logo2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnVender = QtWidgets.QPushButton(self.frame)
        self.btnVender.setGeometry(QtCore.QRect(10, 158, 191, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVender.setIcon(icon)
        self.btnVender.setIconSize(QtCore.QSize(20, 20))
        self.btnVender.setCheckable(False)
        self.btnVender.setObjectName("btnVender")
        self.btnProductos = QtWidgets.QPushButton(self.frame)
        self.btnProductos.setGeometry(QtCore.QRect(10, 198, 191, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/caja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProductos.setIcon(icon1)
        self.btnProductos.setIconSize(QtCore.QSize(26, 26))
        self.btnProductos.setObjectName("btnProductos")
        self.btnClientes = QtWidgets.QPushButton(self.frame)
        self.btnClientes.setGeometry(QtCore.QRect(10, 237, 191, 31))
        self.btnClientes.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClientes.setIcon(icon2)
        self.btnClientes.setIconSize(QtCore.QSize(20, 20))
        self.btnClientes.setObjectName("btnClientes")
        self.btnAlmacenes = QtWidgets.QPushButton(self.frame)
        self.btnAlmacenes.setGeometry(QtCore.QRect(10, 277, 191, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/cajas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlmacenes.setIcon(icon3)
        self.btnAlmacenes.setIconSize(QtCore.QSize(24, 24))
        self.btnAlmacenes.setObjectName("btnAlmacenes")
        self.btnProveedores = QtWidgets.QPushButton(self.frame)
        self.btnProveedores.setGeometry(QtCore.QRect(10, 316, 191, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/terreno.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProveedores.setIcon(icon4)
        self.btnProveedores.setIconSize(QtCore.QSize(24, 24))
        self.btnProveedores.setObjectName("btnProveedores")
        self.btnSalidas = QtWidgets.QPushButton(self.frame)
        self.btnSalidas.setGeometry(QtCore.QRect(10, 356, 191, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/carro-de-entrega.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalidas.setIcon(icon5)
        self.btnSalidas.setIconSize(QtCore.QSize(32, 32))
        self.btnSalidas.setObjectName("btnSalidas")
        self.btnVentas = QtWidgets.QPushButton(self.frame)
        self.btnVentas.setGeometry(QtCore.QRect(10, 395, 191, 31))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/ingresos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVentas.setIcon(icon6)
        self.btnVentas.setIconSize(QtCore.QSize(26, 26))
        self.btnVentas.setObjectName("btnVentas")
        self.btnDetalleVentas = QtWidgets.QPushButton(self.frame)
        self.btnDetalleVentas.setGeometry(QtCore.QRect(10, 435, 191, 31))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/lista-de-deseos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDetalleVentas.setIcon(icon7)
        self.btnDetalleVentas.setIconSize(QtCore.QSize(24, 24))
        self.btnDetalleVentas.setObjectName("btnDetalleVentas")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 0, 561, 61))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(166, 38, 121);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(5, 242, 242);\n"
"font: 10pt \"Comic Sans MS\";\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnSalir = QtWidgets.QPushButton(self.frame_2)
        self.btnSalir.setGeometry(QtCore.QRect(460, 20, 75, 23))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon8)
        self.btnSalir.setIconSize(QtCore.QSize(24, 24))
        self.btnSalir.setObjectName("btnSalir")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnVender.setText(_translate("MainWindow", "VENDER"))
        self.btnProductos.setText(_translate("MainWindow", "PRODUCTOS"))
        self.btnClientes.setText(_translate("MainWindow", "CLIENTES"))
        self.btnAlmacenes.setText(_translate("MainWindow", "ALMACENES"))
        self.btnProveedores.setText(_translate("MainWindow", "PROVEEDORES"))
        self.btnSalidas.setText(_translate("MainWindow", "SALIDAS"))
        self.btnVentas.setText(_translate("MainWindow", "VENTAS"))
        self.btnDetalleVentas.setText(_translate("MainWindow", "DETALLE VENTAS"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
