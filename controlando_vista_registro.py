from ui_vista_registro import Ui_VistaRegistro
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit
import database
from modelos import Usuario


class ControladoraRegistro(QWidget, Ui_VistaRegistro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(390, 360)
        self.entrada_contrasena_registro.setEchoMode(QLineEdit.Password)
        self.entrada_confirmar_contrasena.setEchoMode(QLineEdit.Password)

    def register_validator(self):
        usuario = self.entrada_usuario_registro.text()
        contrasena = self.entrada_contrasena_registro.text()
        confirmar_contrasena = self.entrada_confirmar_contrasena.text()
        buscando_existencia_usuario = database.sesion.query(Usuario).filter(
            Usuario.nombre_usuario == usuario).first()
        cuenta_valida = True
        try:
            if usuario == '' or contrasena == '' or confirmar_contrasena == '':
                print('usuario no valido')
                self.label_error_visual_reg.setText(
                    '                        Faltan campos por completar!')
                cuenta_valida = False

            elif len(usuario) > 50:
                print('nombre de usuario demasiado largo')
                self.label_error_visual_reg.setText(
                    '                        nombre de usuario demasiado largo')
                cuenta_valida = False
            elif buscando_existencia_usuario != None:
                print("Ese nombre de usuario ya existe!")
                cuenta_valida = False

            elif len(contrasena) > 50:
                print('contrasena demasiado larga')
                self.label_error_visual_reg.setText(
                    '                        contrasena demasiado larga')
                cuenta_valida = False
            
                cuenta_valida = False

            elif contrasena != confirmar_contrasena:
                print("La confirmacion y la contrasena no coinciden")
                self.label_error_visual_reg.setText(
                    ' La confirmacion y la contrasena no coinciden')
                cuenta_valida = False

            if cuenta_valida:
                database.sesion.add(
                    Usuario(nombre_usuario=usuario, contrasena=contrasena, sesion_iniciada=False))
                database.sesion.commit()

        except Exception as e:
            print(
                f"Algun error ha ocurrido, verifique que los campos sean validos: {e}")
            self.label_error_visual_reg.setText(
                'Algun error ha ocurrido, verifique que los campos sean validos')
            cuenta_valida = False
        return cuenta_valida
