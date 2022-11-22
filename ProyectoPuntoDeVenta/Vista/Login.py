# Importando el archivo ui y la clase VentanaPrincipal.
from PyQt5 import QtWidgets, uic
from Vista.VentanaPrincipal import *

# Cargando el archivo ui y creando una clase a partir de él.
qtCreatorFile = "ProyectoPuntoDeVenta/UI/Login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


# Carga el archivo Login.ui y conecta el botón a la función iniciarSesion.
class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        uic.loadUi("ProyectoPuntoDeVenta/UI/Login.ui", self)

# Conectando el botón a la función iniciarSesion.
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    def iniciarSesion(self):
        """
        Si el usuario ingresa "Admin" y "123456" en los cuadros de texto, la ventana de inicio de sesión se
        cierra y se abre la ventana principal.
        """
        usuario = self.txtUsuario.text().capitalize()
        contraseña = self.txtPassword.text()
        if usuario == "Admin" and contraseña == "123456":
            self.close()
            vPrincipal = VentanaPrincipal(self)
            vPrincipal.show()
        else:
            """
            Este bloque muestra un cuadro de texto en caso 
            que el usuario y la password sean incorrectas
            """
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Los datos Ingresados son incorrectos!!!")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)
            x = mensaje.exec_()
