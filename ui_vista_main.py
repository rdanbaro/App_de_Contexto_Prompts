# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_vista_main(object):
    def setupUi(self, vista_main):
        if not vista_main.objectName():
            vista_main.setObjectName(u"vista_main")
        vista_main.resize(789, 428)
        palette = QPalette()
        brush = QBrush(QColor(143, 240, 164, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(153, 193, 241, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        vista_main.setPalette(palette)
        self.actionLog_out = QAction(vista_main)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.action = QAction(vista_main)
        self.action.setObjectName(u"action")
        self.actionsession = QAction(vista_main)
        self.actionsession.setObjectName(u"actionsession")
        self.actionLog_out_2 = QAction(vista_main)
        self.actionLog_out_2.setObjectName(u"actionLog_out_2")
        self.centralwidget = QWidget(vista_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_13 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_titulo_prompt_3 = QLabel(self.centralwidget)
        self.label_titulo_prompt_3.setObjectName(u"label_titulo_prompt_3")

        self.horizontalLayout_9.addWidget(self.label_titulo_prompt_3)

        self.entrada_titulo_prompt_3 = QLineEdit(self.centralwidget)
        self.entrada_titulo_prompt_3.setObjectName(u"entrada_titulo_prompt_3")

        self.horizontalLayout_9.addWidget(self.entrada_titulo_prompt_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.cuadro_text_prompt = QTextEdit(self.centralwidget)
        self.cuadro_text_prompt.setObjectName(u"cuadro_text_prompt")

        self.verticalLayout_10.addWidget(self.cuadro_text_prompt)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.VaciarButton = QPushButton(self.centralwidget)
        self.VaciarButton.setObjectName(u"VaciarButton")

        self.horizontalLayout_11.addWidget(self.VaciarButton)

        self.CopyButton = QPushButton(self.centralwidget)
        self.CopyButton.setObjectName(u"CopyButton")

        self.horizontalLayout_11.addWidget(self.CopyButton)

        self.label_error_visual_main = QLabel(self.centralwidget)
        self.label_error_visual_main.setObjectName(u"label_error_visual_main")
        palette1 = QPalette()
        brush3 = QBrush(QColor(224, 27, 36, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(190, 190, 190, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.label_error_visual_main.setPalette(palette1)

        self.horizontalLayout_11.addWidget(self.label_error_visual_main)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 1, -1, 17)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)

        self.label_cuadro_titulo = QLabel(self.centralwidget)
        self.label_cuadro_titulo.setObjectName(u"label_cuadro_titulo")

        self.verticalLayout_11.addWidget(self.label_cuadro_titulo)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 18)
        self.ScrollArea = QScrollArea(self.centralwidget)
        self.ScrollArea.setObjectName(u"ScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrollArea.sizePolicy().hasHeightForWidth())
        self.ScrollArea.setSizePolicy(sizePolicy)
        self.ScrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.ScrollArea.setSizeIncrement(QSize(4, 0))
        self.ScrollArea.setBaseSize(QSize(4, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.ScrollArea.setPalette(palette2)
        self.ScrollArea.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 180, 272))
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_12.addWidget(self.ScrollArea)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetMaximumSize)
        self.AnadirButton = QPushButton(self.centralwidget)
        self.AnadirButton.setObjectName(u"AnadirButton")

        self.horizontalLayout_12.addWidget(self.AnadirButton)

        self.BorrarButton = QPushButton(self.centralwidget)
        self.BorrarButton.setObjectName(u"BorrarButton")

        self.horizontalLayout_12.addWidget(self.BorrarButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        vista_main.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(vista_main)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 789, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy1)
        self.menuBar.setLayoutDirection(Qt.RightToLeft)
        self.menuhola = QMenu(self.menuBar)
        self.menuhola.setObjectName(u"menuhola")
        vista_main.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuhola.menuAction())
        self.menuhola.addAction(self.actionLog_out_2)

        self.retranslateUi(vista_main)

        QMetaObject.connectSlotsByName(vista_main)
    # setupUi

    def retranslateUi(self, vista_main):
        vista_main.setWindowTitle(QCoreApplication.translate("vista_main", u"App Prompt", None))
        self.actionLog_out.setText(QCoreApplication.translate("vista_main", u"Log out", None))
        self.action.setText("")
        self.actionsession.setText(QCoreApplication.translate("vista_main", u"session", None))
        self.actionLog_out_2.setText(QCoreApplication.translate("vista_main", u"Log out", None))
        self.label_titulo_prompt_3.setText(QCoreApplication.translate("vista_main", u"T\u00edtulo prompt:", None))
        self.VaciarButton.setText(QCoreApplication.translate("vista_main", u"Vaciar ", None))
        self.CopyButton.setText(QCoreApplication.translate("vista_main", u"Copy", None))
        self.label_error_visual_main.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_cuadro_titulo.setText(QCoreApplication.translate("vista_main", u"Lista de Prompts:", None))
        self.AnadirButton.setText(QCoreApplication.translate("vista_main", u"A\u00f1adir", None))
        self.BorrarButton.setText(QCoreApplication.translate("vista_main", u"Borrar", None))
        self.menuhola.setTitle(QCoreApplication.translate("vista_main", u"Session", None))
    # retranslateUi

