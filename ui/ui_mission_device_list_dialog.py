# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mission_device_list_dialogNrsBhN.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 126)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(400, 200))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_mission_device_title = QLabel(Dialog)
        self.label_mission_device_title.setObjectName(u"label_mission_device_title")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_mission_device_title.setFont(font)

        self.verticalLayout.addWidget(self.label_mission_device_title)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.combo_mission_device_list = QComboBox(Dialog)
        self.combo_mission_device_list.addItem("")
        self.combo_mission_device_list.addItem("")
        self.combo_mission_device_list.addItem("")
        self.combo_mission_device_list.addItem("")
        self.combo_mission_device_list.setObjectName(u"combo_mission_device_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_mission_device_list.sizePolicy().hasHeightForWidth())
        self.combo_mission_device_list.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.combo_mission_device_list.setFont(font1)

        self.verticalLayout.addWidget(self.combo_mission_device_list)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\uc784\ubb34\uc7a5\ube44 \ubaa9\ub85d", None))
        self.label_mission_device_title.setText(QCoreApplication.translate("Dialog", u"\uc784\ubb34\uc7a5\ube44 \ubaa9\ub85d", None))
        self.combo_mission_device_list.setItemText(0, QCoreApplication.translate("Dialog", u"\uae38\ucc9c", None))
        self.combo_mission_device_list.setItemText(1, QCoreApplication.translate("Dialog", u"\uc6b8\uc0b0 \uc911\uad6c", None))
        self.combo_mission_device_list.setItemText(2, QCoreApplication.translate("Dialog", u"\uc6b8\uc0b0 \ub0a8\uad6c", None))
        self.combo_mission_device_list.setItemText(3, QCoreApplication.translate("Dialog", u"\uc6b8\uc0b0 \ud2b9\uad6c(\ub300\uc6b4\uc0b0)", None))

    # retranslateUi

