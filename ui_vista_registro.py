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
        VistaRegistro.resize(367, 379)
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
        self.verticalLayout_3 = QVBoxLayout(VistaRegistro)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(VistaRegistro)
        self.widget.setObjectName(u"widget")
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
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 44, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.etiqueta_usuario_registro = QLabel(self.widget)
        self.etiqueta_usuario_registro.setObjectName(u"etiqueta_usuario_registro")
        self.etiqueta_usuario_registro.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.etiqueta_usuario_registro)

        self.etiqueta_contrasena_registro = QLabel(self.widget)
        self.etiqueta_contrasena_registro.setObjectName(u"etiqueta_contrasena_registro")
        self.etiqueta_contrasena_registro.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.etiqueta_contrasena_registro)

        self.etiqueta_confirmar_contrasena = QLabel(self.widget)
        self.etiqueta_confirmar_contrasena.setObjectName(u"etiqueta_confirmar_contrasena")
        self.etiqueta_confirmar_contrasena.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.verticalLayout.addWidget(self.etiqueta_confirmar_contrasena)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 3)
        self.entrada_usuario_registro = QLineEdit(self.widget)
        self.entrada_usuario_registro.setObjectName(u"entrada_usuario_registro")

        self.verticalLayout_2.addWidget(self.entrada_usuario_registro)

        self.entrada_contrasena_registro = QLineEdit(self.widget)
        self.entrada_contrasena_registro.setObjectName(u"entrada_contrasena_registro")

        self.verticalLayout_2.addWidget(self.entrada_contrasena_registro)

        self.entrada_confirmar_contrasena = QLineEdit(self.widget)
        self.entrada_confirmar_contrasena.setObjectName(u"entrada_confirmar_contrasena")

        self.verticalLayout_2.addWidget(self.entrada_confirmar_contrasena)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.label_error_visual_reg = QLabel(self.widget)
        self.label_error_visual_reg.setObjectName(u"label_error_visual_reg")
        palette2 = QPalette()
        brush3 = QBrush(QColor(224, 27, 36, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(190, 190, 190, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.label_error_visual_reg.setPalette(palette2)
        self.label_error_visual_reg.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label_error_visual_reg)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, 9, 30)
        self.boton_cancelar = QPushButton(self.widget)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setEnabled(True)
        self.boton_cancelar.setMaximumSize(QSize(110, 16777215))
        palette3 = QPalette()
        brush5 = QBrush(QColor(239, 133, 133, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        self.boton_cancelar.setPalette(palette3)

        self.horizontalLayout_2.addWidget(self.boton_cancelar)

        self.boton_registrar = QPushButton(self.widget)
        self.boton_registrar.setObjectName(u"boton_registrar")
        self.boton_registrar.setMaximumSize(QSize(110, 16777215))
        palette4 = QPalette()
        brush6 = QBrush(QColor(163, 223, 236, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        self.boton_registrar.setPalette(palette4)

        self.horizontalLayout_2.addWidget(self.boton_registrar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(VistaRegistro)

        QMetaObject.connectSlotsByName(VistaRegistro)
    # setupUi

    def retranslateUi(self, VistaRegistro):
        VistaRegistro.setWindowTitle(QCoreApplication.translate("VistaRegistro", u"Form", None))
        self.etiqueta_usuario_registro.setText(QCoreApplication.translate("VistaRegistro", u"usuario", None))
        self.etiqueta_contrasena_registro.setText(QCoreApplication.translate("VistaRegistro", u"contrase\u00f1a", None))
        self.etiqueta_confirmar_contrasena.setText(QCoreApplication.translate("VistaRegistro", u"confirmar\n"
"contrase\u00f1a", None))
        self.label_error_visual_reg.setText("")
        self.boton_cancelar.setText(QCoreApplication.translate("VistaRegistro", u"Cancelar", None))
        self.boton_registrar.setText(QCoreApplication.translate("VistaRegistro", u"Registrar", None))
    # retranslateUi

