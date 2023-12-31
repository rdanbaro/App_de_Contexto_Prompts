from PySide6.QtWidgets import QWidget, QLineEdit

import database
from modelos import Usuario
from ui_vista_login import Ui_VentanaPrincipal


class ControladoraLogin(QWidget, Ui_VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.contrasena_entrada.setEchoMode(QLineEdit.Password)

    def login_validator(self):
        usuario = self.usuario_entrada.text()
        contrasena = self.contrasena_entrada.text()

        try:

            user = database.sesion.query(Usuario).filter(Usuario.nombre_usuario == usuario).first()
            if user is not None and user.contrasena == contrasena:
                print("Estoy dentro cobio")

                user.sesion_iniciada = True
                database.sesion.add(user)
                database.sesion.commit()
                return True
            else:
                print("No pude entrar")
                self.contrasena_entrada.setText("")
                print(self.vista_login.contrasena_entrada.text())
                return False
        except Exception as e:
            print(f"Ocurrió un error al intentar iniciar sesión: {e}")
            return False


