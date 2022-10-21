# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys
import window_template
import Ui_MainWindow

class MyWindow(Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 200, 400, 400) # ustawienie gdzie pojawia się okienko i jego wymiary
        self.setWindowTitle("Expense Tracker") # tytul okienka
        self.initUI() # inicjacja

    def initUI(self): # all staff to window
        #LABEL
        self.label = QtWidgets.QLabel(self) # podajemy gdzie ma być label
        self.label.setText("lalalal")
        self.label.move(50,50) #przesuniecie

        #BUTTON
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("HERE")
        self.button.move(100,100)
        self.button.clicked.connect(self.button_clicked)
    
    def button_clicked(self):
        self.label.setText("you pressed the button")
        self.update() # robimy update bo coś się zmienia

    def update(self):
        self.label.adjustSize() # dostosuj rozmiar labelka

#function to button clicked



def window():
    app = QApplication(sys.argv)
    window = MyWindow()
    #window.setGeometry(xpos, ypos, width, height) xpos=0-1920 ypos=0-1000


    window.show()
    sys.exit(app.exec_()) #do zamkniecia

window()