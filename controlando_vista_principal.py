from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMenuBar, QPushButton, QVBoxLayout, QMainWindow
from PySide6.QtGui import QFontMetrics
import database
from modelos import Contexto, Usuario
from ui_vista_main import Ui_vista_main


class ControlandoraVistaPrincipal(QMainWindow, Ui_vista_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lista_botones = []

        # self.actionLog_out_2.triggered.connect(self.log_out)
        self.boton_seleccionado: BotonEspecialPrompt()

        self.Layout_lista_prompts = QVBoxLayout()
        self.Layout_lista_prompts.setAlignment(Qt.AlignTop)
        self.widget = QWidget()
        self.widget.setLayout(self.Layout_lista_prompts)

        self.entrada_titulo_prompt_3.selectionChanged.connect(
            lambda: self.entrada_titulo_prompt_3.setText(''))

        self.AnadirButton.clicked.connect(self.anadir)
        self.BorrarButton.clicked.connect(self.borrar)
        self.VaciarButton.clicked.connect(self.vaciar)
        self.VaciarButton.setFixedSize(100, 25)
        self.CopyButton.clicked.connect(self.copiar)
        self.CopyButton.setFixedSize(100, 25)

        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setWidget(self.widget)
        self.ScrollArea.setMinimumSize(300, 400)

    def get_boton_seleccionado(self):

        # self.list_temp.append(self.sender())
        # print(len(list_temp))
        self.boton_seleccionado = self.sender()
        # return self.boton_seleccionado

    def anadir(self):
        try:
            titulo_prompt = self.entrada_titulo_prompt_3.text()
            usuario_activo = database.sesion.query(Usuario).filter(
                Usuario.sesion_iniciada == True
            ).first()
            if titulo_prompt == '':
                print('Titulo no valido')
                self.label_error_visual_main.setText(
                    'Ingrese un titulo por favor')
            elif self.cuadro_text_prompt.toPlainText() == '':
                print('Por favor escriba algun en texto en el prompt antes de anadirlo')
                self.label_error_visual_main.setText(
                    'Por favor escriba el contenido del prompt a guardar')
            elif len(titulo_prompt) < 100 and len(self.cuadro_text_prompt.toPlainText()) < 550:
                buscando_existencia_contexto = database.sesion.query(Contexto).filter(
                    Contexto.usuario_id == usuario_activo.id,
                    Contexto.nombre_contexto == titulo_prompt).first()

                if buscando_existencia_contexto == None:
                    database.sesion.add(Contexto(nombre_contexto=titulo_prompt,
                                                 contenido=self.cuadro_text_prompt.toPlainText(),
                                                 usuario_contextos=usuario_activo))
                    database.sesion.commit()

                    nuevo_boton = BotonEspecialPrompt(titulo_prompt)
                    nuevo_boton.nombre_contexto_vinculado = titulo_prompt
                    nuevo_boton.setMaximumSize(290, 30)
                    if len(titulo_prompt) > 34:
                        nuevo_boton.setToolTip(titulo_prompt)
                    nuevo_boton.clicked.connect(
                        lambda: self.mostrar_prompt(titulo_prompt))
                    nuevo_boton.setText(QFontMetrics(nuevo_boton.font()).elidedText(titulo_prompt, Qt.ElideRight,
                                                                                    nuevo_boton.width()-25))

                    nuevo_boton.clicked.connect(self.get_boton_seleccionado)
                    self.lista_botones.append(nuevo_boton)

                    self.Layout_lista_prompts.addWidget(nuevo_boton)
                    self.entrada_titulo_prompt_3.setText("")
                    self.cuadro_text_prompt.setText("")
                else:
                    print("Ese prompt ya existe")
                    self.label_error_visual_main.setText('ya existe un prompt guardado con ese titulo')
            else:
                if len(titulo_prompt) > 100:
                    print('El titulo del prompt es demasiado largo!')
                    self.label_error_visual_main.setText('El titulo del prompt es demasiado largo!')
                if len(self.cuadro_text_prompt.toPlainText()) > 550:
                    print('El prompt es demasiado largo!')
                    self.label_error_visual_main.setText('El prompt es demasiado largo!')
        except Exception as e:
            print(f'Algun error ha ocurrido:{e}')
            self.label_error_visual_main.setText('Ha ocurrido algun error')
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
        for i in self.lista_botones:
            if i.nombre_contexto_vinculado == nombre_contexto:
                self.lista_botones.remove(i)

        # Hacemos commit
        database.sesion.commit()
        self.entrada_titulo_prompt_3.clear()
        self.cuadro_text_prompt.clear()

    def vaciar(self):
        self.cuadro_text_prompt.setText("")

    def copiar(self):
        self.cuadro_text_prompt.selectAll()
        self.cuadro_text_prompt.copy()

    def mostrar_prompt(self, titulo):
        usuario_activo = database.sesion.query(Usuario).filter(
            Usuario.sesion_iniciada == True
        ).first()
        prompt = database.sesion.query(Contexto).filter(
            Contexto.usuario_id == usuario_activo.id,
            Contexto.nombre_contexto == titulo).first()

        self.cuadro_text_prompt.setText(prompt.contenido)
        self.entrada_titulo_prompt_3.setText(titulo)

    def mostrar_prompts_guardados(self):
        # lista_botones = []
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
                if len(i.nombre_contexto) > 34:
                    prep_boton.setToolTip(i.nombre_contexto)

                self.lista_botones.append(prep_boton)

        list(map(lambda boton: boton.clicked.connect(
            lambda: self.mostrar_prompt(boton.nombre_contexto_vinculado)), self.lista_botones))
        list(map(lambda boton: boton.clicked.connect(
            self.get_boton_seleccionado), self.lista_botones))

        list(map(lambda i: self.Layout_lista_prompts.addWidget(i), self.lista_botones))

    def vaciar_prompts(self):

        for i in self.lista_botones:
            self.Layout_lista_prompts.removeWidget(i)
            i.deleteLater()
        self.lista_botones = []

    def log_out(self):
        usuario_activo = database.sesion.query(Usuario).filter(
            Usuario.sesion_iniciada == True
        ).first()
        usuario_activo.sesion_iniciada = False
        database.sesion.commit()
        self.cuadro_text_prompt.clear()
        self.entrada_titulo_prompt_3.clear()


class BotonEspecialPrompt(QPushButton):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre_contexto_vinculado: str
