# Importación de los módulos QtWidgets y uic del paquete PyQt5.
from PyQt5 import QtWidgets, uic
from Vista.VentanaProductos import *

# Carga el archivo UI.
class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("ProyectoPuntoDeVenta/UI/VentanaPrincipal.ui", self)

        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnSalir.clicked.connect(self.Salir)

    def abrirVentanaProductos(self):
        self.close()
        vProductos = VentanaProductos(self)
        vProductos.show()

    def Salir(self):
        self.close()
