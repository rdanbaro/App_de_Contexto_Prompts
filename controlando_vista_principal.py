from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QFontMetrics
import database
from modelos import Contexto, Usuario
from ui_vista_principal import Ui_Form


class ControlandoraVistaPrincipal(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.boton_seleccionado: BotonEspecialPrompt()
        self.Layout_lista_prompts = QVBoxLayout()
        self.Layout_lista_prompts.setAlignment(Qt.AlignTop)
        self.widget = QWidget()
        self.widget.setLayout(self.Layout_lista_prompts)
        self.boton_anadir.clicked.connect(self.anadir)
        self.ButtonBorrar.clicked.connect(self.borrar)

        self.ButtonVaciar.clicked.connect(self.vaciar)
        self.ButtonVaciar.setFixedSize(100, 25)
        self.ButtonCopy.clicked.connect(self.copiar)
        self.ButtonCopy.setFixedSize(100, 25)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)
        self.scrollArea.setMinimumSize(300, 400)

    def get_boton_seleccionado(self):

        # self.list_temp.append(self.sender())
        # print(len(list_temp))
        self.boton_seleccionado = self.sender()
        # return self.boton_seleccionado

    def anadir(self):
        titulo_prompt = self.entrada_titulo_prompt.text()
        usuario_activo = database.sesion.query(Usuario).filter(
            Usuario.sesion_iniciada == True
        ).first()

        buscando_existencia_contexto = database.sesion.query(Contexto).filter(
            Contexto.usuario_id == usuario_activo.id,
            Contexto.nombre_contexto == titulo_prompt).first()

        database.sesion.add(Contexto(nombre_contexto=self.entrada_titulo_prompt.text(),
                                     contenido=self.cuadro_texto_prompt.toPlainText(),
                                     usuario_contextos=usuario_activo))
        database.sesion.commit()
        if buscando_existencia_contexto == None:
            titulo_prompt = self.entrada_titulo_prompt.text()
            nuevo_boton = BotonEspecialPrompt(titulo_prompt)
            nuevo_boton.nombre_contexto_vinculado = titulo_prompt
            nuevo_boton.setMaximumSize(290, 30)
            nuevo_boton.clicked.connect(
                lambda: self.mostrar_prompt(titulo_prompt))
            nuevo_boton.setText(QFontMetrics(nuevo_boton.font()).elidedText(titulo_prompt, Qt.ElideRight,
                                                                            nuevo_boton.width()-25))

            nuevo_boton.clicked.connect(self.get_boton_seleccionado)

            self.Layout_lista_prompts.addWidget(nuevo_boton)
            self.entrada_titulo_prompt.setText("")
            self.cuadro_texto_prompt.setText("")
        else:
            print("Ese prompt ya existe")

    def borrar(self):
        # # Obtenemos el botón pulsado
        # boton = self.sender()

        # Obtenemos el nombre del contexto a borrar
        nombre_contexto = self.boton_seleccionado.nombre_contexto_vinculado

        # Buscamos el contexto en la base de datos
        usuario_activo = database.sesion.query(Usuario).filter(
            Usuario.sesion_iniciada == True
        ).first()
        contexto = database.sesion.query(Contexto).filter(
            Contexto.usuario_id == usuario_activo.id,
            Contexto.nombre_contexto == nombre_contexto).first()

        # Eliminamos el contexto de la base de datos
        database.sesion.delete(contexto)

        # Eliminamos el botón

        self.Layout_lista_prompts.removeWidget(self.boton_seleccionado)
        self.boton_seleccionado.deleteLater()

        # Hacemos commit
        database.sesion.commit()

    def vaciar(self):
        self.cuadro_texto_prompt.setText("")

    def copiar(self):
        self.cuadro_texto_prompt.selectAll()
        self.cuadro_texto_prompt.copy()

    def mostrar_prompt(self, titulo):
        usuario_activo = database.sesion.query(Usuario).filter(
            Usuario.sesion_iniciada == True
        ).first()
        prompt = database.sesion.query(Contexto).filter(
            Contexto.usuario_id == usuario_activo.id,
            Contexto.nombre_contexto == titulo).first()

        self.cuadro_texto_prompt.setText(prompt.contenido)

    def mostrar_prompts_guardados(self):
        lista_botones = []
        usuario_activo = database.sesion.query(Usuario).filter(
            Usuario.sesion_iniciada == True
        ).first()
        contextos_usuario_activo = database.sesion.query(Contexto).filter(
            Contexto.usuario_contextos == usuario_activo
        ).all()
        if contextos_usuario_activo is not None:

            for i in contextos_usuario_activo:
                prep_boton = BotonEspecialPrompt(i.nombre_contexto)
                prep_boton.setMaximumSize(290, 30)
                prep_boton.nombre_contexto_vinculado = i.nombre_contexto
                prep_boton.setText(QFontMetrics(prep_boton.font()).elidedText(i.nombre_contexto, Qt.ElideRight,
                                                                              prep_boton.width()-25))
                lista_botones.append(prep_boton)

        list(map(lambda boton: boton.clicked.connect(
            lambda: self.mostrar_prompt(boton.nombre_contexto_vinculado)), lista_botones))
        list(map(lambda boton: boton.clicked.connect(
            self.get_boton_seleccionado), lista_botones))

        list(map(lambda i: self.Layout_lista_prompts.addWidget(i), lista_botones))


class BotonEspecialPrompt(QPushButton):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre_contexto_vinculado: str
