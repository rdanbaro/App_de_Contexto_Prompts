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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(383, 321)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
        VentanaPrincipal.setWindowOpacity(6.500000000000000)
        self.horizontalLayout_2 = QHBoxLayout(VentanaPrincipal)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(13, -1, 13, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, -1, 7, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.etiqueta_usuario = QLabel(self.widget)
        self.etiqueta_usuario.setObjectName(u"etiqueta_usuario")
        self.etiqueta_usuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.etiqueta_usuario)

        self.etiqueta_contrasena = QLabel(self.widget)
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
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usuario_entrada = QLineEdit(self.widget)
        self.usuario_entrada.setObjectName(u"usuario_entrada")

        self.verticalLayout.addWidget(self.usuario_entrada)

        self.contrasena_entrada = QLineEdit(self.widget)
        self.contrasena_entrada.setObjectName(u"contrasena_entrada")

        self.verticalLayout.addWidget(self.contrasena_entrada)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_error_visual = QLabel(self.widget)
        self.label_error_visual.setObjectName(u"label_error_visual")
        self.label_error_visual.setMaximumSize(QSize(16777215, 25))
        palette3 = QPalette()
        brush9 = QBrush(QColor(224, 27, 36, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        brush10 = QBrush(QColor(190, 190, 190, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        self.label_error_visual.setPalette(palette3)
        self.label_error_visual.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_error_visual)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.boton_registrarse = QPushButton(self.widget)
        self.boton_registrarse.setObjectName(u"boton_registrarse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.boton_registrarse.sizePolicy().hasHeightForWidth())
        self.boton_registrarse.setSizePolicy(sizePolicy1)
        self.boton_registrarse.setMaximumSize(QSize(110, 16777215))
        self.boton_registrarse.setBaseSize(QSize(0, 0))
        palette4 = QPalette()
        brush11 = QBrush(QColor(163, 223, 236, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        self.boton_registrarse.setPalette(palette4)

        self.horizontalLayout_3.addWidget(self.boton_registrarse)

        self.boton_entrar = QPushButton(self.widget)
        self.boton_entrar.setObjectName(u"boton_entrar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.boton_entrar.sizePolicy().hasHeightForWidth())
        self.boton_entrar.setSizePolicy(sizePolicy2)
        self.boton_entrar.setMaximumSize(QSize(110, 16777215))
        self.boton_entrar.setBaseSize(QSize(0, 0))
        palette5 = QPalette()
        brush12 = QBrush(QColor(239, 239, 239, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        self.boton_entrar.setPalette(palette5)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        self.boton_entrar.setFont(font)
        self.boton_entrar.setAcceptDrops(False)
        self.boton_entrar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.boton_entrar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Login", None))
        self.etiqueta_usuario.setText(QCoreApplication.translate("VentanaPrincipal", u"usuario", None))
        self.etiqueta_contrasena.setText(QCoreApplication.translate("VentanaPrincipal", u"contrase\u00f1a", None))
        self.usuario_entrada.setText("")
        self.label_error_visual.setText("")
        self.boton_registrarse.setText(QCoreApplication.translate("VentanaPrincipal", u"Registrarse", None))
        self.boton_entrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Entrar", None))
    # retranslateUi

