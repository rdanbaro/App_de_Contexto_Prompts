from PySide6.QtWidgets import QWidget, QLineEdit

import database
from modelos import Usuario
from ui_vista_login import Ui_VentanaPrincipal


class ControladoraLogin(QWidget, Ui_VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(390, 360)
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

            elif usuario == '' or contrasena == '':
                print('Faltan campos por rellenar')
                self.label_error_visual.setText('                        Faltan campos por rellenar')
            else:
                print("Combinacion de usuario y contrasena incorrecta")
                self.label_error_visual.setText('Combinacion de usuario y contrasena incorrecta')
                self.contrasena_entrada.setText("")
                
                return False
        except Exception as e:
            print(f"Ocurrió un error al intentar iniciar sesión: {e}")
            self.label_error_visual.setText('Ocurrió un error al intentar iniciar sesión')
            return False


