# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_login.ui'
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
    QPushButton,  QSizePolicy, QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(263, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaPrincipal.sizePolicy().hasHeightForWidth())
        VentanaPrincipal.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(132, 200, 178, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        VentanaPrincipal.setPalette(palette)
        VentanaPrincipal.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout_3 = QVBoxLayout(VentanaPrincipal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(VentanaPrincipal)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(235, 1))
        self.widget.setMaximumSize(QSize(1000, 16777215))
        palette1 = QPalette()
        brush2 = QBrush(QColor(153, 193, 241, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        brush3 = QBrush(QColor(203, 249, 241, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.widget.setPalette(palette1)
        self.widget.setFocusPolicy(Qt.NoFocus)
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setAutoFillBackground(True)
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 221, 60))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.etiqueta_usuario = QLabel(self.layoutWidget)
        self.etiqueta_usuario.setObjectName(u"etiqueta_usuario")
        self.etiqueta_usuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.etiqueta_usuario)

        self.etiqueta_contrasena = QLabel(self.layoutWidget)
        self.etiqueta_contrasena.setObjectName(u"etiqueta_contrasena")
        palette2 = QPalette()
        brush4 = QBrush(QColor(149, 244, 221, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush2)
        brush5 = QBrush(QColor(249, 240, 107, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        brush6 = QBrush(QColor(97, 234, 201, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush6)
        brush7 = QBrush(QColor(53, 132, 228, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        brush8 = QBrush(QColor(230, 97, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.etiqueta_contrasena.setPalette(palette2)
        self.etiqueta_contrasena.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.etiqueta_contrasena)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usuario_entrada = QLineEdit(self.layoutWidget)
        self.usuario_entrada.setObjectName(u"usuario_entrada")

        self.verticalLayout.addWidget(self.usuario_entrada)

        self.contrasena_entrada = QLineEdit(self.layoutWidget)
        self.contrasena_entrada.setObjectName(u"contrasena_entrada")

        self.verticalLayout.addWidget(self.contrasena_entrada)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.boton_entrar = QPushButton(self.widget)
        self.boton_entrar.setObjectName(u"boton_entrar")
        self.boton_entrar.setGeometry(QRect(140, 160, 91, 31))
        self.boton_entrar.setMaximumSize(QSize(235, 16777215))
        palette3 = QPalette()
        brush9 = QBrush(QColor(239, 239, 239, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        self.boton_entrar.setPalette(palette3)
        self.boton_entrar.setStyleSheet(u"")
        self.boton_registrarse = QPushButton(self.widget)
        self.boton_registrarse.setObjectName(u"boton_registrarse")
        self.boton_registrarse.setGeometry(QRect(30, 160, 91, 31))
        palette4 = QPalette()
        brush10 = QBrush(QColor(163, 223, 236, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        self.boton_registrarse.setPalette(palette4)

        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Login", None))
        self.etiqueta_usuario.setText(QCoreApplication.translate("VentanaPrincipal", u"usuario", None))
        self.etiqueta_contrasena.setText(QCoreApplication.translate("VentanaPrincipal", u"contrase\u00f1a", None))
        self.boton_entrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Entrar", None))
        self.boton_registrarse.setText(QCoreApplication.translate("VentanaPrincipal", u"Registrarse", None))
    # retranslateUi

