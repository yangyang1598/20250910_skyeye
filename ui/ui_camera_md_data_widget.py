# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_md_data_widgetEkvalr.ui'
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
        self.label_data_md_roll = QLabel(Form)
        self.label_data_md_roll.setObjectName(u"label_data_md_roll")
        self.label_data_md_roll.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_md_roll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_md_roll, 14, 1, 1, 1)

        self.label_title_md_location = QLabel(Form)
        self.label_title_md_location.setObjectName(u"label_title_md_location")
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\ub465\uadfc\ud5e4\ub4dc\ub77c\uc778"])
        font.setPointSize(22)
        self.label_title_md_location.setFont(font)

        self.gridLayout.addWidget(self.label_title_md_location, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.label_title_cam_pitch = QLabel(Form)
        self.label_title_cam_pitch.setObjectName(u"label_title_cam_pitch")

        self.gridLayout.addWidget(self.label_title_cam_pitch, 6, 0, 1, 1)

        self.label_title_title_md = QLabel(Form)
        self.label_title_title_md.setObjectName(u"label_title_title_md")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_title_title_md.setFont(font1)

        self.gridLayout.addWidget(self.label_title_title_md, 9, 0, 1, 1)

        self.label_data_cam_roll = QLabel(Form)
        self.label_data_cam_roll.setObjectName(u"label_data_cam_roll")
        self.label_data_cam_roll.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_cam_roll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_cam_roll, 5, 1, 1, 1)

        self.label_title_degree_6 = QLabel(Form)
        self.label_title_degree_6.setObjectName(u"label_title_degree_6")

        self.gridLayout.addWidget(self.label_title_degree_6, 10, 2, 1, 1)

        self.label_title_degree_7 = QLabel(Form)
        self.label_title_degree_7.setObjectName(u"label_title_degree_7")

        self.gridLayout.addWidget(self.label_title_degree_7, 11, 2, 1, 1)

        self.label_data_cam_zoom = QLabel(Form)
        self.label_data_cam_zoom.setObjectName(u"label_data_cam_zoom")
        self.label_data_cam_zoom.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_cam_zoom.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_cam_zoom, 3, 1, 1, 1)

        self.label_title_md_yaw = QLabel(Form)
        self.label_title_md_yaw.setObjectName(u"label_title_md_yaw")

        self.gridLayout.addWidget(self.label_title_md_yaw, 16, 0, 1, 1)

        self.label_title_degree_10 = QLabel(Form)
        self.label_title_degree_10.setObjectName(u"label_title_degree_10")

        self.gridLayout.addWidget(self.label_title_degree_10, 16, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.label_title_degree_8 = QLabel(Form)
        self.label_title_degree_8.setObjectName(u"label_title_degree_8")

        self.gridLayout.addWidget(self.label_title_degree_8, 14, 2, 1, 1)

        self.label_title_cam_zoom = QLabel(Form)
        self.label_title_cam_zoom.setObjectName(u"label_title_cam_zoom")

        self.gridLayout.addWidget(self.label_title_cam_zoom, 3, 0, 1, 1)

        self.label_title_md_pitch = QLabel(Form)
        self.label_title_md_pitch.setObjectName(u"label_title_md_pitch")

        self.gridLayout.addWidget(self.label_title_md_pitch, 15, 0, 1, 1)

        self.label_data_cam_yaw = QLabel(Form)
        self.label_data_cam_yaw.setObjectName(u"label_data_cam_yaw")
        self.label_data_cam_yaw.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_cam_yaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_cam_yaw, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.label_title_degree_9 = QLabel(Form)
        self.label_title_degree_9.setObjectName(u"label_title_degree_9")

        self.gridLayout.addWidget(self.label_title_degree_9, 15, 2, 1, 1)

        self.label_data_cam_pitch = QLabel(Form)
        self.label_data_cam_pitch.setObjectName(u"label_data_cam_pitch")
        self.label_data_cam_pitch.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_cam_pitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_cam_pitch, 6, 1, 1, 1)

        self.label_title_degree_3 = QLabel(Form)
        self.label_title_degree_3.setObjectName(u"label_title_degree_3")

        self.gridLayout.addWidget(self.label_title_degree_3, 5, 2, 1, 1)

        self.label_title_degree_4 = QLabel(Form)
        self.label_title_degree_4.setObjectName(u"label_title_degree_4")

        self.gridLayout.addWidget(self.label_title_degree_4, 6, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 13, 0, 1, 1)

        self.label_title_cam_yaw = QLabel(Form)
        self.label_title_cam_yaw.setObjectName(u"label_title_cam_yaw")

        self.gridLayout.addWidget(self.label_title_cam_yaw, 7, 0, 1, 1)

        self.label_data_md_alt = QLabel(Form)
        self.label_data_md_alt.setObjectName(u"label_data_md_alt")
        self.label_data_md_alt.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_md_alt.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_md_alt, 12, 1, 1, 1)

        self.label_title_meter = QLabel(Form)
        self.label_title_meter.setObjectName(u"label_title_meter")

        self.gridLayout.addWidget(self.label_title_meter, 12, 2, 1, 1)

        self.label_title_cam_roll = QLabel(Form)
        self.label_title_cam_roll.setObjectName(u"label_title_cam_roll")

        self.gridLayout.addWidget(self.label_title_cam_roll, 5, 0, 1, 1)

        self.label_data_md_lng = QLabel(Form)
        self.label_data_md_lng.setObjectName(u"label_data_md_lng")
        self.label_data_md_lng.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_md_lng.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_md_lng, 11, 1, 1, 1)

        self.label_title_md_lat = QLabel(Form)
        self.label_title_md_lat.setObjectName(u"label_title_md_lat")

        self.gridLayout.addWidget(self.label_title_md_lat, 10, 0, 1, 1)

        self.label_data_md_lat = QLabel(Form)
        self.label_data_md_lat.setObjectName(u"label_data_md_lat")
        self.label_data_md_lat.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_md_lat.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_md_lat, 10, 1, 1, 1)

        self.label_title_degree_5 = QLabel(Form)
        self.label_title_degree_5.setObjectName(u"label_title_degree_5")

        self.gridLayout.addWidget(self.label_title_degree_5, 7, 2, 1, 1)

        self.label_title_md_alt = QLabel(Form)
        self.label_title_md_alt.setObjectName(u"label_title_md_alt")

        self.gridLayout.addWidget(self.label_title_md_alt, 12, 0, 1, 1)

        self.label_title_title_camera = QLabel(Form)
        self.label_title_title_camera.setObjectName(u"label_title_title_camera")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        self.label_title_title_camera.setFont(font2)

        self.gridLayout.addWidget(self.label_title_title_camera, 2, 0, 1, 1)

        self.label_title_md_roll = QLabel(Form)
        self.label_title_md_roll.setObjectName(u"label_title_md_roll")

        self.gridLayout.addWidget(self.label_title_md_roll, 14, 0, 1, 1)

        self.label_title_fold = QLabel(Form)
        self.label_title_fold.setObjectName(u"label_title_fold")

        self.gridLayout.addWidget(self.label_title_fold, 3, 2, 1, 1)

        self.label_data_md_pitch = QLabel(Form)
        self.label_data_md_pitch.setObjectName(u"label_data_md_pitch")
        self.label_data_md_pitch.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_md_pitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_md_pitch, 15, 1, 1, 1)

        self.label_data_md_yaw = QLabel(Form)
        self.label_data_md_yaw.setObjectName(u"label_data_md_yaw")
        self.label_data_md_yaw.setInputMethodHints(Qt.InputMethodHint.ImhNoTextHandles)
        self.label_data_md_yaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_data_md_yaw, 16, 1, 1, 1)

        self.label_title_md_lng = QLabel(Form)
        self.label_title_md_lng.setObjectName(u"label_title_md_lng")

        self.gridLayout.addWidget(self.label_title_md_lng, 11, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_data_md_roll.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_md_location.setText(QCoreApplication.translate("Form", u"\uc911\uad6c", None))
        self.label_title_cam_pitch.setText(QCoreApplication.translate("Form", u"Y\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Pitch)", None))
        self.label_title_title_md.setText(QCoreApplication.translate("Form", u"\uc784\ubb34\uc7a5\ube44 \ub370\uc774\ud130", None))
        self.label_data_cam_roll.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_degree_6.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_title_degree_7.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_data_cam_zoom.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_title_md_yaw.setText(QCoreApplication.translate("Form", u"Z\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Yaw)", None))
        self.label_title_degree_10.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_title_degree_8.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_title_cam_zoom.setText(QCoreApplication.translate("Form", u"\uc90c", None))
        self.label_title_md_pitch.setText(QCoreApplication.translate("Form", u"Y\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Pitch)", None))
        self.label_data_cam_yaw.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_degree_9.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_data_cam_pitch.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_degree_3.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_title_degree_4.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_title_cam_yaw.setText(QCoreApplication.translate("Form", u"Z\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Yaw)", None))
        self.label_data_md_alt.setText(QCoreApplication.translate("Form", u"3.5", None))
        self.label_title_meter.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_title_cam_roll.setText(QCoreApplication.translate("Form", u"X\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Roll)", None))
        self.label_data_md_lng.setText(QCoreApplication.translate("Form", u"129.36272847732522", None))
        self.label_title_md_lat.setText(QCoreApplication.translate("Form", u"\uc704\ub3c4", None))
        self.label_data_md_lat.setText(QCoreApplication.translate("Form", u" 35.650472602503896", None))
        self.label_title_degree_5.setText(QCoreApplication.translate("Form", u"\u00ba", None))
        self.label_title_md_alt.setText(QCoreApplication.translate("Form", u"\uace0\ub3c4", None))
        self.label_title_title_camera.setText(QCoreApplication.translate("Form", u"\uce74\uba54\ub77c \ub370\uc774\ud130", None))
        self.label_title_md_roll.setText(QCoreApplication.translate("Form", u"X\ucd95 \uae30\uc900 \ud68c\uc804 \ubc18\uacbd(Roll)", None))
        self.label_title_fold.setText(QCoreApplication.translate("Form", u"\ubc30", None))
        self.label_data_md_pitch.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_data_md_yaw.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_title_md_lng.setText(QCoreApplication.translate("Form", u"\uacbd\ub3c4", None))
    # retranslateUi

