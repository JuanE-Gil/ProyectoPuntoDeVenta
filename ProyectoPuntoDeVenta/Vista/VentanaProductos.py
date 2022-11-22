# Importamos los modulos requeridos.
from PyQt5 import QtWidgets, uic
from Controlador.ArregloProductos import *

aPro = ArregloProductos()

# Crea una clase llamada VentanaProductos.


class VentanaProductos(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        """
        Carga el archivo UI.

        :param parent: El widget principal
        """
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("ProyectoPuntoDeVenta/UI/VentanaProductos.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.listar()
        self.show()

    def obtenerCodigo(self):
        """
        Devuelve el texto en el cuadro de texto.
        :return: El texto en el cuadro de texto.
        """
        return self.txtCodigo.text()

    def obtenerNombre(self):
        return self.txtNombre.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerMinimo(self):
        return self.txtStockMinimo.text()

    def obtenerActual(self):
        return self.txtStockActual.text()

    def obtenerCosto(self):
        return self.txtPrecioCosto.text()

    def obtenerPrecio(self):
        return self.txtPrecioVenta.text()

    def obtenerProveedor(self):
        """
        Devuelve el texto actual del cuadro combinado.
        :return: El texto actual del cuadro combinado.
        """
        return self.cboProveedor.currentText()

    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() == None:
            self.txtCodigo.setFocus()
            return "Código del Producto!!!."

        elif self.txtNombre.text() == None:
            self.txtCodigo.setFocus()
            return "Nombre del Producto!!!."

        elif self.txtDescripcion.text() == None:
            self.txtDescripcion.setFocus()
            return "Descripcion del Producto!!!."

        elif self.txtStockMinimo.text() == None:
            self.txtStockMinimo.setFocus()
            return "Stock Minimo del Producto!!!."

        elif self.txtStockActual.text() == None:
            self.txtStockActual.setFocus()
            return "Stock Actual del Producto!!!."

        elif self.txtPrecioCosto.text() == None:
            self.txtPrecioCosto.setFocus()
            return "Precio Costo del Producto!!!."

        elif self.txtPrecioVenta.text() == None:
            self.txtPrecioVenta.setFocus()
            return "Precio Venta del Producto!!!."

        elif self.cboProveedor.currentText() == "Seleccionar Proveedor":
            self.cboProveedor.setCurrentIndex(0)
            return "Proveedor del Producto!!!."

        elif self.cboAlmacen.currentText() == "Seleccionar Almacén":
            self.cboAlmacen.setCurrentIndex(0)
            return "Almacen del Producto!!!."

        else:
            return None

    def listar(self):
        self.tblProductos.setRowCount(aPro.tamañoArregloProductos())
        self.tblProductos.setColumnCount(9)

        for i in range(aPro.tamañoArregloProductos()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getCodigo()))

            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getNombre()))

            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getDescripcion()))

            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getStockMinimo()))

            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getStockActual()))

            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getPrecioCosto()))

            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getPrecioVenta()))

            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getProveedor()))

            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(
                aPro.devolverProducto(i).getAlmacen()))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

    def registrar(self):
        if self.valida() == None:
            objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(), self.obtenerMinimo(
            ), self.obtenerActual(), self.obtenerCosto(), self.obtenerPrecio(), self.obtenerProveedor(), self.obtenerAlmacen())

            codigo = self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                self.limpiarControles()
                self.listar()

            else:
                QtWidgets.QMessageBox.information(
                    self, "Registrar Producto", "El código ingresado ya existe!!!.", QtWidgets.QMessageBox.Ok)

        else:   
            QtWidgets.QMessageBox.information(
                self, "Registrar Producto", f"Error en {self.valida()}", QtWidgets.QMessageBox.Ok)
