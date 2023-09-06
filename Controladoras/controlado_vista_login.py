from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtGui import QGuiApplication
import database
from Modelo.modelos import Usuario
from Vistas.ui_vista_login import Ui_VentanaPrincipal

# Clase ControladoraLogin que hereda de QWidget y Ui_VentanaPrincipal
class ControladoraLogin(QWidget, Ui_VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.contrasena_entrada.setEchoMode(QLineEdit.Password)

    # Función para centrar la ventana en la pantalla
    def centrar_ventana(self):
        # Obtener el tamaño de la pantalla
        pantalla = QGuiApplication.primaryScreen().availableGeometry()
        # Obtener el tamaño de la ventana
        ventana = self.geometry()
        # Calcular las coordenadas para centrar la ventana
        x = (pantalla.width() - ventana.width()) // 2
        y = (pantalla.height() - ventana.height()) // 2
        self.move(x, y)

    # Función para validar el inicio de sesión
    def login_validator(self):
        usuario = self.usuario_entrada.text()
        contrasena = self.contrasena_entrada.text()
        try:
            # Buscar el usuario en la base de datos
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
