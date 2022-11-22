# Importando la clase Productos del archivo Productos.py
from Controlador.Productos import *


# Crea una clase llamada ArregloProductos.
class ArregloProductos():

    def __init__(self):
        """
        Crea una lista llamada dataProductos.
        """
        self.dataProductos = []

    def adicionaProducto(self, objPro):
        """
        Añade un producto a la lista de productos.

        :param objPro: es un objeto de la clase Producto
        """
        self.dataProductos.append(objPro)

    def devolverProducto(self, pos):
        """
        Devuelve el producto en la posición especificada por el parámetro

        :param pos: posición del producto en la lista
        :return: El producto en la posición pos.
        """
        return self.dataProductos[pos]

    def tamañoArregloProductos(self):
        """
        Devuelve la longitud del arreglo dataProductos
        :return: La longitud de la matriz
        """
        return len(self.dataProductos)

    def buscarProducto(self, codigo):
        """
        Busca un producto en la matriz de productos.

        :param codigo: es el codigo del producto
        :return: El índice del producto en la matriz.
        """
        for i in range(self.tamañoArregloProductos()):
            if codigo == self.dataProductos[i].getCodigo():
                return i
        return -1

    def eliminarProducto(self, indice):
        """
        Elimina el producto en el índice dado de la lista de productos

        :param indice: El índice del producto a eliminar
        """
        del (self.dataProductos[indice])
