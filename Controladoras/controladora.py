from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut, QScreen, QGuiApplication
import sys
from Controladoras.controlado_vista_login import ControladoraLogin
from Controladoras.controlando_vista_principal import ControlandoraVistaPrincipal
from Controladoras.controlando_vista_registro import ControladoraRegistro

class Controladora(QWidget):
    def __init__(self):
        super().__init__()

        # Instanciar las vistas
        self.vista_login = ControladoraLogin()
        self.vista_registro = ControladoraRegistro()
        self.vista_principal = ControlandoraVistaPrincipal()

        # Mostrar la vista de inicio de sesión
        self.vista_login.show()

        # Conectar los botones de la vista de inicio de sesión con los métodos correspondientes
        self.vista_login.boton_registrarse.clicked.connect(self.registro)
        self.vista_login.boton_entrar.clicked.connect(self.login)

        # Conectar los botones de la vista de registro con los métodos correspondientes
        self.vista_registro.boton_registrar.clicked.connect(self.accion_registrar)
        self.vista_registro.boton_cancelar.clicked.connect(self.accion_cancelar)

        # Conectar la opción de cerrar sesión en la vista principal con el método correspondiente
        self.vista_principal.actionLog_out_2.triggered.connect(self.accion_log_out)

        # Crear atajos de teclado para los botones "registrar" y "entrar"
        shortcut_registrar = QShortcut(QKeySequence(Qt.Key_Return), self.vista_registro)
        shortcut_registrar.activated.connect(self.accion_registrar)
        shortcut_entrar = QShortcut(QKeySequence(Qt.Key_Return), self.vista_login)
        shortcut_entrar.activated.connect(self.login)

    def login(self):
        # Validar el inicio de sesión
        if self.vista_login.login_validator():
            # Cerrar la vista de inicio de sesión
            self.vista_login.close()

            # Mostrar la vista principal
            self.vista_principal.show()

            # Mostrar los prompts guardados en la vista principal
            self.vista_principal.mostrar_prompts_guardados()

    def registro(self):
        # Limpiar el mensaje de error en la vista de registro
        self.vista_registro.label_error_visual_reg.clear()

        # Cerrar la vista de inicio de sesión
        self.vista_login.close()

        # Mostrar la vista de registro
        self.vista_registro.show()

        # Mover la vista de registro a una posición específica
        self.vista_registro.move(1700, 1800)

    def accion_registrar(self):
        # Validar el registro
        if self.vista_registro.register_validator():
            # Mostrar un cuadro de diálogo de confirmación
            ret = QMessageBox.information(self, "Confirmacion de Registro", "El registro ha sido exitoso", QMessageBox.Ok)

            # Si se confirma el registro, cerrar la vista de registro y limpiar los campos
            if ret == QMessageBox.Ok:
                self.vista_registro.close()
                self.vista_login.usuario_entrada.clear()
                self.vista_login.contrasena_entrada.clear()
                self.vista_registro.entrada_usuario_registro.clear()
                self.vista_registro.entrada_contrasena_registro.clear()
                self.vista_registro.entrada_confirmar_contrasena.clear()

                # Centrar la vista de inicio de sesión en la pantalla
                self.center_window(self.vista_login)

                # Mostrar la vista de inicio de sesión
                self.vista_login.show()

    def accion_cancelar(self):
        # Cerrar la vista de registro
        self.vista_registro.close()

        # Limpiar los campos de la vista de inicio de sesión y de registro
        self.vista_login.usuario_entrada.clear()
        self.vista_login.contrasena_entrada.clear()
        self.vista_login.label_error_visual.clear()
        self.vista_registro.entrada_usuario_registro.clear()
        self.vista_registro.entrada_contrasena_registro.clear()
        self.vista_registro.entrada_confirmar_contrasena.clear()

        # Centrar la vista de inicio de sesión en la pantalla
        self.center_window(self.vista_login)

        # Mostrar la vista de inicio de sesión
        self.vista_login.show()

    def accion_log_out(self):
        # Vaciar los prompts en la vista principal
        self.vista_principal.vaciar_prompts()

        # Limpiar el mensaje de error en la vista principal
        self.vista_principal.label_error_visual_main.clear()

        # Cerrar la vista principal
        self.vista_principal.close()

        # Limpiar los campos de la vista de inicio de sesión
        self.vista_login.usuario_entrada.setText("")
        self.vista_login.contrasena_entrada.setText("")
        self.vista_login.label_error_visual.clear()

        # Mostrar la vista de inicio de sesión
        self.vista_login.show()

    def center_window(self, widget):
        # Obtener el objeto QScreen activo
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Obtener la geometría del widget
        widget_geometry = widget.frameGeometry()

        # Calcular la posición central del widget
        center_position = screen_geometry.center() - widget_geometry.center()

        # Mover el widget a la posición central
        widget.move(center_position)