import random
import sys
import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLCDNumber, QSlider, QRadioButton, QLabel, QColorDialog, QComboBox)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore

#from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from difflib import get_close_matches

def insight4():
    class MainWindow(QWidget):

        def __init__(self):
            super().__init__()
            
            cr = pd.read_csv('q3carsales.csv', index_col = 0)
            cs = pd.read_csv('carrating.csv', index_col =0)
            fe = pd.read_csv('carFE.csv', index_col = 0)

            del cs['2020']
            cs.reset_index(inplace=True)
            cs = cs.sort_values(by='2019')
            cs = cs.dropna()
            
            self.names = []

            for a in cs.index:
                self.names.append(cs.loc[a][0])

            self.setWindowTitle("Car Ratings from Lowest to Highest")
            self.resize(700,200)
            self.bool = False


            self.label1 = QLabel("Car Model:")

            self.year1 = QRadioButton("2019")
            self.year2 = QRadioButton("2020")
            self.year1.clicked.connect(self.year1clicked)
            self.year2.clicked.connect(self.year2clicked)


            self.entryforlower= QLineEdit()
            self.output = QLineEdit()
            self.output.setAlignment(QtCore.Qt.AlignCenter)
            self.output.setEnabled(False)


            
            

            self.data = QPushButton("Get Data!")

            self.data.setStyleSheet("background-color: cyan")


            vbox = QVBoxLayout()
            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            hbox3 = QHBoxLayout()

            
            hbox2.addWidget(self.label1)
           
            vbox.addLayout(hbox1)



            
            self.slider = QSlider()
            
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.setTickPosition(QSlider.TicksBelow)
            self.slider.setTickInterval(1)
            self.slider.setMinimum(0)
            
            self.slider.setMaximum(len(self.names)-1)


            vbox.addWidget(self.slider)
            # vbox.addLayout(hbox2)
            # vbox.addWidget(self.data)
            # vbox.addLayout(hbox3)
            self.output.setAlignment
            vbox.addWidget(self.output)

            self.data.setEnabled(False)

            self.setLayout(vbox)



          

            self.slider.valueChanged.connect(self.changedValue)

            

        

        def changedValue(self):
            num = self.slider.value()
            self.output.setText(str(self.names[num]))




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




        








  

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())



############ Function Call ############
insight4()