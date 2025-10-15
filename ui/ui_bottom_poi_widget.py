# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bottom_poi_widgetsocENn.ui'
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
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(247, 94)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title_poi = QLabel(Form)
        self.label_title_poi.setObjectName(u"label_title_poi")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_title_poi.setFont(font)

        self.verticalLayout.addWidget(self.label_title_poi)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_around_patrol = QRadioButton(Form)
        self.radio_around_patrol.setObjectName(u"radio_around_patrol")

        self.horizontalLayout.addWidget(self.radio_around_patrol)

        self.radio_registered_loction = QRadioButton(Form)
        self.radio_registered_loction.setObjectName(u"radio_registered_loction")

        self.horizontalLayout.addWidget(self.radio_registered_loction)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title_poi.setText(QCoreApplication.translate("Form", u" P.O.I", None))
        self.radio_around_patrol.setText(QCoreApplication.translate("Form", u"\uc8fc\ubcc0\uc21c\ucc30", None))
        self.radio_registered_loction.setText(QCoreApplication.translate("Form", u"\ub4f1\ub85d \uc704\uce58", None))
    # retranslateUi

