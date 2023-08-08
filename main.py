import sys
from PySide6.QtWidgets import QApplication
import database
from controladora import Controladora
from modelos import *

if __name__ == "__main__":
    #Base.metadata.drop_all(database.link)
    try:
        Base.metadata.create_all(database.link)

    except Exception as e:
        print("seguimos adelante")

hola = QApplication(sys.argv)

qwuelta = Controladora()

hola.exec()

usuario = database.sesion.query(Usuario).filter(Usuario.sesion_iniciada == True).first()
usuario.sesion_iniciada = False  # Cambiar a tu nuevo valor

database.sesion.commit()
