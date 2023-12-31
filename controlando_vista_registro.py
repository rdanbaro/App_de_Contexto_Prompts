from ui_vista_registro import Ui_VistaRegistro
from PySide6.QtWidgets import QWidget, QMessageBox
import database
from modelos import Usuario


class ControladoraRegistro(QWidget, Ui_VistaRegistro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



    def register_validator(self):
        usuario = self.entrada_usuario_registro.text()
        contrasena = self.entrada_contrasena_registro.text()
        confirmar_contrasena = self.entrada_confirmar_contrasena.text()
        buscando_existencia_usuario = database.sesion.query(Usuario).filter(
            Usuario.nombre_usuario == usuario).first()
        cuenta_valida = True
        try:
            if buscando_existencia_usuario != None:
                print("Ese nombre de usuario ya existe!")
                cuenta_valida = False
            if contrasena == "":
                print("contrasena no valida")
                cuenta_valida = False
            if contrasena != confirmar_contrasena:
                cuenta_valida = False
                print("Verifique que la confirmacion de la contrasena sea correcta")
            if cuenta_valida:
                database.sesion.add(Usuario(nombre_usuario=usuario, contrasena=contrasena, sesion_iniciada=False))
                database.sesion.commit()

        except Exception as e:
            print(f"Algun error ha ocurrido, verifique que los campos sean validos: {e}")

        return cuenta_valida

