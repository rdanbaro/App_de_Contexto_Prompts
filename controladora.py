from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut

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

        self.vista_principal.actionLog_out_2.triggered.connect(self.accion_log_out)

        # Crear un atajo de teclado para el botón "registrar"
        shortcut_registrar = QShortcut(QKeySequence(Qt.Key_Return), self.vista_registro)
        shortcut_registrar.activated.connect(self.accion_registrar)

        # Crear un atajo de teclado para el botón "entrar"
        shortcut_entrar = QShortcut(QKeySequence(Qt.Key_Return), self.vista_login)
        shortcut_entrar.activated.connect(self.login)


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
                self.vista_login.usuario_entrada.setText("")
                self.vista_login.contrasena_entrada.setText("")
                self.vista_login.show()

    def accion_cancelar(self):
        self.vista_registro.close()
        self.vista_login.usuario_entrada.setText("")
        self.vista_login.contrasena_entrada.setText("")
        self.vista_login.show()

    def accion_log_out(self):
        self.vista_principal.vaciar_prompts()
        self.vista_principal.log_out()
        self.vista_principal.close()
        self.vista_login.usuario_entrada.setText("")
        self.vista_login.contrasena_entrada.setText("")
        self.vista_login.show()

