# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(589, 526)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(203, 249, 241, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Form.setPalette(palette)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.etiqueta_titulo_prompt = QLabel(Form)
        self.etiqueta_titulo_prompt.setObjectName(u"etiqueta_titulo_prompt")

        self.horizontalLayout.addWidget(self.etiqueta_titulo_prompt)

        self.entrada_titulo_prompt = QLineEdit(Form)
        self.entrada_titulo_prompt.setObjectName(u"entrada_titulo_prompt")

        self.horizontalLayout.addWidget(self.entrada_titulo_prompt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cuadro_texto_prompt = QTextEdit(Form)
        self.cuadro_texto_prompt.setObjectName(u"cuadro_texto_prompt")

        self.verticalLayout.addWidget(self.cuadro_texto_prompt)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ButtonVaciar = QPushButton(Form)
        self.ButtonVaciar.setObjectName(u"ButtonVaciar")

        self.horizontalLayout_3.addWidget(self.ButtonVaciar)

        self.ButtonCopy = QPushButton(Form)
        self.ButtonCopy.setObjectName(u"ButtonCopy")

        self.horizontalLayout_3.addWidget(self.ButtonCopy)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 1, -1, 17)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.etiqueta_cuadro_titulo = QLabel(Form)
        self.etiqueta_cuadro_titulo.setObjectName(u"etiqueta_cuadro_titulo")

        self.verticalLayout_4.addWidget(self.etiqueta_cuadro_titulo)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 18)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setSizeIncrement(QSize(4, 0))
        self.scrollArea.setBaseSize(QSize(4, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.scrollArea.setPalette(palette1)
        self.scrollArea.setContextMenuPolicy(Qt.CustomContextMenu)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 180, 392))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.boton_anadir = QPushButton(Form)
        self.boton_anadir.setObjectName(u"boton_anadir")

        self.horizontalLayout_2.addWidget(self.boton_anadir)

        self.ButtonBorrar = QPushButton(Form)
        self.ButtonBorrar.setObjectName(u"ButtonBorrar")

        self.horizontalLayout_2.addWidget(self.ButtonBorrar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.etiqueta_titulo_prompt.setText(QCoreApplication.translate("Form", u"T\u00edtulo prompt:", None))
        self.ButtonVaciar.setText(QCoreApplication.translate("Form", u"Vaciar Prompt", None))
        self.ButtonCopy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
        self.label.setText("")
        self.etiqueta_cuadro_titulo.setText(QCoreApplication.translate("Form", u"Lista de Prompts:", None))
        self.boton_anadir.setText(QCoreApplication.translate("Form", u"A\u00f1adir", None))
        self.ButtonBorrar.setText(QCoreApplication.translate("Form", u"Borrar", None))
    # retranslateUi

