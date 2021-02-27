import random
import sys
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLCDNumber, QSlider, QRadioButton, QLabel, QColorDialog, QComboBox)
from PyQt5.QtGui import QColor
#from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from difflib import get_close_matches
def insight2():
    class MainWindow(QWidget):

        def __init__(self):
            super().__init__()

            cs = pd.read_csv('q3carsales.csv', index_col = 0)
            cr = pd.read_csv('carrating.csv', index_col =0)
            fe = pd.read_csv('carFE.csv', index_col = 0)

            self.names = []

            for a in cs.index:
                if not "Nissan Rogue" in a:
                    if not "Nissan Quest" in a:
                        if not "Nissan Juke" in a:
                            self.names.append(a)

            self.setWindowTitle("Car Sales, Fuel Economy, and Rating by Model")
            self.resize(700,200)
            self.bool = False


            self.label1 = QLabel("Car Model:")

            self.year1 = QRadioButton("2019")
            self.year2 = QRadioButton("2020")
            self.year1.clicked.connect(self.year1clicked)
            self.year2.clicked.connect(self.year2clicked)


            self.entryforlower= QLineEdit()
            self.output = QLineEdit()


            self.comboBox = QComboBox(self)
            self.comboBox.setGeometry(50,50,400,35)
            self.comboBox.addItems(self.names)

            self.data = QPushButton("Get Data!")

            self.data.setStyleSheet("background-color: cyan")


            vbox = QVBoxLayout()
            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            hbox3 = QHBoxLayout()

            hbox1.addWidget(self.year1)
            hbox1.addWidget(self.year2)
            hbox2.addWidget(self.label1)
            hbox2.addWidget(self.comboBox)
            vbox.addLayout(hbox1)
            vbox.addLayout(hbox2)
            vbox.addWidget(self.data)
            vbox.addLayout(hbox3)
            vbox.addWidget(self.output)

            self.data.setEnabled(False)

            self.setLayout(vbox)

            self.data.clicked.connect(self.getdata)






        def year1clicked(self):
            self.type = "2019"
            self.bool = True
            if self.bool:
                self.data.setEnabled(True)

        def year2clicked(self):
            self.type = "2020"
            self.bool = True
            if self.bool:
                self.data.setEnabled(True)




        def getdata(self):
            cs = pd.read_csv('q3carsales.csv', index_col = 0)
            cr = pd.read_csv('carrating.csv', index_col =0)
            fe = pd.read_csv('carFE.csv', index_col = 0)

            car = self.comboBox.currentText()

            if self.type == "2019":
                num = 0
            else:
                num = 1
            sales = cs.loc[car].iloc[num]

            try:
                if "-Class" in car:
                    x = car.split("-Class")
                    x = x[0]
                    fuel = fe.loc[x].iloc[num]
                elif "-Series" in car:
                    x = car.split("-Series")
                    x = x[0] + ""
                    val = get_close_matches(x,fe.index)
                    fuel = fe.loc[val[0]].iloc[num]
                elif "Range" in car:
                    x = car.split("Range")
                    x = x[0] + "Range"
                    val = get_close_matches(x,fe.index)
                    fuel = fe.loc[val[0]].iloc[num]
                elif "Discovery" in car:
                    x = car.split("Discovery")
                    x = x[0] + "Discovery"
                    val = get_close_matches(x,fe.index)
                    fuel = fe.loc[val[0]].iloc[num]
                else:
                    fuel = fe.loc[car].iloc[num]
            except:
                fuel = "No Data Available"

            if self.type == "2019":
                num = 1
            else:
                num = 0

            rating = str(cs.loc[car].iloc[num])
            if rating == "nan" or rating == "0.0":
                rating = "No Data Available"
            if str(sales) == "0.0":
                sales = "No Data Available"
            self.output.setText("Q3 Car Sales: " + str(sales) + "            " + "JD Car Rating: " + str(rating) + "            " + " Fuel Economy: " + str(fuel))











    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())



############ Function Call ############
insight2()
