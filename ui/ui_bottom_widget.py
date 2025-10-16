# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bottom_widgetdkLWnY.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(339, 96)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title_location = QLabel(Form)
        self.label_title_location.setObjectName(u"label_title_location")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_title_location.setFont(font)

        self.verticalLayout_2.addWidget(self.label_title_location)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_title_latitude = QLabel(Form)
        self.label_title_latitude.setObjectName(u"label_title_latitude")

        self.horizontalLayout_3.addWidget(self.label_title_latitude)

        self.label_value_latitude = QLabel(Form)
        self.label_value_latitude.setObjectName(u"label_value_latitude")

        self.horizontalLayout_3.addWidget(self.label_value_latitude)

        self.label_title_longitude = QLabel(Form)
        self.label_title_longitude.setObjectName(u"label_title_longitude")

        self.horizontalLayout_3.addWidget(self.label_title_longitude)

        self.label_value_longitude = QLabel(Form)
        self.label_value_longitude.setObjectName(u"label_value_longitude")

        self.horizontalLayout_3.addWidget(self.label_value_longitude)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.button_move_location = QPushButton(Form)
        self.button_move_location.setObjectName(u"button_move_location")

        self.verticalLayout_2.addWidget(self.button_move_location)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title_poi = QLabel(Form)
        self.label_title_poi.setObjectName(u"label_title_poi")
        self.label_title_poi.setFont(font)

        self.verticalLayout.addWidget(self.label_title_poi)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radio_around_patrol = QRadioButton(Form)
        self.radio_around_patrol.setObjectName(u"radio_around_patrol")
        self.radio_around_patrol.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radio_around_patrol)

        self.radio_registered_loction = QRadioButton(Form)
        self.radio_registered_loction.setObjectName(u"radio_registered_loction")

        self.horizontalLayout_2.addWidget(self.radio_registered_loction)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.button_start_patrol = QPushButton(Form)
        self.button_start_patrol.setObjectName(u"button_start_patrol")

        self.verticalLayout.addWidget(self.button_start_patrol)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


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
        self.label_title_poi.setText(QCoreApplication.translate("Form", u" P.O.I", None))
        self.radio_around_patrol.setText(QCoreApplication.translate("Form", u"\uc8fc\ubcc0\uc21c\ucc30", None))
        self.radio_registered_loction.setText(QCoreApplication.translate("Form", u"\ub4f1\ub85d \uc704\uce58", None))
        self.button_start_patrol.setText(QCoreApplication.translate("Form", u"\uc21c\ucc30 \uc2dc\uc791", None))
    # retranslateUi

