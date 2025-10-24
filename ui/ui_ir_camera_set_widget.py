# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ir_camera_set_widgetGOemga.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(531, 306)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_black_hot = QRadioButton(Form)
        self.radio_black_hot.setObjectName(u"radio_black_hot")

        self.gridLayout.addWidget(self.radio_black_hot, 1, 1, 1, 1)

        self.radio_rainbow = QRadioButton(Form)
        self.radio_rainbow.setObjectName(u"radio_rainbow")

        self.gridLayout.addWidget(self.radio_rainbow, 3, 1, 1, 1)

        self.radio_hot_iron = QRadioButton(Form)
        self.radio_hot_iron.setObjectName(u"radio_hot_iron")

        self.gridLayout.addWidget(self.radio_hot_iron, 4, 1, 1, 1)

        self.radio_rainbow_hc = QRadioButton(Form)
        self.radio_rainbow_hc.setObjectName(u"radio_rainbow_hc")

        self.gridLayout.addWidget(self.radio_rainbow_hc, 3, 0, 1, 1)

        self.radio_white_hot = QRadioButton(Form)
        self.radio_white_hot.setObjectName(u"radio_white_hot")

        self.gridLayout.addWidget(self.radio_white_hot, 1, 0, 1, 1)

        self.radio_ironbow = QRadioButton(Form)
        self.radio_ironbow.setObjectName(u"radio_ironbow")

        self.gridLayout.addWidget(self.radio_ironbow, 4, 0, 1, 1)

        self.radio_lava = QRadioButton(Form)
        self.radio_lava.setObjectName(u"radio_lava")

        self.gridLayout.addWidget(self.radio_lava, 2, 1, 1, 1)

        self.label_title_ir_color_palette = QLabel(Form)
        self.label_title_ir_color_palette.setObjectName(u"label_title_ir_color_palette")
        self.label_title_ir_color_palette.setMaximumSize(QSize(200, 20))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        self.label_title_ir_color_palette.setFont(font)

        self.gridLayout.addWidget(self.label_title_ir_color_palette, 0, 0, 1, 1)

        self.radio_red_hot = QRadioButton(Form)
        self.radio_red_hot.setObjectName(u"radio_red_hot")

        self.gridLayout.addWidget(self.radio_red_hot, 2, 0, 1, 1)

        self.radio_arctic = QRadioButton(Form)
        self.radio_arctic.setObjectName(u"radio_arctic")

        self.gridLayout.addWidget(self.radio_arctic, 5, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radio_EO_IR = QRadioButton(Form)
        self.radio_EO_IR.setObjectName(u"radio_EO_IR")

        self.gridLayout_2.addWidget(self.radio_EO_IR, 2, 0, 1, 1)

        self.radio_IR_EO = QRadioButton(Form)
        self.radio_IR_EO.setObjectName(u"radio_IR_EO")

        self.gridLayout_2.addWidget(self.radio_IR_EO, 2, 1, 1, 1)

        self.label_title_ir_sensor = QLabel(Form)
        self.label_title_ir_sensor.setObjectName(u"label_title_ir_sensor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title_ir_sensor.sizePolicy().hasHeightForWidth())
        self.label_title_ir_sensor.setSizePolicy(sizePolicy)
        self.label_title_ir_sensor.setMaximumSize(QSize(200, 20))
        self.label_title_ir_sensor.setFont(font)

        self.gridLayout_2.addWidget(self.label_title_ir_sensor, 0, 0, 1, 1)

        self.radio_eo = QRadioButton(Form)
        self.radio_eo.setObjectName(u"radio_eo")

        self.gridLayout_2.addWidget(self.radio_eo, 1, 0, 1, 1)

        self.radio_ir = QRadioButton(Form)
        self.radio_ir.setObjectName(u"radio_ir")

        self.gridLayout_2.addWidget(self.radio_ir, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"IR \uc7a5\ube44 \uc124\uc815", None))
        self.radio_black_hot.setText(QCoreApplication.translate("Form", u"Black Hot", None))
        self.radio_rainbow.setText(QCoreApplication.translate("Form", u"Rainbow", None))
        self.radio_hot_iron.setText(QCoreApplication.translate("Form", u"Hot Iron", None))
        self.radio_rainbow_hc.setText(QCoreApplication.translate("Form", u"Rainbow HC", None))
        self.radio_white_hot.setText(QCoreApplication.translate("Form", u"White Hot", None))
        self.radio_ironbow.setText(QCoreApplication.translate("Form", u"Ironbow", None))
        self.radio_lava.setText(QCoreApplication.translate("Form", u"Lava", None))
        self.label_title_ir_color_palette.setText(QCoreApplication.translate("Form", u"IR Color Palette", None))
        self.radio_red_hot.setText(QCoreApplication.translate("Form", u"Red Hot", None))
        self.radio_arctic.setText(QCoreApplication.translate("Form", u"Arctic", None))
        self.radio_EO_IR.setText(QCoreApplication.translate("Form", u"EO+IR", None))
        self.radio_IR_EO.setText(QCoreApplication.translate("Form", u"IR+EO", None))
        self.label_title_ir_sensor.setText(QCoreApplication.translate("Form", u"IR Image Sensor", None))
        self.radio_eo.setText(QCoreApplication.translate("Form", u"EO", None))
        self.radio_ir.setText(QCoreApplication.translate("Form", u"IR", None))
    # retranslateUi

