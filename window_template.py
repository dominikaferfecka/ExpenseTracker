# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(958, 735)
        MainWindow.setGeometry(300, 50, 950, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(290, 50, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 200, 511, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_add_expense = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_add_expense.setFont(font)
        self.button_add_expense.setObjectName("button_add_expense")
        self.verticalLayout.addWidget(self.button_add_expense)
        self.button_show_statistics = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_show_statistics.setFont(font)
        self.button_show_statistics.setObjectName("button_show_statistics")
        self.verticalLayout.addWidget(self.button_show_statistics)
        self.stackedWidget.addWidget(self.page)
        
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(90, 310, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(90, 400, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.add_button = QtWidgets.QPushButton(self.page_2)
        self.add_button.setGeometry(QtCore.QRect(270, 560, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.cancel_button = QtWidgets.QPushButton(self.page_2)
        self.cancel_button.setGeometry(QtCore.QRect(460, 560, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.details_text_edit = QtWidgets.QTextEdit(self.page_2)
        self.details_text_edit.setGeometry(QtCore.QRect(260, 420, 291, 31))
        self.details_text_edit.setObjectName("details_text_edit")
        self.category_combo_box = QtWidgets.QComboBox(self.page_2)
        self.category_combo_box.setGeometry(QtCore.QRect(260, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.category_combo_box.setFont(font)
        self.category_combo_box.setObjectName("category_combo_box")
        self.category_combo_box.addItem("")
        self.category_combo_box.addItem("")
        self.category_combo_box.addItem("")
        self.category_combo_box.addItem("")
        self.category_combo_box.addItem("")
        self.category_combo_box.addItem("")
        self.category_combo_box.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.page_2)
        self.dateEdit.setGeometry(QtCore.QRect(260, 320, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.spinBox = QtWidgets.QSpinBox(self.page_2)
        self.spinBox.setGeometry(QtCore.QRect(260, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.stackedWidget.addWidget(self.page_2)
        
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(320, 20, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setTitle("")
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setStatusTip("")
        self.action.setObjectName("action")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expense Tracker"))
        self.label.setText(_translate("MainWindow", "Expense Tracker"))
        self.button_add_expense.setText(_translate("MainWindow", "Add new expense"))
        self.button_show_statistics.setText(_translate("MainWindow", "Show statistics"))
        self.label_2.setText(_translate("MainWindow", "Add new expense"))
        self.label_4.setText(_translate("MainWindow", "Category"))
        self.label_5.setText(_translate("MainWindow", "Cost"))
        self.label_6.setText(_translate("MainWindow", "Date"))
        self.label_7.setText(_translate("MainWindow", "Details"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.category_combo_box.setItemText(0, _translate("MainWindow", "Food"))
        self.category_combo_box.setItemText(1, _translate("MainWindow", "Transportation"))
        self.category_combo_box.setItemText(2, _translate("MainWindow", "Medical & Healthcare"))
        self.category_combo_box.setItemText(3, _translate("MainWindow", "Clothes & shoes"))
        self.category_combo_box.setItemText(4, _translate("MainWindow", "Entertainment"))
        self.category_combo_box.setItemText(5, _translate("MainWindow", "Housing"))
        self.category_combo_box.setItemText(6, _translate("MainWindow", "Other"))
        self.label_3.setText(_translate("MainWindow", "Statistics"))
        self.menuFile.setTitle(_translate("MainWindow", " "))
        self.action.setText(_translate("MainWindow", "New"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
