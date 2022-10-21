from tkinter.messagebox import QUESTION
from ui_window_template import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
import sys 
from database import ExpenseTrackerDatabase
from plots import pie_chart

class ExpenseTrackerWindow(Ui_MainWindow):
    def __init__(self, MainWindow, parent=None):
        super().__init__()
        self.database = ExpenseTrackerDatabase()
        self.setupUi(MainWindow)
        self.initUI(MainWindow)

    
    def initUI(self, MainWindow):
        MainWindow.setGeometry(300, 50, 950, 750)

        self.update_total_sum()

        #buttons
        #first page
        self.button_add_expense.clicked.connect(self.show_add_new_expense)
        self.button_show_statistics.clicked.connect(self.show_statistics)
        self.button_reset.clicked.connect(self.popup_reset)
        #second page
        self.cancel_button.clicked.connect(self.show_main_page)
        self.add_button.clicked.connect(self.add_expense)
        #third page
        self.button_cancel.clicked.connect(self.show_main_page)
        self.button_categories_charts.clicked.connect(self.create_pie_chart)
        #fourth page
        self.button_cancel_categories_charts.clicked.connect(self.show_main_page)
        
    def show_add_new_expense(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
    
    def add_expense(self):
        id = 0 #???
        category = self.category_combo_box.currentText()
        cost = str(self.spinBox.value())
        date = str(self.dateEdit.text())
        details = self.details_text_edit.toPlainText()
        self.database.add_row(id, category, cost, date, details)
        print(f"{category} {cost} {date} {details}")
        self.update_total_sum()
        self.show_popup_added_expense(category, cost, date, details)

    def show_popup_added_expense(self, category, cost, date, details):
        message = QMessageBox()
        message.setWindowTitle("New expense added")
        message.setText("You added new expense")
        message.setInformativeText(f"{category} {cost}zł {date} {details}")
        x = message.exec_()


    def update_total_sum(self):
        new_sum = self.database.sum()
        self.label_total_sum.setText(str(new_sum))

    def show_statistics(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def show_main_page(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def reset(self, i):
        if i.text() == "&Yes":
            self.database.reset_database()
            self.update_total_sum()
    
    def popup_reset(self):
        message = QMessageBox()
        message.setWindowTitle("Reset")
        message.setText("Do you want to reset all expenses?")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.buttonClicked.connect(self.reset)
        x = message.exec_()

    def create_pie_chart(self):
        sums, categories = self.database.data_for_pie()
        pie_chart(sums, categories)
        self.label_categories_chart.setPixmap(QtGui.QPixmap("categories_chart.jpg"))
        self.stackedWidget.setCurrentWidget(self.page_4)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ExpenseTrackerWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())