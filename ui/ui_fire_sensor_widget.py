# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fire_sensor_widgetDLgJAF.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(317, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(350, 660))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_data_sensor_temp = QLabel(Form)
        self.label_data_sensor_temp.setObjectName(u"label_data_sensor_temp")
        self.label_data_sensor_temp.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_temp.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_temp, 2, 1, 1, 1)

        self.label_title_sensor_flags = QLabel(Form)
        self.label_title_sensor_flags.setObjectName(u"label_title_sensor_flags")

        self.gridLayout.addWidget(self.label_title_sensor_flags, 8, 0, 1, 1)

        self.label_data_sensor_pressure = QLabel(Form)
        self.label_data_sensor_pressure.setObjectName(u"label_data_sensor_pressure")
        self.label_data_sensor_pressure.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_pressure.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_pressure, 4, 1, 1, 1)

        self.label_data_sensor_gas_index = QLabel(Form)
        self.label_data_sensor_gas_index.setObjectName(u"label_data_sensor_gas_index")
        self.label_data_sensor_gas_index.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_gas_index.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_gas_index, 5, 1, 1, 1)

        self.label_data_sensor_rh = QLabel(Form)
        self.label_data_sensor_rh.setObjectName(u"label_data_sensor_rh")
        self.label_data_sensor_rh.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_rh.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_rh, 3, 1, 1, 1)

        self.label_title_sensor_temp = QLabel(Form)
        self.label_title_sensor_temp.setObjectName(u"label_title_sensor_temp")

        self.gridLayout.addWidget(self.label_title_sensor_temp, 2, 0, 1, 1)

        self.label_title_sensor_gas_index = QLabel(Form)
        self.label_title_sensor_gas_index.setObjectName(u"label_title_sensor_gas_index")

        self.gridLayout.addWidget(self.label_title_sensor_gas_index, 5, 0, 1, 1)

        self.label_title_sensor_rh = QLabel(Form)
        self.label_title_sensor_rh.setObjectName(u"label_title_sensor_rh")

        self.gridLayout.addWidget(self.label_title_sensor_rh, 3, 0, 1, 1)

        self.label_title_sensor_pressure = QLabel(Form)
        self.label_title_sensor_pressure.setObjectName(u"label_title_sensor_pressure")

        self.gridLayout.addWidget(self.label_title_sensor_pressure, 4, 0, 1, 1)

        self.label_title_sensor_checksum = QLabel(Form)
        self.label_title_sensor_checksum.setObjectName(u"label_title_sensor_checksum")

        self.gridLayout.addWidget(self.label_title_sensor_checksum, 9, 0, 1, 1)

        self.label_data_sensor_vcap = QLabel(Form)
        self.label_data_sensor_vcap.setObjectName(u"label_data_sensor_vcap")
        self.label_data_sensor_vcap.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_vcap.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_vcap, 7, 1, 1, 1)

        self.label_title_mV = QLabel(Form)
        self.label_title_mV.setObjectName(u"label_title_mV")

        self.gridLayout.addWidget(self.label_title_mV, 7, 2, 1, 1)

        self.label_data_sensor_trend = QLabel(Form)
        self.label_data_sensor_trend.setObjectName(u"label_data_sensor_trend")
        self.label_data_sensor_trend.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_trend.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_trend, 6, 1, 1, 1)

        self.label_data_sensor_checksum = QLabel(Form)
        self.label_data_sensor_checksum.setObjectName(u"label_data_sensor_checksum")
        self.label_data_sensor_checksum.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_checksum.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_checksum, 9, 1, 1, 1)

        self.label_title_degree_3 = QLabel(Form)
        self.label_title_degree_3.setObjectName(u"label_title_degree_3")

        self.gridLayout.addWidget(self.label_title_degree_3, 2, 2, 1, 1)

        self.label_data_sensor_flags = QLabel(Form)
        self.label_data_sensor_flags.setObjectName(u"label_data_sensor_flags")
        self.label_data_sensor_flags.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_sensor_flags.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_sensor_flags, 8, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.label_title_sensor_trend = QLabel(Form)
        self.label_title_sensor_trend.setObjectName(u"label_title_sensor_trend")

        self.gridLayout.addWidget(self.label_title_sensor_trend, 6, 0, 1, 1)

        self.label_title_hPa = QLabel(Form)
        self.label_title_hPa.setObjectName(u"label_title_hPa")

        self.gridLayout.addWidget(self.label_title_hPa, 4, 2, 1, 1)

        self.label_title_md_location = QLabel(Form)
        self.label_title_md_location.setObjectName(u"label_title_md_location")
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\ub465\uadfc\ud5e4\ub4dc\ub77c\uc778"])
        font.setPointSize(15)
        self.label_title_md_location.setFont(font)

        self.gridLayout.addWidget(self.label_title_md_location, 0, 0, 1, 1)

        self.label_title_sensor_vcap = QLabel(Form)
        self.label_title_sensor_vcap.setObjectName(u"label_title_sensor_vcap")

        self.gridLayout.addWidget(self.label_title_sensor_vcap, 7, 0, 1, 1)

        self.label_title_percent_4 = QLabel(Form)
        self.label_title_percent_4.setObjectName(u"label_title_percent_4")

        self.gridLayout.addWidget(self.label_title_percent_4, 3, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_data_sensor_temp.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_sensor_flags.setText(QCoreApplication.translate("Form", u"\uc0c1\ud0dc \ud50c\ub798\uadf8", None))
        self.label_data_sensor_pressure.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_data_sensor_gas_index.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_data_sensor_rh.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_sensor_temp.setText(QCoreApplication.translate("Form", u"\uc628\ub3c4(\uc12d\uc528)", None))
        self.label_title_sensor_gas_index.setText(QCoreApplication.translate("Form", u"\uac00\uc2a4\uc9c0\uc218 ", None))
        self.label_title_sensor_rh.setText(QCoreApplication.translate("Form", u"\uc0c1\ub300 \uc2b5\ub3c4", None))
        self.label_title_sensor_pressure.setText(QCoreApplication.translate("Form", u"\uae30\uc555", None))
        self.label_title_sensor_checksum.setText(QCoreApplication.translate("Form", u"\uccb4\ud06c\uc12c", None))
        self.label_data_sensor_vcap.setText(QCoreApplication.translate("Form", u"3.5", None))
        self.label_title_mV.setText(QCoreApplication.translate("Form", u"mV", None))
        self.label_data_sensor_trend.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_data_sensor_checksum.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_degree_3.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_data_sensor_flags.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_title_sensor_trend.setText(QCoreApplication.translate("Form", u"\uac00\uc2a4 \uc0c1\uc2b9 \ud50c\ub798\uadf8", None))
        self.label_title_hPa.setText(QCoreApplication.translate("Form", u"hPa", None))
        self.label_title_md_location.setText(QCoreApplication.translate("Form", u"\uc0b0\ubd88\uac10\uc9c0 \uc13c\uc11c", None))
        self.label_title_sensor_vcap.setText(QCoreApplication.translate("Form", u"\ubc30\ud130\ub9ac \uc804\uc555", None))
        self.label_title_percent_4.setText(QCoreApplication.translate("Form", u"%", None))
    # retranslateUi

