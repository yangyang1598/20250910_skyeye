# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialogIPecoI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(288, 146)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_title_login = QLabel(Dialog)
        self.label_title_login.setObjectName(u"label_title_login")
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\ub465\uadfc\ud5e4\ub4dc\ub77c\uc778"])
        font.setPointSize(15)
        self.label_title_login.setFont(font)

        self.gridLayout.addWidget(self.label_title_login, 0, 0, 1, 1)

        self.label_title_pw = QLabel(Dialog)
        self.label_title_pw.setObjectName(u"label_title_pw")

        self.gridLayout.addWidget(self.label_title_pw, 3, 0, 1, 1)

        self.label_title_id = QLabel(Dialog)
        self.label_title_id.setObjectName(u"label_title_id")

        self.gridLayout.addWidget(self.label_title_id, 2, 0, 1, 1)

        self.line_edit_pw = QLineEdit(Dialog)
        self.line_edit_pw.setObjectName(u"line_edit_pw")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_pw.sizePolicy().hasHeightForWidth())
        self.line_edit_pw.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.line_edit_pw, 3, 1, 1, 1)

        self.line_edit_id = QLineEdit(Dialog)
        self.line_edit_id.setObjectName(u"line_edit_id")
        sizePolicy.setHeightForWidth(self.line_edit_id.sizePolicy().hasHeightForWidth())
        self.line_edit_id.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.line_edit_id, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\ub85c\uadf8\uc778 \ucc3d", None))
        self.label_title_login.setText(QCoreApplication.translate("Dialog", u"\ub85c\uadf8\uc778 ", None))
        self.label_title_pw.setText(QCoreApplication.translate("Dialog", u"PW", None))
        self.label_title_id.setText(QCoreApplication.translate("Dialog", u"ID", None))
    # retranslateUi

