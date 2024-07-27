# Created by: PyQt6 UI code generator 6.7.0
from PyQt6 import QtCore, QtGui, QtWidgets
from kanasouphtml import resource_path


class Ui_kana2epub(object):
    def setupUi(self, kana2epub):
        kana2epub.setObjectName("kana2epub")
        kana2epub.resize(651, 378)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(kana2epub.sizePolicy().hasHeightForWidth())
        kana2epub.setSizePolicy(sizePolicy)
        kana2epub.setMinimumSize(QtCore.QSize(651, 378))
        kana2epub.setMaximumSize(QtCore.QSize(651, 378))
        kana2epub.setStyleSheet("border-radius: 5px;")
        self.img_label = QtWidgets.QLabel(parent=kana2epub)
        self.img_label.setGeometry(QtCore.QRect(0, 0, 651, 378))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_label.sizePolicy().hasHeightForWidth())
        self.img_label.setSizePolicy(sizePolicy)
        self.img_label.setMinimumSize(QtCore.QSize(651, 378))
        self.img_label.setMaximumSize(QtCore.QSize(651, 378))
        self.img_label.setStyleSheet("border-redius:5px;")
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(resource_path("./src/wallpaper.png")))
        self.img_label.setScaledContents(True)
        self.img_label.setObjectName("img_label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 40, 160, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 1px;\n"
"            background-color: rgba(45, 26, 255, 20);\n"
"            color:rgb(86, 86, 86);}\n"
"        QPushButton:hover{\n"
"            background-color: rgba(45, 26, 255, 100);}\n"
"        QPushButton:pressed{\n"
"            background-color: rgba(205, 10, 155, 100);}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 40, 160, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 1px;\n"
"            background-color: rgba(45, 26, 255, 20);\n"
"            color:rgb(86, 86, 86);}\n"
"        QPushButton:hover{\n"
"            background-color: rgba(45, 26, 255, 100);}\n"
"        QPushButton:pressed{\n"
"            background-color: rgba(205, 10, 155, 100);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton.setGeometry(QtCore.QRect(170, 40, 160, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 1px;\n"
"            background-color: rgba(45, 26, 255, 20);\n"
"            color:rgb(86, 86, 86);}\n"
"        QPushButton:hover{\n"
"            background-color: rgba(45, 26, 255, 100);}\n"
"        QPushButton:pressed{\n"
"            background-color: rgba(205, 10, 155, 100);}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 290, 251, 61))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 1px;\n"
"            background-color: rgba(45, 26, 255, 20);\n"
"            color:rgb(86, 86, 86);}\n"
"        QPushButton:hover{\n"
"            background-color: rgba(45, 26, 255, 100);}\n"
"        QPushButton:pressed{\n"
"            background-color: rgba(205, 10, 155, 100);}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_5.setGeometry(QtCore.QRect(586, 10, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 8px;\n"
"            background-color: rgba(255, 255,0, 255);}QPushButton:hover{\n"
"            background-color: rgba(205, 205, 15, 200);}\n"
"QPushButton:pressed{\n"
"            background-color: rgba(205, 205, 15, 255);}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 10, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 8px;\n"
"            background-color: rgba(255, 0, 0, 255);}\n"
"QPushButton:hover{\n"
"            background-color: rgba(220, 0, 15, 180);}\n"
"QPushButton:pressed{\n"
"            background-color: rgba(240, 0, 15, 170);}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 40, 170, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,100);\n"
"            border-radius: 1px;\n"
"            background-color: rgba(45, 26, 255, 20);\n"
"            color:rgb(86, 86, 86);}\n"
"        QPushButton:hover{\n"
"            background-color: rgba(45, 26, 255, 100);}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox = QtWidgets.QCheckBox(parent=kana2epub)
        self.checkBox.setGeometry(QtCore.QRect(20, 290, 301, 26))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        #######################################################
        self.checkBox.setStyleSheet("color: rgb(255,255,255)")
        self.lineEdit = QtWidgets.QLineEdit(parent=kana2epub)
        self.lineEdit.setGeometry(QtCore.QRect(19, 320, 311, 21))
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=kana2epub)
        self.label.setGeometry(QtCore.QRect(10, 356, 631, 20))
        self.label.setObjectName("label")
        #####################################################
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2 = QtWidgets.QLabel(parent=kana2epub)
        self.label_2.setGeometry(QtCore.QRect(92, 114, 421, 41))  # 140
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        ###########################################################
        self.label_2.setStyleSheet("color:rgba(231, 46, 255, 255)")  # rgba(231, 46, 255, 232)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=kana2epub)
        self.label_3.setGeometry(QtCore.QRect(142, 154, 611, 31))  # 190
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        ###########################################################
        self.label_3.setStyleSheet("color:rgba(231, 46, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(parent=kana2epub)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 320, 23, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,0);\n"
"            border-radius: 4px;\n"
"            background-color: rgba(0, 0, 0, 0);}\n"
"QPushButton:hover{\n"
"            background-color:rgba(255, 247, 24, 120);}\n"
"QPushButton:pressed{\n"
"            background-color: rgba(240, 0, 15, 170);}")
        self.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("./src/open_folder_file_icon_219486.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setAutoRepeat(False)
        self.pushButton_8.setAutoExclusive(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.widget = QtWidgets.QWidget(parent=kana2epub)
        self.widget.setGeometry(QtCore.QRect(10, 10, 571, 20))
        self.widget.setObjectName("widget")

        self.retranslateUi(kana2epub)
        QtCore.QMetaObject.connectSlotsByName(kana2epub)

        self.shima_rabel = QtWidgets.QLabel(parent = kana2epub)
        self.shima_rabel.setGeometry(QtCore.QRect(480, 209, 571, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.shima_rabel.setFont(font)
        self.shima_rabel.setText("——しまむら")
        self.shima_rabel.setStyleSheet("color: rgb(4, 245, 245)")


    def retranslateUi(self, kana2epub):
        _translate = QtCore.QCoreApplication.translate
        kana2epub.setWindowTitle(_translate("kana2epub", "Form"))
        self.pushButton_3.setText(_translate("kana2epub", "日本語"))
        self.pushButton_2.setText(_translate("kana2epub", "English"))
        self.pushButton.setText(_translate("kana2epub", "中 文"))
        self.pushButton_6.setText("KANA2EPUB")
        self.pushButton_7.setText(_translate("kana2epub", "Language"))
        self.checkBox.setText("customize the output path")
        self.label.setText("status bar： please push the kana2epub button to select epub files")
        self.label_2.setText("誰か を 好き になるって、唐突 なことなのだ。")  # "あなたとはうんめーてきなものを感じますね。"
        self.label_3.setText("多分、計算 とか、妥協 とか、挟まる 余地 がない。")  # "多分、わたしはあなたと会うために生まれてきたのだと思いますよ。"