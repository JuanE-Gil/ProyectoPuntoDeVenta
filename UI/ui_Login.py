# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\IDAT\Ciclo - II\Estructura de Datos y POO\EDDPOO\ProyectoPuntoDeVenta\UI\Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 386)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 255, 127);\n"
"font: \"Comic Sans MS\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(54, 54, 54);\n"
"border-bottom: 2px solid rgb(216, 0, 216);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(54, 54, 54);\n"
"border-bottom: 2px solid rgb(245, 245, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(227, 0, 0);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(79, 196, 207);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 131, 131))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/hombre1.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 66, 26))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(40, 190, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setObjectName("txtUsuario")
        self.btnIniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIniciar.setGeometry(QtCore.QRect(50, 310, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.btnIniciar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Documents\\IDAT\\Ciclo - II\\Estructura de Datos y POO\\EDDPOO\\ProyectoPuntoDeVenta\\UI\\img/sign4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIniciar.setIcon(icon)
        self.btnIniciar.setIconSize(QtCore.QSize(32, 32))
        self.btnIniciar.setObjectName("btnIniciar")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(40, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtPassword.setFont(font)
        self.txtPassword.setAutoFillBackground(False)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setCursorPosition(0)
        self.txtPassword.setObjectName("txtPassword")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 97, 26))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.btnIniciar.setText(_translate("MainWindow", "INICIAR SESION"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))