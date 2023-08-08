# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_registro.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_VistaRegistro(object):
    def setupUi(self, VistaRegistro):
        if not VistaRegistro.objectName():
            VistaRegistro.setObjectName(u"VistaRegistro")
        VistaRegistro.resize(282, 282)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(46, 194, 126, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        VistaRegistro.setPalette(palette)
        self.widget = QWidget(VistaRegistro)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 261, 261))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        brush2 = QBrush(QColor(176, 244, 228, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.widget.setPalette(palette1)
        self.widget.setFocusPolicy(Qt.NoFocus)
        self.widget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget.setAutoFillBackground(True)
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 230, 101))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.etiqueta_usuario_registro = QLabel(self.layoutWidget)
        self.etiqueta_usuario_registro.setObjectName(u"etiqueta_usuario_registro")
        self.etiqueta_usuario_registro.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.etiqueta_usuario_registro)

        self.etiqueta_contrasena_registro = QLabel(self.layoutWidget)
        self.etiqueta_contrasena_registro.setObjectName(u"etiqueta_contrasena_registro")
        self.etiqueta_contrasena_registro.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.etiqueta_contrasena_registro)

        self.etiqueta_confirmar_contrasena = QLabel(self.layoutWidget)
        self.etiqueta_confirmar_contrasena.setObjectName(u"etiqueta_confirmar_contrasena")
        self.etiqueta_confirmar_contrasena.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.etiqueta_confirmar_contrasena)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.entrada_usuario_registro = QLineEdit(self.layoutWidget)
        self.entrada_usuario_registro.setObjectName(u"entrada_usuario_registro")

        self.verticalLayout_2.addWidget(self.entrada_usuario_registro)

        self.entrada_contrasena_registro = QLineEdit(self.layoutWidget)
        self.entrada_contrasena_registro.setObjectName(u"entrada_contrasena_registro")

        self.verticalLayout_2.addWidget(self.entrada_contrasena_registro)

        self.entrada_confirmar_contrasena = QLineEdit(self.layoutWidget)
        self.entrada_confirmar_contrasena.setObjectName(u"entrada_confirmar_contrasena")

        self.verticalLayout_2.addWidget(self.entrada_confirmar_contrasena)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.boton_registrar = QPushButton(self.widget)
        self.boton_registrar.setObjectName(u"boton_registrar")
        self.boton_registrar.setGeometry(QRect(150, 180, 89, 31))
        palette2 = QPalette()
        brush3 = QBrush(QColor(163, 223, 236, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        self.boton_registrar.setPalette(palette2)
        self.boton_cancelar = QPushButton(self.widget)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(30, 180, 89, 31))
        palette3 = QPalette()
        brush4 = QBrush(QColor(239, 133, 133, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        self.boton_cancelar.setPalette(palette3)

        self.retranslateUi(VistaRegistro)

        QMetaObject.connectSlotsByName(VistaRegistro)
    # setupUi

    def retranslateUi(self,  VistaRegistro):
        VistaRegistro.setWindowTitle(QCoreApplication.translate("VistaRegistro", u"Form", None))
        self.etiqueta_usuario_registro.setText(QCoreApplication.translate("VistaRegistro", u"usuario", None))
        self.etiqueta_contrasena_registro.setText(QCoreApplication.translate("VistaRegistro", u"contrase\u00f1a", None))
        self.etiqueta_confirmar_contrasena.setText(QCoreApplication.translate("VistaRegistro", u"confirmar\n"
"contrase\u00f1a", None))
        self.boton_registrar.setText(QCoreApplication.translate("VistaRegistro", u"Registrar", None))
        self.boton_cancelar.setText(QCoreApplication.translate("VistaRegistro", u"Cancelar", None))
    # retranslateUi

