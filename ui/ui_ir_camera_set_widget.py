# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ir_camera_set_widgetfYxSSp.ui'
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
        self.radio_blackHot = QRadioButton(Form)
        self.radio_blackHot.setObjectName(u"radio_blackHot")

        self.gridLayout.addWidget(self.radio_blackHot, 1, 1, 1, 1)

        self.radio_rainbow = QRadioButton(Form)
        self.radio_rainbow.setObjectName(u"radio_rainbow")

        self.gridLayout.addWidget(self.radio_rainbow, 3, 1, 1, 1)

        self.radio_hotIron = QRadioButton(Form)
        self.radio_hotIron.setObjectName(u"radio_hotIron")

        self.gridLayout.addWidget(self.radio_hotIron, 4, 1, 1, 1)

        self.radio_rainbowHc = QRadioButton(Form)
        self.radio_rainbowHc.setObjectName(u"radio_rainbowHc")

        self.gridLayout.addWidget(self.radio_rainbowHc, 3, 0, 1, 1)

        self.radio_whiteHot = QRadioButton(Form)
        self.radio_whiteHot.setObjectName(u"radio_whiteHot")

        self.gridLayout.addWidget(self.radio_whiteHot, 1, 0, 1, 1)

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

        self.radio_redHot = QRadioButton(Form)
        self.radio_redHot.setObjectName(u"radio_redHot")

        self.gridLayout.addWidget(self.radio_redHot, 2, 0, 1, 1)

        self.radio_arctic = QRadioButton(Form)
        self.radio_arctic.setObjectName(u"radio_arctic")

        self.gridLayout.addWidget(self.radio_arctic, 5, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radio_eo_ir_pip = QRadioButton(Form)
        self.radio_eo_ir_pip.setObjectName(u"radio_eo_ir_pip")

        self.gridLayout_2.addWidget(self.radio_eo_ir_pip, 2, 0, 1, 1)

        self.radio_ir_eo_pip = QRadioButton(Form)
        self.radio_ir_eo_pip.setObjectName(u"radio_ir_eo_pip")

        self.gridLayout_2.addWidget(self.radio_ir_eo_pip, 2, 1, 1, 1)

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
        self.radio_blackHot.setText(QCoreApplication.translate("Form", u"Black Hot", None))
        self.radio_rainbow.setText(QCoreApplication.translate("Form", u"Rainbow", None))
        self.radio_hotIron.setText(QCoreApplication.translate("Form", u"Hot Iron", None))
        self.radio_rainbowHc.setText(QCoreApplication.translate("Form", u"Rainbow HC", None))
        self.radio_whiteHot.setText(QCoreApplication.translate("Form", u"White Hot", None))
        self.radio_ironbow.setText(QCoreApplication.translate("Form", u"Ironbow", None))
        self.radio_lava.setText(QCoreApplication.translate("Form", u"Lava", None))
        self.label_title_ir_color_palette.setText(QCoreApplication.translate("Form", u"IR Color Palette", None))
        self.radio_redHot.setText(QCoreApplication.translate("Form", u"Red Hot", None))
        self.radio_arctic.setText(QCoreApplication.translate("Form", u"Arctic", None))
        self.radio_eo_ir_pip.setText(QCoreApplication.translate("Form", u"EO+IR", None))
        self.radio_ir_eo_pip.setText(QCoreApplication.translate("Form", u"IR+EO", None))
        self.label_title_ir_sensor.setText(QCoreApplication.translate("Form", u"IR Image Sensor", None))
        self.radio_eo.setText(QCoreApplication.translate("Form", u"EO", None))
        self.radio_ir.setText(QCoreApplication.translate("Form", u"IR", None))
    # retranslateUi

