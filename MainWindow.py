# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("background-color: #c8c8c8;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 500, 661, 181))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(550, 90, 21, 31))
        self.label_10.setObjectName("label_10")
        self.PhiFirstLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PhiFirstLineEdit.setGeometry(QtCore.QRect(580, 90, 61, 31))
        self.PhiFirstLineEdit.setInputMask("")
        self.PhiFirstLineEdit.setObjectName("PhiFirstLineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 90, 81, 31))
        self.label_4.setObjectName("label_4")
        self.PhiZeroLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PhiZeroLineEdit.setGeometry(QtCore.QRect(580, 40, 61, 31))
        self.PhiZeroLineEdit.setObjectName("PhiZeroLineEdit")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(420, 40, 21, 31))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.label_2.setObjectName("label_2")
        self.PsiFirtsLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PsiFirtsLineEdit.setGeometry(QtCore.QRect(450, 90, 61, 31))
        self.PsiFirtsLineEdit.setObjectName("PsiFirtsLineEdit")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(420, 140, 21, 31))
        self.label_7.setObjectName("label_7")
        self.LengthStepLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.LengthStepLineEdit.setGeometry(QtCore.QRect(270, 40, 61, 31))
        self.LengthStepLineEdit.setObjectName("LengthStepLineEdit")
        self.PsiZeroLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PsiZeroLineEdit.setGeometry(QtCore.QRect(450, 40, 61, 31))
        self.PsiZeroLineEdit.setObjectName("PsiZeroLineEdit")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(420, 90, 21, 31))
        self.label_6.setObjectName("label_6")
        self.StringLengthLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.StringLengthLineEdit.setGeometry(QtCore.QRect(90, 40, 61, 31))
        self.StringLengthLineEdit.setObjectName("StringLengthLineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label.setObjectName("label")
        self.TimeLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.TimeLineEdit.setGeometry(QtCore.QRect(90, 90, 61, 31))
        self.TimeLineEdit.setObjectName("TimeLineEdit")
        self.TimeStepLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.TimeStepLineEdit.setGeometry(QtCore.QRect(270, 90, 61, 31))
        self.TimeStepLineEdit.setObjectName("TimeStepLineEdit")
        self.PsiSecondLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PsiSecondLineEdit.setGeometry(QtCore.QRect(450, 140, 61, 31))
        self.PsiSecondLineEdit.setObjectName("PsiSecondLineEdit")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(550, 40, 21, 31))
        self.label_9.setObjectName("label_9")
        self.PhiSecondLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PhiSecondLineEdit.setGeometry(QtCore.QRect(580, 140, 61, 31))
        self.PhiSecondLineEdit.setInputMask("")
        self.PhiSecondLineEdit.setObjectName("PhiSecondLineEdit")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(550, 140, 21, 31))
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 140, 81, 31))
        self.label_5.setObjectName("label_5")
        self.CoefficientALineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CoefficientALineEdit.setGeometry(QtCore.QRect(270, 140, 61, 31))
        self.CoefficientALineEdit.setObjectName("CoefficientALineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 20, 661, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ClearSheduleButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearSheduleButton.setGeometry(QtCore.QRect(70, 700, 181, 41))
        self.ClearSheduleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ClearSheduleButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.ClearSheduleButton.setObjectName("ClearSheduleButton")
        self.RunCalculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunCalculateButton.setGeometry(QtCore.QRect(310, 700, 181, 41))
        self.RunCalculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RunCalculateButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.RunCalculateButton.setObjectName("RunCalculateButton")
        self.ShowPhiFunctionButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShowPhiFunctionButton.setGeometry(QtCore.QRect(550, 700, 181, 41))
        self.ShowPhiFunctionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowPhiFunctionButton.setStyleSheet("background-color: #557a95; border: none;color: white;padding: 5px;text-align: center;  text-decoration: none;  font-size: 14px;\n"
"outline: none;")
        self.ShowPhiFunctionButton.setObjectName("ShowPhiFunctionButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.StringLengthLineEdit, self.TimeLineEdit)
        MainWindow.setTabOrder(self.TimeLineEdit, self.LengthStepLineEdit)
        MainWindow.setTabOrder(self.LengthStepLineEdit, self.TimeStepLineEdit)
        MainWindow.setTabOrder(self.TimeStepLineEdit, self.CoefficientALineEdit)
        MainWindow.setTabOrder(self.CoefficientALineEdit, self.PsiZeroLineEdit)
        MainWindow.setTabOrder(self.PsiZeroLineEdit, self.PsiFirtsLineEdit)
        MainWindow.setTabOrder(self.PsiFirtsLineEdit, self.PsiSecondLineEdit)
        MainWindow.setTabOrder(self.PsiSecondLineEdit, self.PhiZeroLineEdit)
        MainWindow.setTabOrder(self.PhiZeroLineEdit, self.PhiFirstLineEdit)
        MainWindow.setTabOrder(self.PhiFirstLineEdit, self.PhiSecondLineEdit)
        MainWindow.setTabOrder(self.PhiSecondLineEdit, self.RunCalculateButton)
        MainWindow.setTabOrder(self.RunCalculateButton, self.ShowPhiFunctionButton)
        MainWindow.setTabOrder(self.ShowPhiFunctionButton, self.ClearSheduleButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вычислительные методы"))
        self.groupBox.setTitle(_translate("MainWindow", "Данные для ввода:"))
        self.label_10.setText(_translate("MainWindow", "φ1"))
        self.label_4.setText(_translate("MainWindow", "Шаг по времени"))
        self.label_8.setText(_translate("MainWindow", "ψ0"))
        self.label_3.setText(_translate("MainWindow", "Шаг по длине"))
        self.label_2.setText(_translate("MainWindow", "Время"))
        self.label_7.setText(_translate("MainWindow", "ψ2"))
        self.label_6.setText(_translate("MainWindow", "ψ1"))
        self.label.setText(_translate("MainWindow", "Длина струны"))
        self.label_9.setText(_translate("MainWindow", "φ0"))
        self.label_11.setText(_translate("MainWindow", "φ2"))
        self.label_5.setText(_translate("MainWindow", "Коэффициент а"))
        self.ClearSheduleButton.setText(_translate("MainWindow", "Очистить холст"))
        self.RunCalculateButton.setText(_translate("MainWindow", "Выполнить решение"))
        self.ShowPhiFunctionButton.setText(_translate("MainWindow", "Вывести функцию Φ"))
