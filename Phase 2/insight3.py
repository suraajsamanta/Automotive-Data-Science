import random
import sys
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLCDNumber, QSlider, QRadioButton, QLabel, QColorDialog, QComboBox)
from PyQt5.QtGui import QColor
#from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from difflib import get_close_matches
def insight4():
    class MainWindow(QWidget):

        def __init__(self):
            super().__init__()

            cs = pd.read_csv('q3carsales.csv', index_col = 0)
            cr = pd.read_csv('carrating.csv', index_col =0)
            fe = pd.read_csv('carFE.csv', index_col = 0)

            self.names = []

            for a in cs.index:
                self.names.append(a)

            make = []
            for name in self.names:
                x = name.split()
                if "Alfa Romeo" in name:
                    x = x[:2]
                    x = " ".join(x)
                elif "Land Rover" in name:
                    x = x[:2]
                    x = " ".join(x)
                else:
                    x = x[0]
                make.append(x)

            make = list(set(make))
            make.sort()
            print(len(cs.index))

            self.setWindowTitle("Changes in Sales by Make")
            self.resize(700,200)
            self.bool = False


            self.label1 = QLabel("Car Make:")


            self.entryforlower= QLineEdit()
            self.output = QLineEdit()


            self.comboBox = QComboBox(self)
            self.comboBox.setGeometry(50,50,400,35)
            self.comboBox.addItems(make)

            self.data = QPushButton("Get Data!")

            self.data.setStyleSheet("background-color: yellow")


            vbox = QVBoxLayout()
            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            hbox3 = QHBoxLayout()

            hbox2.addWidget(self.label1)
            hbox2.addWidget(self.comboBox)
            vbox.addLayout(hbox1)
            vbox.addLayout(hbox2)
            vbox.addWidget(self.data)
            vbox.addLayout(hbox3)
            vbox.addWidget(self.output)

            #self.data.setEnabled(False)

            self.setLayout(vbox)

            self.data.clicked.connect(self.getdata)



        def getdata(self):
            cs = pd.read_csv('q3carsales.csv', index_col = 0)
            cr = pd.read_csv('carrating.csv', index_col =0)
            fe = pd.read_csv('carFE.csv', index_col = 0)

            make1 = []
            for name in cs.index:
                x = name.split()
                if "Alfa Romeo" in name:
                    x = x[:2]
                    x = " ".join(x)
                elif "Land Rover" in name:
                    x = x[:2]
                    x = " ".join(x)
                else:
                    x = x[0]
                make1.append(x)
            cs.index = make1
            cs.reset_index(inplace=True)
            cs= cs.groupby(["index"]).aggregate({'2019':'mean', '2020': 'mean'}).round(3)
            car = self.comboBox.currentText()
            sales1 = cs.loc[car]["2019"]
            sales2 = cs.loc[car]["2020"]
            if (sales2-sales1) < 0:
                self.output.setText("Sales went down by " + str(sales1-sales2)[0:8] + "!")
                self.output.setStyleSheet("background-color: red")
            else:
                self.output.setText("Sales went up by " + str(sales2-sales1)[0:8] + "!")
                self.output.setStyleSheet("background-color: green")






    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())



############ Function Call ############
insight4()
