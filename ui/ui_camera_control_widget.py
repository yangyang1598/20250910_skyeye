# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_control_widgetbOcqNj.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(540, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(540, 300))
        Form.setAcceptDrops(False)
        Form.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    image: url(1.png);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(2.png);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton:pressed {\n"
"    /* \ub20c\ub838\uc744 \ub54c \ubc30\uacbd\uc0c9\uc744 \uc0b4\uc9dd \uc5b4\ub461\uac8c */\n"
"    background-color: darkgray;\n"
"    /* (\uc120\ud0dd \uc0ac\ud56d) \uc0b4\uc9dd \uc704\uce58\ub97c \uc774\ub3d9\uc2dc\ucf1c \ub20c\ub9ac\ub294 \ub4ef\ud55c \uc785\uccb4\uac10 \uc8fc\uae30 */\n"
"    padding-top: 2px;\n"
"    padding-left: 2px;\n"
"    /* (\uc120\ud0dd \uc0ac\ud56d) \ud14c\ub450\ub9ac\ub098 \uadf8\ub9bc\uc790 \ubcc0\ud654 */\n"
"    border: 1px solid black;\n"
"    box-shadow: inset 1px 1px 3px rgba(0,0,0,0.5); /* \uadf8\ub9bc\uc790 \uc548\ucabd\uc73c\ub85c */\n"
"}")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontal_slider_cam_speed = QSlider(Form)
        self.horizontal_slider_cam_speed.setObjectName(u"horizontal_slider_cam_speed")
        self.horizontal_slider_cam_speed.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontal_slider_cam_speed)

        self.label_cam_speed = QLabel(Form)
        self.label_cam_speed.setObjectName(u"label_cam_speed")

        self.horizontalLayout_2.addWidget(self.label_cam_speed)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_right_up = QPushButton(Form)
        self.button_right_up.setObjectName(u"button_right_up")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_right_up.sizePolicy().hasHeightForWidth())
        self.button_right_up.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.button_right_up.setFont(font1)

        self.gridLayout.addWidget(self.button_right_up, 1, 2, 1, 1)

        self.button_up = QPushButton(Form)
        self.button_up.setObjectName(u"button_up")
        sizePolicy1.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy1)
        self.button_up.setFont(font1)

        self.gridLayout.addWidget(self.button_up, 1, 1, 1, 1)

        self.button_left_down = QPushButton(Form)
        self.button_left_down.setObjectName(u"button_left_down")
        sizePolicy1.setHeightForWidth(self.button_left_down.sizePolicy().hasHeightForWidth())
        self.button_left_down.setSizePolicy(sizePolicy1)
        self.button_left_down.setFont(font1)

        self.gridLayout.addWidget(self.button_left_down, 4, 0, 1, 1)

        self.button_right = QPushButton(Form)
        self.button_right.setObjectName(u"button_right")
        sizePolicy1.setHeightForWidth(self.button_right.sizePolicy().hasHeightForWidth())
        self.button_right.setSizePolicy(sizePolicy1)
        self.button_right.setFont(font1)

        self.gridLayout.addWidget(self.button_right, 2, 2, 1, 1)

        self.button_left = QPushButton(Form)
        self.button_left.setObjectName(u"button_left")
        sizePolicy1.setHeightForWidth(self.button_left.sizePolicy().hasHeightForWidth())
        self.button_left.setSizePolicy(sizePolicy1)
        self.button_left.setFont(font1)

        self.gridLayout.addWidget(self.button_left, 2, 0, 1, 1)

        self.button_down = QPushButton(Form)
        self.button_down.setObjectName(u"button_down")
        sizePolicy1.setHeightForWidth(self.button_down.sizePolicy().hasHeightForWidth())
        self.button_down.setSizePolicy(sizePolicy1)
        self.button_down.setFont(font1)

        self.gridLayout.addWidget(self.button_down, 4, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 2, 3, 1, 1)

        self.button_left_up = QPushButton(Form)
        self.button_left_up.setObjectName(u"button_left_up")
        sizePolicy1.setHeightForWidth(self.button_left_up.sizePolicy().hasHeightForWidth())
        self.button_left_up.setSizePolicy(sizePolicy1)
        self.button_left_up.setFont(font1)

        self.gridLayout.addWidget(self.button_left_up, 1, 0, 1, 1)

        self.button_right_down = QPushButton(Form)
        self.button_right_down.setObjectName(u"button_right_down")
        sizePolicy1.setHeightForWidth(self.button_right_down.sizePolicy().hasHeightForWidth())
        self.button_right_down.setSizePolicy(sizePolicy1)
        self.button_right_down.setFont(font1)

        self.gridLayout.addWidget(self.button_right_down, 4, 2, 1, 1)

        self.button_home = QPushButton(Form)
        self.button_home.setObjectName(u"button_home")
        sizePolicy1.setHeightForWidth(self.button_home.sizePolicy().hasHeightForWidth())
        self.button_home.setSizePolicy(sizePolicy1)
        self.button_home.setFont(font1)

        self.gridLayout.addWidget(self.button_home, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_zoom_out = QPushButton(Form)
        self.button_zoom_out.setObjectName(u"button_zoom_out")
        sizePolicy1.setHeightForWidth(self.button_zoom_out.sizePolicy().hasHeightForWidth())
        self.button_zoom_out.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(20)
        self.button_zoom_out.setFont(font2)
        self.button_zoom_out.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-image: url(\"D:/Downloads/minus.png\");\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    /* \ubc84\ud2bc \ud06c\uae30 \uc124\uc815 */\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"}")

        self.horizontalLayout.addWidget(self.button_zoom_out)

        self.label_zoom = QLabel(Form)
        self.label_zoom.setObjectName(u"label_zoom")
        sizePolicy1.setHeightForWidth(self.label_zoom.sizePolicy().hasHeightForWidth())
        self.label_zoom.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(16)
        self.label_zoom.setFont(font3)
        self.label_zoom.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_zoom)

        self.button_zoom_in = QPushButton(Form)
        self.button_zoom_in.setObjectName(u"button_zoom_in")
        sizePolicy1.setHeightForWidth(self.button_zoom_in.sizePolicy().hasHeightForWidth())
        self.button_zoom_in.setSizePolicy(sizePolicy1)
        self.button_zoom_in.setFont(font2)
        self.button_zoom_in.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-image: url(\"D:/Downloads/plus.png\");\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    /* \ubc84\ud2bc \ud06c\uae30 \uc124\uc815 */\n"
"    min-width: 50px;\n"
"    min-height: 50px;\n"
"}")

        self.horizontalLayout.addWidget(self.button_zoom_in)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_active_follow_yaw = QLabel(Form)
        self.label_active_follow_yaw.setObjectName(u"label_active_follow_yaw")
        sizePolicy1.setHeightForWidth(self.label_active_follow_yaw.sizePolicy().hasHeightForWidth())
        self.label_active_follow_yaw.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_active_follow_yaw.setFont(font4)
        self.label_active_follow_yaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_active_follow_yaw)

        self.toggle_active_follow_yaw = QPushButton(Form)
        self.toggle_active_follow_yaw.setObjectName(u"toggle_active_follow_yaw")
        sizePolicy.setHeightForWidth(self.toggle_active_follow_yaw.sizePolicy().hasHeightForWidth())
        self.toggle_active_follow_yaw.setSizePolicy(sizePolicy)
        self.toggle_active_follow_yaw.setMaximumSize(QSize(150, 58))
        font5 = QFont()
        font5.setPointSize(50)
        self.toggle_active_follow_yaw.setFont(font5)
        self.toggle_active_follow_yaw.setAutoFillBackground(False)
        self.toggle_active_follow_yaw.setStyleSheet(u"QPushButton:checked {\n"
"    border: none;\n"
"    image: url(\"D:/Downloads/switch-on.png\");\n"
"}\n"
"QPushButton:!checked {\n"
"    border: none;\n"
"    image: url(\"D:/Downloads/switch-off.png\");\n"
"}")
        self.toggle_active_follow_yaw.setIconSize(QSize(50, 50))
        self.toggle_active_follow_yaw.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.toggle_active_follow_yaw)

        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_active_motor = QLabel(Form)
        self.label_active_motor.setObjectName(u"label_active_motor")
        sizePolicy1.setHeightForWidth(self.label_active_motor.sizePolicy().hasHeightForWidth())
        self.label_active_motor.setSizePolicy(sizePolicy1)
        self.label_active_motor.setFont(font4)
        self.label_active_motor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_active_motor)

        self.toggle_active_motor = QPushButton(Form)
        self.toggle_active_motor.setObjectName(u"toggle_active_motor")
        sizePolicy.setHeightForWidth(self.toggle_active_motor.sizePolicy().hasHeightForWidth())
        self.toggle_active_motor.setSizePolicy(sizePolicy)
        self.toggle_active_motor.setMaximumSize(QSize(150, 58))
        self.toggle_active_motor.setFont(font5)
        self.toggle_active_motor.setAutoFillBackground(False)
        self.toggle_active_motor.setStyleSheet(u"QPushButton:checked {\n"
"    border: none;\n"
"    image: url(\"D:/Downloads/switch-on.png\");\n"
"}\n"
"QPushButton:!checked {\n"
"    border: none;\n"
"    image: url(\"D:/Downloads/switch-off.png\");\n"
"}")
        self.toggle_active_motor.setIconSize(QSize(50, 50))
        self.toggle_active_motor.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.toggle_active_motor)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_active_osd = QLabel(Form)
        self.label_active_osd.setObjectName(u"label_active_osd")
        sizePolicy1.setHeightForWidth(self.label_active_osd.sizePolicy().hasHeightForWidth())
        self.label_active_osd.setSizePolicy(sizePolicy1)
        self.label_active_osd.setFont(font4)
        self.label_active_osd.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_active_osd)

        self.toggle_active_osd = QPushButton(Form)
        self.toggle_active_osd.setObjectName(u"toggle_active_osd")
        sizePolicy.setHeightForWidth(self.toggle_active_osd.sizePolicy().hasHeightForWidth())
        self.toggle_active_osd.setSizePolicy(sizePolicy)
        self.toggle_active_osd.setMaximumSize(QSize(150, 58))
        self.toggle_active_osd.setFont(font5)
        self.toggle_active_osd.setAutoFillBackground(False)
        self.toggle_active_osd.setStyleSheet(u"QPushButton:checked {\n"
"    border: none;\n"
"    image: url(\"D:/Downloads/switch-on.png\");\n"
"}\n"
"QPushButton:!checked {\n"
"    border: none;\n"
"    image: url(\"D:/Downloads/switch-off.png\");\n"
"}")
        self.toggle_active_osd.setIconSize(QSize(50, 50))
        self.toggle_active_osd.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.toggle_active_osd)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\uce74\uba54\ub77c \uc81c\uc5b4", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uce74\uba54\ub77c \uc774\ub3d9\uc18d\ub3c4", None))
        self.label_cam_speed.setText(QCoreApplication.translate("Form", u"100", None))
        self.button_right_up.setText(QCoreApplication.translate("Form", u"\u2197", None))
        self.button_up.setText(QCoreApplication.translate("Form", u"\u2191", None))
        self.button_left_down.setText(QCoreApplication.translate("Form", u"\u2199", None))
        self.button_right.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.button_left.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.button_down.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.button_left_up.setText(QCoreApplication.translate("Form", u"\u2196", None))
        self.button_right_down.setText(QCoreApplication.translate("Form", u"\u2198", None))
        self.button_home.setText(QCoreApplication.translate("Form", u"HOME", None))
        self.button_zoom_out.setText("")
        self.label_zoom.setText(QCoreApplication.translate("Form", u"\uc90c", None))
        self.button_zoom_in.setText("")
        self.label_active_follow_yaw.setText(QCoreApplication.translate("Form", u"Follow Yaw", None))
        self.toggle_active_follow_yaw.setText("")
        self.label_active_motor.setText(QCoreApplication.translate("Form", u"\ubaa8\ud130", None))
        self.toggle_active_motor.setText("")
        self.label_active_osd.setText(QCoreApplication.translate("Form", u"\uba54\ub274(OSD)", None))
        self.toggle_active_osd.setText("")
    # retranslateUi

