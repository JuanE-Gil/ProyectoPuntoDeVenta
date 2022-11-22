class Producto():
    def __init__(self, codigo, nombre, descripcion, stockMinimo, stockActual, precioCosto, precioVenta, proveedor, almacen):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__stockMinimo = stockMinimo
        self.__stockActual = stockActual
        self.__precioCosto = precioCosto
        self.__precioVenta = precioVenta
        self.__proveedor = proveedor
        self.__almacen = almacen

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    def getStockMinimo(self):
        return self.__stockMinimo

    def getStockActual(self):
        return self.__stockActual

    def getPrecioCosto(self):
        return self.__precioCosto

    def getPrecioVenta(self):
        return self.__precioVenta

    def getProveedor(self):
        return self.__proveedor

    def getAlmacen(self):
        return self.__almacen
