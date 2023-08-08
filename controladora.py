from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget

from controlado_vista_login import ControladoraLogin
from controlando_vista_principal import ControlandoraVistaPrincipal
from controlando_vista_registro import ControladoraRegistro


class Controladora(QWidget):
    def __init__(self):
        super().__init__()
        self.vista_login = ControladoraLogin()
        self.vista_registro = ControladoraRegistro()
        self.vista_principal = ControlandoraVistaPrincipal()
        self.vista_login.show()

        self.vista_login.boton_registrarse.clicked.connect(self.registro)
        self.vista_login.boton_entrar.clicked.connect(self.login)

        self.vista_registro.boton_registrar.clicked.connect(self.accion_registrar)
        self.vista_registro.boton_cancelar.clicked.connect(self.accion_cancelar)

    def login(self):

        if self.vista_login.login_validator():
            self.vista_login.close()
            self.vista_principal.show()
            self.vista_principal.mostrar_prompts_guardados()
        else:
            print("No pude entrar")

    def registro(self):
        self.vista_login.close()
        self.vista_registro.show()

    def accion_registrar(self):

        if self.vista_registro.register_validator():

            ret = QMessageBox.information(self, "Confirmacion de Registro", "El registro ha sido exitoso",
                                          QMessageBox.Ok)
            if ret == QMessageBox.Ok:
                self.vista_registro.close()
                self.vista_login.show()

    def accion_cancelar(self):
        self.vista_registro.close()
        self.vista_login.show()
