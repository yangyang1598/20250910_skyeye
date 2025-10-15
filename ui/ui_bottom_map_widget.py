# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bottom_map_widgetmfuJWu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(279, 93)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title_location = QLabel(Form)
        self.label_title_location.setObjectName(u"label_title_location")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_title_location.setFont(font)

        self.verticalLayout.addWidget(self.label_title_location)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_title_latitude = QLabel(Form)
        self.label_title_latitude.setObjectName(u"label_title_latitude")

        self.horizontalLayout.addWidget(self.label_title_latitude)

        self.label_value_latitude = QLabel(Form)
        self.label_value_latitude.setObjectName(u"label_value_latitude")

        self.horizontalLayout.addWidget(self.label_value_latitude)

        self.label_title_longitude = QLabel(Form)
        self.label_title_longitude.setObjectName(u"label_title_longitude")

        self.horizontalLayout.addWidget(self.label_title_longitude)

        self.label_value_longitude = QLabel(Form)
        self.label_value_longitude.setObjectName(u"label_value_longitude")

        self.horizontalLayout.addWidget(self.label_value_longitude)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.button_move_location = QPushButton(Form)
        self.button_move_location.setObjectName(u"button_move_location")

        self.verticalLayout.addWidget(self.button_move_location)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title_location.setText(QCoreApplication.translate("Form", u"\uc9c0\ub3c4", None))
        self.label_title_latitude.setText(QCoreApplication.translate("Form", u"\uc704\ub3c4", None))
        self.label_value_latitude.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_title_longitude.setText(QCoreApplication.translate("Form", u"\uacbd\ub3c4", None))
        self.label_value_longitude.setText(QCoreApplication.translate("Form", u"0", None))
        self.button_move_location.setText(QCoreApplication.translate("Form", u"\ud5ec\ub9ac\uce74\uc774\ud2b8 \uc704\uce58\ub85c \uc774\ub3d9", None))
    # retranslateUi

