# Importación de los módulos necesarios para la ejecución del programa.
import sys
from PyQt5 import QtWidgets, uic
# Importación de la clase de inicio de sesión desde el archivo Login.py.
from Vista.Login import *

# La función principal.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Creando una instancia de la clase Login.
    window = Login()
    app.exec()
