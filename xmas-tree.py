# Interactive RGB 3D Christmas tree
# Version 1.0
# Created By David Peck
# Some of the code has been modified from various web sources
# Created Aug-2022
# The program allows the user to set various parameters
# File Name: xmas-tree.py

from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QApplication, QWidget, QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from tree import RGBXmasTree
from colorzero import Color
from numpy.random import permutation
import sys
import time

tree = RGBXmasTree()

# Initial Brightness Level
level = 0.1
tree.brightness = (level)

# Initial LED State
led_state = "black"

colorchoice_0 = led_state
colorchoice_1 = led_state
colorchoice_2 = led_state
colorchoice_3 = led_state
colorchoice_4 = led_state
colorchoice_5 = led_state
colorchoice_6 = led_state
colorchoice_7 = led_state
colorchoice_8 = led_state
colorchoice_9 = led_state
colorchoice_10 = led_state
colorchoice_11 = led_state
colorchoice_12 = led_state
colorchoice_13 = led_state
colorchoice_14 = led_state
colorchoice_15 = led_state
colorchoice_16 = led_state
colorchoice_17 = led_state
colorchoice_18 = led_state
colorchoice_19 = led_state
colorchoice_20 = led_state
colorchoice_21 = led_state
colorchoice_22 = led_state
colorchoice_23 = led_state
colorchoice_24 = led_state

# Cycle 1 Settings
range1 = 5
snooze_a = 0
snooze_b = 0

# Cycle 2 Settings
range2 = 5
snooze_c = 0
snooze_d = 0

# Cycle 3 Settings
range3 = 5
snooze_e = 0
snooze_f = 0

####################################### Initialise GUI ############################################

class treegui(QtWidgets.QMainWindow):        
    
    def __init__(self):
        
        super(treegui, self).__init__()
        uic.loadUi('treegui.ui', self)
        
        pixmap = QPixmap("tree_A.jpg")
        self.image_label_1.setPixmap(pixmap)
        
        pixmap2 = QPixmap("tree_B.jpg")
        self.image_label_2.setPixmap(pixmap2)
        
        pixmap3 = QPixmap("tree_L.jpg")
        self.image_label_3.setPixmap(pixmap3)
        
        pixmap4 = QPixmap("tree_R.jpg")
        self.image_label_4.setPixmap(pixmap4)
        
        self.label_7.setStyleSheet("background: #fcd7da")
        self.label_8.setStyleSheet("background: #fcd7da")
        self.label_9.setStyleSheet("background: #fcd7da")
        
        self.color_select.addItem("black") 
        self.color_select.addItem("red")
        self.color_select.addItem("yellow")
        self.color_select.addItem("green")
        self.color_select.addItem("blue")
        self.color_select.addItem("cyan")
        self.color_select.addItem("purple")
        self.color_select.addItem("white")
        
        self.set_cycles.addItem("5")
        self.set_cycles.addItem("10")
        self.set_cycles.addItem("25")
        self.set_cycles.addItem("50")
        self.set_cycles.addItem("100") 
        self.set_cycles.addItem("1000")
        self.set_cycles.addItem("10000")
        
        self.set_delay1.addItem("0")
        self.set_delay1.addItem("0.01")                       
        self.set_delay1.addItem("0.02")                        
        self.set_delay1.addItem("0.03")                        
        self.set_delay1.addItem("0.04")                        
        self.set_delay1.addItem("0.05")                        
        self.set_delay1.addItem("0.06")
        self.set_delay1.addItem("0.07")
        self.set_delay1.addItem("0.08")
        self.set_delay1.addItem("0.09")
        self.set_delay1.addItem("0.1")
        self.set_delay1.addItem("0.2")                        
        self.set_delay1.addItem("0.3")
        self.set_delay1.addItem("0.4")
        self.set_delay1.addItem("0.5")
                                
        self.set_delay2.addItem("0")
        self.set_delay2.addItem("0.01")                       
        self.set_delay2.addItem("0.02")                        
        self.set_delay2.addItem("0.03")                        
        self.set_delay2.addItem("0.04")                        
        self.set_delay2.addItem("0.05")                        
        self.set_delay2.addItem("0.06")
        self.set_delay2.addItem("0.07")
        self.set_delay2.addItem("0.08")
        self.set_delay2.addItem("0.09")
        self.set_delay2.addItem("0.1")
        self.set_delay2.addItem("0.2")                        
        self.set_delay2.addItem("0.3")
        self.set_delay2.addItem("0.4")
        self.set_delay2.addItem("0.5")
        
        self.run_order_1.addItem("None")
        self.run_order_1.addItem("Variation-1")
        self.run_order_1.addItem("Variation-2")
        self.run_order_1.addItem("Variation-3")
        
        
        self.run_order_2.addItem("None")
        self.run_order_2.addItem("Variation-1")
        self.run_order_2.addItem("Variation-2")
        self.run_order_2.addItem("Variation-3")
        
        
        self.run_order_3.addItem("None")
        self.run_order_3.addItem("Variation-1")
        self.run_order_3.addItem("Variation-2")
        self.run_order_3.addItem("Variation-3")
        
        
        self.button_0.clicked.connect(self.set_led_color_0)
        self.button_0.setStyleSheet("background: #B2B1B9")
        
        self.button_1.clicked.connect(self.set_led_color_1)
        self.button_1.setStyleSheet("background: #B2B1B9")
        
        self.button_2.clicked.connect(self.set_led_color_2)
        self.button_2.setStyleSheet("background: #B2B1B9")
        
        self.button_3.clicked.connect(self.set_led_color_3)
        self.button_3.setStyleSheet("background: #B2B1B9")
        
        self.button_4.clicked.connect(self.set_led_color_4)
        self.button_4.setStyleSheet("background: #B2B1B9")
        
        self.button_5.clicked.connect(self.set_led_color_5)
        self.button_5.setStyleSheet("background: #B2B1B9")
        
        self.button_6.clicked.connect(self.set_led_color_6)
        self.button_6.setStyleSheet("background: #B2B1B9")
        
        self.button_7.clicked.connect(self.set_led_color_7)
        self.button_7.setStyleSheet("background: #B2B1B9")
        
        self.button_8.clicked.connect(self.set_led_color_8)
        self.button_8.setStyleSheet("background: #B2B1B9")
        
        self.button_9.clicked.connect(self.set_led_color_9)
        self.button_9.setStyleSheet("background: #B2B1B9")
        
        self.button_10.clicked.connect(self.set_led_color_10)
        self.button_10.setStyleSheet("background: #B2B1B9")
        
        self.button_11.clicked.connect(self.set_led_color_11)
        self.button_11.setStyleSheet("background: #B2B1B9")
        
        self.button_12.clicked.connect(self.set_led_color_12)
        self.button_12.setStyleSheet("background: #B2B1B9")
        
        self.button_13.clicked.connect(self.set_led_color_13)
        self.button_13.setStyleSheet("background: #B2B1B9")
        
        self.button_14.clicked.connect(self.set_led_color_14)
        self.button_14.setStyleSheet("background: #B2B1B9")
        
        self.button_15.clicked.connect(self.set_led_color_15)
        self.button_15.setStyleSheet("background: #B2B1B9")
        
        self.button_16.clicked.connect(self.set_led_color_16)
        self.button_16.setStyleSheet("background: #B2B1B9")
        
        self.button_17.clicked.connect(self.set_led_color_17)
        self.button_17.setStyleSheet("background: #B2B1B9")
        
        self.button_18.clicked.connect(self.set_led_color_18)
        self.button_18.setStyleSheet("background: #B2B1B9")
        
        self.button_19.clicked.connect(self.set_led_color_19)
        self.button_19.setStyleSheet("background: #B2B1B9")
        
        self.button_20.clicked.connect(self.set_led_color_20)
        self.button_20.setStyleSheet("background: #B2B1B9")
        
        self.button_21.clicked.connect(self.set_led_color_21)
        self.button_21.setStyleSheet("background: #B2B1B9")
        
        self.button_22.clicked.connect(self.set_led_color_22)
        self.button_22.setStyleSheet("background: #B2B1B9")
        
        self.button_23.clicked.connect(self.set_led_color_23)
        self.button_23.setStyleSheet("background: #B2B1B9")
        
        self.button_24.clicked.connect(self.set_led_color_24)
        self.button_24.setStyleSheet("background: #B2B1B9")
        
        self.all_off.clicked.connect(self.tree_off)
        
        self.set_all.clicked.connect(self.on_click_set_all)
        
        self.brightness_slider.setRange(0, 10)
        self.brightness_slider.setValue(1)
        self.brightness_slider.valueChanged.connect(self.brightness_value_changed)
        self.bright_level.setText(str(level))
        self.brightness_slider.setStyleSheet("background: #FCFFA6")
        
        self.set_front.clicked.connect(self.set_front_btn)
        self.set_rear.clicked.connect(self.set_rear_btn)
        self.set_left.clicked.connect(self.set_left_btn)
        self.set_right.clicked.connect(self.set_right_btn)
        
        self.run_cycle.clicked.connect(self.cycle_run)
        self.run_cycle_2.clicked.connect(self.cycle2_run)
        self.run_cycle_3.clicked.connect(self.cycle3_run)
        
        self.set_1.clicked.connect(self.variation1_settings)
        self.set_2.clicked.connect(self.variation2_settings)
        self.set_3.clicked.connect(self.variation3_settings)
        
        self.start_btn.clicked.connect(self.start_btn_clicked)
        
        self.reset_btn.clicked.connect(self.reset_values)
              
####################################### Set Brightness ############################################
    def brightness_value_changed(self,b):
        global level
        level = b/10
        tree.brightness = (level)
        self.bright_level.setText(str(level))

####################################### Set Front ################################################# 
    def set_front_btn(self):
        global colorchoice_0       
        global colorchoice_1
        global colorchoice_2
        global colorchoice_3
        global colorchoice_4
        global colorchoice_5
        global colorchoice_6
        
        colorchoice_0 = str(self.color_select.currentText())
        tree[0].color = Color(self.color_select.currentText())
        if colorchoice_0 == "black":
                self.button_0.setStyleSheet("background: #B2B1B9")
        else:
            self.button_0.setStyleSheet("background:" + (colorchoice_0))
        
        colorchoice_1 = self.color_select.currentText()               
        tree[1].color = Color(self.color_select.currentText())
        if colorchoice_1 == "black":
                self.button_1.setStyleSheet("background: #B2B1B9")
        else:
            self.button_1.setStyleSheet("background:" + (colorchoice_1))       
        
        colorchoice_2 = self.color_select.currentText()
        tree[2].color = Color(self.color_select.currentText())    
        if colorchoice_2 == "black":
                self.button_2.setStyleSheet("background: #B2B1B9")
        else:        
            self.button_2.setStyleSheet("background:" + (colorchoice_2))       
        
        colorchoice_3 = self.color_select.currentText()
        tree[3].color = Color(self.color_select.currentText())
        if colorchoice_3 == "black":
                self.button_3.setStyleSheet("background: #B2B1B9")
        else:
            self.button_3.setStyleSheet("background:" + (colorchoice_3))        
                
        colorchoice_4 = self.color_select.currentText()
        tree[4].color = Color(self.color_select.currentText())
        if colorchoice_4 == "black":
                self.button_4.setStyleSheet("background: #B2B1B9")
        else:
            self.button_4.setStyleSheet("background:" + (colorchoice_4))    
              
        colorchoice_5 = self.color_select.currentText()
        tree[5].color = Color(self.color_select.currentText()) 
        if colorchoice_5 == "black":
                self.button_5.setStyleSheet("background: #B2B1B9")
        else:
            self.button_5.setStyleSheet("background:" + (colorchoice_5))    
        
        colorchoice_6 = self.color_select.currentText()
        tree[6].color = Color(self.color_select.currentText())        
        if colorchoice_6 == "black":
                self.button_6.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_6.setStyleSheet("background:" + (colorchoice_6))
            
####################################### Set Rear  #################################################     
    def set_rear_btn(self):       
        global colorchoice_7
        global colorchoice_8
        global colorchoice_9
        global colorchoice_10
        global colorchoice_11
        global colorchoice_12
        
        colorchoice_7 = self.color_select.currentText()
        tree[7].color = Color(self.color_select.currentText()) 
        if colorchoice_7 == "black":
                self.button_7.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_7.setStyleSheet("background:" + (colorchoice_7))
     
        colorchoice_8 = self.color_select.currentText()
        tree[8].color = Color(self.color_select.currentText()) 
        if colorchoice_8 == "black":
                self.button_8.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_8.setStyleSheet("background:" + (colorchoice_8))

        colorchoice_9 = self.color_select.currentText()
        tree[9].color = Color(self.color_select.currentText())
        if colorchoice_9 == "black":
                self.button_9.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_9.setStyleSheet("background:" + (colorchoice_9))
             
        colorchoice_10 = self.color_select.currentText()
        tree[10].color = Color(self.color_select.currentText())    
        if colorchoice_10 == "black":
                self.button_10.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_10.setStyleSheet("background:" + (colorchoice_10))
                 
        colorchoice_11 = self.color_select.currentText()
        tree[11].color = Color(self.color_select.currentText())    
        if colorchoice_11 == "black":
                self.button_11.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_11.setStyleSheet("background:" + (colorchoice_11))
        
        colorchoice_12 = self.color_select.currentText()
        tree[12].color = Color(self.color_select.currentText())  
        if colorchoice_12 == "black":
                self.button_12.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_12.setStyleSheet("background:" + (colorchoice_12))

####################################### Set Left  #################################################
    def set_left_btn(self):           
        global colorchoice_13
        global colorchoice_14
        global colorchoice_15
        global colorchoice_22
        global colorchoice_23
        global colorchoice_24
        
        colorchoice_13 = self.color_select.currentText()
        tree[13].color = Color(self.color_select.currentText())   
        if colorchoice_13 == "black":
                self.button_13.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_13.setStyleSheet("background:" + (colorchoice_13))
        
        colorchoice_14 = self.color_select.currentText()
        tree[14].color = Color(self.color_select.currentText())
        if colorchoice_14 == "black":
                self.button_14.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_14.setStyleSheet("background:" + (colorchoice_14))
            
        colorchoice_15 = self.color_select.currentText()
        tree[15].color = Color(self.color_select.currentText())    
        if colorchoice_15 == "black":
                self.button_15.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_15.setStyleSheet("background:" + (colorchoice_15))
        
        colorchoice_22 = self.color_select.currentText()
        tree[22].color = Color(self.color_select.currentText())    
        if colorchoice_22 == "black":
                self.button_22.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_22.setStyleSheet("background:" + (colorchoice_22))
        
        colorchoice_23 = self.color_select.currentText()
        tree[23].color = Color(self.color_select.currentText())    
        if colorchoice_23 == "black":
                self.button_23.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_23.setStyleSheet("background:" + (colorchoice_23))
        
        colorchoice_24 = self.color_select.currentText() 
        tree[24].color = Color(self.color_select.currentText())    
        if colorchoice_24 == "black":
                self.button_24.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_24.setStyleSheet("background:" + (colorchoice_24))    

####################################### Set Right #################################################
    def set_right_btn(self):     
        global colorchoice_16
        global colorchoice_17
        global colorchoice_18
        global colorchoice_19
        global colorchoice_20
        global colorchoice_21
        
        colorchoice_16 = self.color_select.currentText() 
        tree[16].color = Color(self.color_select.currentText())   
        if colorchoice_16 == "black":
                self.button_16.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_16.setStyleSheet("background:" + (colorchoice_16))
        
        colorchoice_17 = self.color_select.currentText()
        tree[17].color = Color(self.color_select.currentText())    
        if colorchoice_17 == "black":
                self.button_17.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_17.setStyleSheet("background:" + (colorchoice_17))
        
        colorchoice_18 = self.color_select.currentText()
        tree[18].color = Color(self.color_select.currentText())    
        if colorchoice_18 == "black":
                self.button_18.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_18.setStyleSheet("background:" + (colorchoice_18))       

        colorchoice_19 = self.color_select.currentText()
        tree[19].color = Color(self.color_select.currentText())
        if colorchoice_19 == "black":
                self.button_19.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_19.setStyleSheet("background:" + (colorchoice_19))

        colorchoice_20 = self.color_select.currentText()
        tree[20].color = Color(self.color_select.currentText())    
        if colorchoice_20 == "black":
                self.button_20.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_20.setStyleSheet("background:" + (colorchoice_20))

        colorchoice_21 = self.color_select.currentText()
        tree[21].color = Color(self.color_select.currentText())    
        if colorchoice_21 == "black":
                self.button_21.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_21.setStyleSheet("background:" + (colorchoice_21))

####################################### Set LED 0 #################################################
    def set_led_color_0(self):        
        global colorchoice_0 
        
        colorchoice_0 = str(self.color_select.currentText())
        tree[0].color = Color(self.color_select.currentText())
        if colorchoice_0 == "black":
                self.button_0.setStyleSheet("background: #B2B1B9")
        else:
            self.button_0.setStyleSheet("background:" + (colorchoice_0))

####################################### Set LED 1 #################################################         
    def set_led_color_1(self):        
        global colorchoice_1 
        
        colorchoice_1 = self.color_select.currentText()               
        tree[1].color = Color(self.color_select.currentText())
        if colorchoice_1 == "black":
                self.button_1.setStyleSheet("background: #B2B1B9")
        else:
            self.button_1.setStyleSheet("background:" + (colorchoice_1))
            
####################################### Set LED 2 #################################################         
    def set_led_color_2(self):        
        global colorchoice_2
        
        colorchoice_2 = self.color_select.currentText()
        tree[2].color = Color(self.color_select.currentText())    
        if colorchoice_2 == "black":
                self.button_2.setStyleSheet("background: #B2B1B9")
        else:        
            self.button_2.setStyleSheet("background:" + (colorchoice_2))
            
####################################### Set LED 3 #################################################        
    def set_led_color_3(self):        
        global colorchoice_3
        
        colorchoice_3 = self.color_select.currentText()
        tree[3].color = Color(self.color_select.currentText())
        if colorchoice_3 == "black":
                self.button_3.setStyleSheet("background: #B2B1B9")
        else:
            self.button_3.setStyleSheet("background:" + (colorchoice_3))
            
####################################### Set LED 4 #################################################          
    def set_led_color_4(self):        
        global colorchoice_4
        
        colorchoice_4 = self.color_select.currentText()
        tree[4].color = Color(self.color_select.currentText())
        if colorchoice_4 == "black":
                self.button_4.setStyleSheet("background: #B2B1B9")
        else:
            self.button_4.setStyleSheet("background:" + (colorchoice_4))
            
####################################### Set LED 5 #################################################        
    def set_led_color_5(self):        
        global colorchoice_5
        
        colorchoice_5 = self.color_select.currentText()
        tree[5].color = Color(self.color_select.currentText()) 
        if colorchoice_5 == "black":
                self.button_5.setStyleSheet("background: #B2B1B9")
        else:
            self.button_5.setStyleSheet("background:" + (colorchoice_5))
            
####################################### Set LED 6 #################################################          
    def set_led_color_6(self):        
        global colorchoice_6
        
        colorchoice_6 = self.color_select.currentText()
        tree[6].color = Color(self.color_select.currentText())        
        if colorchoice_6 == "black":
                self.button_6.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_6.setStyleSheet("background:" + (colorchoice_6))
            
####################################### Set LED 7 #################################################           
    def set_led_color_7(self):        
        global colorchoice_7
        
        colorchoice_7 = self.color_select.currentText()
        tree[7].color = Color(self.color_select.currentText()) 
        if colorchoice_7 == "black":
                self.button_7.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_7.setStyleSheet("background:" + (colorchoice_7))
            
####################################### Set LED 8 #################################################        
    def set_led_color_8(self):        
        global colorchoice_8
        
        colorchoice_8 = self.color_select.currentText()
        tree[8].color = Color(self.color_select.currentText()) 
        if colorchoice_8 == "black":
                self.button_8.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_8.setStyleSheet("background:" + (colorchoice_8))
            
####################################### Set LED 9 #################################################       
    def set_led_color_9(self):        
        global colorchoice_9
        
        colorchoice_9 = self.color_select.currentText()
        tree[9].color = Color(self.color_select.currentText())
        if colorchoice_9 == "black":
                self.button_9.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_9.setStyleSheet("background:" + (colorchoice_9))
            
####################################### Set LED 10 ################################################        
    def set_led_color_10(self):        
        global colorchoice_10
        
        colorchoice_10 = self.color_select.currentText()
        tree[10].color = Color(self.color_select.currentText())    
        if colorchoice_10 == "black":
                self.button_10.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_10.setStyleSheet("background:" + (colorchoice_10))
            
####################################### Set LED 11 ################################################         
    def set_led_color_11(self):        
        global colorchoice_11
        
        colorchoice_11 = self.color_select.currentText()
        tree[11].color = Color(self.color_select.currentText())    
        if colorchoice_11 == "black":
                self.button_11.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_11.setStyleSheet("background:" + (colorchoice_11))
            
####################################### Set LED 12 ################################################         
    def set_led_color_12(self):        
        global colorchoice_12
    
        colorchoice_12 = self.color_select.currentText()
        tree[12].color = Color(self.color_select.currentText())  
        if colorchoice_12 == "black":
                self.button_12.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_12.setStyleSheet("background:" + (colorchoice_12))
            
####################################### Set LED 13 ################################################         
    def set_led_color_13(self):        
        global colorchoice_13
        
        colorchoice_13 = self.color_select.currentText()
        tree[13].color = Color(self.color_select.currentText())   
        if colorchoice_13 == "black":
                self.button_13.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_13.setStyleSheet("background:" + (colorchoice_13))
            
####################################### Set LED 14 ################################################        
    def set_led_color_14(self):        
        global colorchoice_14
        
        colorchoice_14 = self.color_select.currentText()
        tree[14].color = Color(self.color_select.currentText())
        if colorchoice_14 == "black":
                self.button_14.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_14.setStyleSheet("background:" + (colorchoice_14))
            
####################################### Set LED 15 ################################################          
    def set_led_color_15(self):        
        global colorchoice_15
        
        colorchoice_15 = self.color_select.currentText()
        tree[15].color = Color(self.color_select.currentText())    
        if colorchoice_15 == "black":
                self.button_15.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_15.setStyleSheet("background:" + (colorchoice_15))
            
####################################### Set LED 16 ################################################        
    def set_led_color_16(self):        
        global colorchoice_16
        
        colorchoice_16 = self.color_select.currentText()
        tree[16].color = Color(self.color_select.currentText())   
        if colorchoice_16 == "black":
                self.button_16.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_16.setStyleSheet("background:" + (colorchoice_16))
            
####################################### Set LED 17 ################################################          
    def set_led_color_17(self):        
        global colorchoice_17
        
        colorchoice_17 = self.color_select.currentText()
        tree[17].color = Color(self.color_select.currentText())    
        if colorchoice_17 == "black":
                self.button_17.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_17.setStyleSheet("background:" + (colorchoice_17))
            
####################################### Set LED 18 ################################################           
    def set_led_color_18(self):        
        global colorchoice_18
        
        colorchoice_18 = self.color_select.currentText()
        tree[18].color = Color(self.color_select.currentText())    
        if colorchoice_18 == "black":
                self.button_18.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_18.setStyleSheet("background:" + (colorchoice_18))
            
####################################### Set LED 19 ################################################           
    def set_led_color_19(self):        
        global colorchoice_19
        
        colorchoice_19 = self.color_select.currentText()
        tree[19].color = Color(self.color_select.currentText())
        if colorchoice_19 == "black":
                self.button_19.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_19.setStyleSheet("background:" + (colorchoice_19))
            
####################################### Set LED 20 ################################################          
    def set_led_color_20(self):        
        global colorchoice_20
        
        colorchoice_20 = self.color_select.currentText()
        tree[20].color = Color(self.color_select.currentText())    
        if colorchoice_20 == "black":
                self.button_20.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_20.setStyleSheet("background:" + (colorchoice_20))
            
####################################### Set LED 21 ################################################         
    def set_led_color_21(self):        
        global colorchoice_21
        
        colorchoice_21 = self.color_select.currentText()
        tree[21].color = Color(self.color_select.currentText())    
        if colorchoice_21 == "black":
                self.button_21.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_21.setStyleSheet("background:" + (colorchoice_21))
            
####################################### Set LED 22 ################################################         
    def set_led_color_22(self):        
        global colorchoice_22
        
        colorchoice_22 = self.color_select.currentText()
        tree[22].color = Color(self.color_select.currentText())    
        if colorchoice_22 == "black":
                self.button_22.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_22.setStyleSheet("background:" + (colorchoice_22))
            
####################################### Set LED 23 ################################################          
    def set_led_color_23(self):        
        global colorchoice_23
        
        colorchoice_23 = self.color_select.currentText()
        tree[23].color = Color(self.color_select.currentText())    
        if colorchoice_23 == "black":
                self.button_23.setStyleSheet("background: #B2B1B9") 
        else:
            self.button_23.setStyleSheet("background:" + (colorchoice_23))
            
####################################### Set LED 24 ################################################         
    def set_led_color_24(self):        
        global colorchoice_24
        
        colorchoice_24 = self.color_select.currentText()
        tree[24].color = Color(self.color_select.currentText())    
        if colorchoice_24 == "black":
                self.button_24.setStyleSheet("background: #B2B1B9")  
        else:
            self.button_24.setStyleSheet("background:" + (colorchoice_24))
    
####################################### Tree On ###################################################            
    def on_click_set_all(self):
        global colorchoice_0 
        global colorchoice_1 
        global colorchoice_2
        global colorchoice_3
        global colorchoice_4
        global colorchoice_5
        global colorchoice_6
        global colorchoice_7
        global colorchoice_8
        global colorchoice_9
        global colorchoice_10
        global colorchoice_11
        global colorchoice_12
        global colorchoice_13
        global colorchoice_14
        global colorchoice_15
        global colorchoice_16
        global colorchoice_17
        global colorchoice_18
        global colorchoice_19
        global colorchoice_20
        global colorchoice_21
        global colorchoice_22
        global colorchoice_23
        global colorchoice_24
         
        tree[0].color = Color(colorchoice_0)
        if colorchoice_0 == "black":
                self.button_0.setStyleSheet("background: #B2B1B9")
        else:
            self.button_0.setStyleSheet("background:" + (colorchoice_0))
        
        tree[1].color = Color(colorchoice_1)
        if colorchoice_1 == "black":
                self.button_1.setStyleSheet("background: #B2B1B9")
        else:
            self.button_1.setStyleSheet("background:" + (colorchoice_1))
        
        tree[2].color = Color(colorchoice_2)
        if colorchoice_2 == "black":
                self.button_2.setStyleSheet("background: #B2B1B9")
        else:
            self.button_2.setStyleSheet("background:" + (colorchoice_2))
        
        tree[3].color = Color(colorchoice_3)
        if colorchoice_3 == "black":
                self.button_3.setStyleSheet("background: #B2B1B9")
        else:
            self.button_3.setStyleSheet("background:" + (colorchoice_3))
        
        tree[4].color = Color(colorchoice_4)
        if colorchoice_4 == "black":
                self.button_4.setStyleSheet("background: #B2B1B9")
        else:
            self.button_4.setStyleSheet("background:" + (colorchoice_4))
        
        tree[5].color = Color(colorchoice_5)
        if colorchoice_5 == "black":
                self.button_5.setStyleSheet("background: #B2B1B9")
        else:
            self.button_5.setStyleSheet("background:" + (colorchoice_5))
        
        tree[6].color = Color(colorchoice_6)
        if colorchoice_6 == "black":
                self.button_6.setStyleSheet("background: #B2B1B9")
        else: 
            self.button_6.setStyleSheet("background:" + (colorchoice_6))

        tree[7].color = Color(colorchoice_7)
        if colorchoice_7 == "black":
                self.button_7.setStyleSheet("background: #B2B1B9")
        else:
            self.button_7.setStyleSheet("background:" + (colorchoice_7))
        
        tree[8].color = Color(colorchoice_8)
        if colorchoice_8 == "black":
                self.button_8.setStyleSheet("background: #B2B1B9")
        else:
            self.button_8.setStyleSheet("background:" + (colorchoice_8))
        
        tree[9].color = Color(colorchoice_9)
        if colorchoice_9 == "black":
                self.button_9.setStyleSheet("background: #B2B1B9")
        else: 
            self.button_9.setStyleSheet("background:" + (colorchoice_9))
        
        tree[10].color = Color(colorchoice_10)
        if colorchoice_10 == "black":
                self.button_10.setStyleSheet("background: #B2B1B9")
        else:
            self.button_10.setStyleSheet("background:" + (colorchoice_10))
        
        tree[11].color = Color(colorchoice_11)
        if colorchoice_11 == "black":
                self.button_11.setStyleSheet("background: #B2B1B9")
        else:
            self.button_11.setStyleSheet("background:" + (colorchoice_11))
        
        tree[12].color = Color(colorchoice_12)
        if colorchoice_12 == "black":
                self.button_12.setStyleSheet("background: #B2B1B9")
        else:
            self.button_12.setStyleSheet("background:" + (colorchoice_12))
        
        tree[13].color = Color(colorchoice_13)
        if colorchoice_13 == "black":
                self.button_13.setStyleSheet("background: #B2B1B9")
        else:
            self.button_13.setStyleSheet("background:" + (colorchoice_13))
        
        tree[14].color = Color(colorchoice_14)
        if colorchoice_14 == "black":
                self.button_14.setStyleSheet("background: #B2B1B9")
        else:
            self.button_14.setStyleSheet("background:" + (colorchoice_14))
        
        tree[15].color = Color(colorchoice_15)
        if colorchoice_15 == "black":
                self.button_15.setStyleSheet("background: #B2B1B9")
        else:
            self.button_15.setStyleSheet("background:" + (colorchoice_15))
        
        tree[16].color = Color(colorchoice_16)
        if colorchoice_16 == "black":
                self.button_16.setStyleSheet("background: #B2B1B9")
        else:
            self.button_16.setStyleSheet("background:" + (colorchoice_16))
        
        tree[17].color = Color(colorchoice_17)
        if colorchoice_17 == "black":
                self.button_17.setStyleSheet("background: #B2B1B9")
        else:
            self.button_17.setStyleSheet("background:" + (colorchoice_17))
        
        tree[18].color = Color(colorchoice_18)
        if colorchoice_18 == "black":
                self.button_18.setStyleSheet("background: #B2B1B9")
        else:
            self.button_18.setStyleSheet("background:" + (colorchoice_18))
        
        tree[19].color = Color(colorchoice_19)
        if colorchoice_19 == "black":
                self.button_19.setStyleSheet("background: #B2B1B9")
        else:
            self.button_19.setStyleSheet("background:" + (colorchoice_19))
        
        tree[20].color = Color(colorchoice_20)
        if colorchoice_20 == "black":
                self.button_20.setStyleSheet("background: #B2B1B9")
        else:
            self.button_20.setStyleSheet("background:" + (colorchoice_20))
        
        tree[21].color = Color(colorchoice_21)
        if colorchoice_21 == "black":
                self.button_21.setStyleSheet("background: #B2B1B9")
        else:
            self.button_21.setStyleSheet("background:" + (colorchoice_21))
        
        tree[22].color = Color(colorchoice_22)
        if colorchoice_22 == "black":
                self.button_22.setStyleSheet("background: #B2B1B9")
        else:
            self.button_22.setStyleSheet("background:" + (colorchoice_22))
        
        tree[23].color = Color(colorchoice_23)
        if colorchoice_23 == "black":
                self.button_23.setStyleSheet("background: #B2B1B9")
        else:
            self.button_23.setStyleSheet("background:" + (colorchoice_23))
        
        tree[24].color = Color(colorchoice_24)
        if colorchoice_24 == "black":
                self.button_24.setStyleSheet("background: #B2B1B9")
        else:
            self.button_24.setStyleSheet("background:" + (colorchoice_24))        
    
####################################### Cycle 1 ###################################################
    def cycle_run(self):
        global colorchoice_0 
        global colorchoice_1 
        global colorchoice_2
        global colorchoice_3
        global colorchoice_4
        global colorchoice_5
        global colorchoice_6
        global colorchoice_7
        global colorchoice_8
        global colorchoice_9
        global colorchoice_10
        global colorchoice_11
        global colorchoice_12
        global colorchoice_13
        global colorchoice_14
        global colorchoice_15
        global colorchoice_16
        global colorchoice_17
        global colorchoice_18
        global colorchoice_19
        global colorchoice_20
        global colorchoice_21
        global colorchoice_22
        global colorchoice_23
        global colorchoice_24
        global range1
        global snooze_a
        global snooze_b
      
        led_off = "black"
        tree.off()
        
        tree[3].color = Color(colorchoice_3)
        
        for x in range(int(range1)):           
            print("Running Variation-1, Cycles Remaining: ", int(range1)-x-1, end="      \r")
            tree[0].color = Color(colorchoice_0)
            time.sleep(float(snooze_a))
            tree[24].color = Color(led_off)
            
            tree[1].color = Color(colorchoice_1)
            time.sleep(float(snooze_b))
            tree[0].color = Color(led_off)
            
            tree[2].color = Color(colorchoice_2)
            time.sleep(float(snooze_a))
            tree[1].color = Color(led_off)
            
            tree[4].color = Color(colorchoice_4)
            time.sleep(float(snooze_b))
            tree[2].color = Color(led_off)
            
            tree[5].color = Color(colorchoice_5)
            time.sleep(float(snooze_a))
            tree[4].color = Color(led_off)
            
            tree[6].color = Color(colorchoice_6)
            time.sleep(float(snooze_b))
            tree[5].color = Color(led_off)
            
            tree[7].color = Color(colorchoice_7)
            time.sleep(float(snooze_a))
            tree[6].color = Color(led_off)
            
            tree[8].color = Color(colorchoice_8)
            time.sleep(float(snooze_b))
            tree[7].color = Color(led_off)
            
            tree[9].color = Color(colorchoice_9)
            time.sleep(float(snooze_a))
            tree[8].color = Color(led_off)
            
            tree[10].color = Color(colorchoice_10)
            time.sleep(float(snooze_b))
            tree[9].color = Color(led_off)
            
            tree[11].color = Color(colorchoice_11)
            time.sleep(float(snooze_a))
            tree[10].color = Color(led_off)
            
            tree[12].color = Color(colorchoice_12)
            time.sleep(float(snooze_b))
            tree[11].color = Color(led_off)
            
            tree[13].color = Color(colorchoice_13)
            time.sleep(float(snooze_a))
            tree[12].color = Color(led_off)
            
            tree[14].color = Color(colorchoice_14)
            time.sleep(float(snooze_b))
            tree[13].color = Color(led_off)
            
            tree[15].color = Color(colorchoice_15)
            time.sleep(float(snooze_a))
            tree[14].color = Color(led_off)
            
            tree[16].color = Color(colorchoice_16)
            time.sleep(float(snooze_b))
            tree[15].color = Color(led_off)
            
            tree[17].color = Color(colorchoice_17)
            time.sleep(float(snooze_a))
            tree[16].color = Color(led_off)
            
            tree[18].color = Color(colorchoice_18)
            time.sleep(float(snooze_b))
            tree[17].color = Color(led_off)
            
            tree[19].color = Color(colorchoice_19)
            time.sleep(float(snooze_a))
            tree[18].color = Color(led_off)
            
            tree[20].color = Color(colorchoice_20)
            time.sleep(float(snooze_b))
            tree[19].color = Color(led_off)
            
            tree[21].color = Color(colorchoice_21)
            time.sleep(float(snooze_a))
            tree[20].color = Color(led_off)
            
            tree[22].color = Color(colorchoice_22)
            time.sleep(float(snooze_b))
            tree[21].color = Color(led_off)
            
            tree[23].color = Color(colorchoice_23)
            time.sleep(float(snooze_a))
            tree[22].color = Color(led_off)
            
            tree[24].color = Color(colorchoice_24)        
            time.sleep(float(snooze_b))            
            tree[23].color = Color(led_off)                       
            
        self.tree_off()
               
####################################### Cycle 2 ###################################################      
    def cycle2_run(self):
        global colorchoice_0 
        global colorchoice_1 
        global colorchoice_2
        global colorchoice_3
        global colorchoice_4
        global colorchoice_5
        global colorchoice_6
        global colorchoice_7
        global colorchoice_8
        global colorchoice_9
        global colorchoice_10
        global colorchoice_11
        global colorchoice_12
        global colorchoice_13
        global colorchoice_14
        global colorchoice_15
        global colorchoice_16
        global colorchoice_17
        global colorchoice_18
        global colorchoice_19
        global colorchoice_20
        global colorchoice_21
        global colorchoice_22
        global colorchoice_23
        global colorchoice_24
        global range2
        global snooze_c
        global snooze_d
        
        led_off = "black"
        tree.off()
        
        for x in range(int(range2)):           
            print("Running Variation-2, Cycles Remaining: ", int(range2)-x-1, end="      \r")   
            tree[0].color = Color(colorchoice_0)
            time.sleep(float(snooze_c))
            
            tree[1].color = Color(colorchoice_1)
            time.sleep(float(snooze_d))
            
            tree[2].color = Color(colorchoice_2)
            time.sleep(float(snooze_c))
            
            tree[3].color = Color(colorchoice_3)
            time.sleep(float(snooze_d))
            
            tree[4].color = Color(colorchoice_4)
            time.sleep(float(snooze_c))
            
            tree[5].color = Color(colorchoice_5)
            time.sleep(float(snooze_d))
            
            tree[6].color = Color(colorchoice_6)
            time.sleep(float(snooze_c))
            
            tree[7].color = Color(colorchoice_7)
            time.sleep(float(snooze_d))
            
            tree[8].color = Color(colorchoice_8)
            time.sleep(float(snooze_c))
            
            tree[9].color = Color(colorchoice_9)
            time.sleep(float(snooze_d))
            
            tree[10].color = Color(colorchoice_10)
            time.sleep(float(snooze_c))
            
            tree[11].color = Color(colorchoice_11)
            time.sleep(float(snooze_d))
            
            tree[12].color = Color(colorchoice_12)
            time.sleep(float(snooze_c))
            
            tree[13].color = Color(colorchoice_13)
            time.sleep(float(snooze_d))
            
            tree[14].color = Color(colorchoice_14)
            time.sleep(float(snooze_c))
            
            tree[15].color = Color(colorchoice_15)
            time.sleep(float(snooze_d))
            
            tree[16].color = Color(colorchoice_16)
            time.sleep(float(snooze_c))
            
            tree[17].color = Color(colorchoice_17)
            time.sleep(float(snooze_d))
            
            tree[18].color = Color(colorchoice_18)
            time.sleep(float(snooze_c))
            
            tree[19].color = Color(colorchoice_19)
            time.sleep(float(snooze_d))
            
            tree[20].color = Color(colorchoice_20)
            time.sleep(float(snooze_c))
            
            tree[21].color = Color(colorchoice_21)
            time.sleep(float(snooze_d))
            
            tree[22].color = Color(colorchoice_22)
            time.sleep(float(snooze_c))
            
            tree[23].color = Color(colorchoice_23)
            time.sleep(float(snooze_d))
             
            tree[24].color = Color(colorchoice_24)        
            time.sleep(float(snooze_c))            
            
            tree.off()
            
        self.tree_off()
        
####################################### Cycle 3 ###################################################
    def cycle3_run(self):
        global colorchoice_0 
        global colorchoice_1 
        global colorchoice_2
        global colorchoice_3
        global colorchoice_4
        global colorchoice_5
        global colorchoice_6
        global colorchoice_7
        global colorchoice_8
        global colorchoice_9
        global colorchoice_10
        global colorchoice_11
        global colorchoice_12
        global colorchoice_13
        global colorchoice_14
        global colorchoice_15
        global colorchoice_16
        global colorchoice_17
        global colorchoice_18
        global colorchoice_19
        global colorchoice_20
        global colorchoice_21
        global colorchoice_22
        global colorchoice_23
        global colorchoice_24
        global range3
        global snooze_e
        global snooze_f
        
        led_off = "black"
        tree.off()
        
        for x in range(int(range3)):           
            
            #print(range3, end="      \r")
            print("Running Variation-3, Cycles Remaining: ", int(range3)-x-1, end="      \r")
            #print("Cycle-3 ", (x))
            tree[0].color = Color(colorchoice_0)
            time.sleep(float(snooze_e))
            
            tree[1].color = Color(colorchoice_1)
            time.sleep(float(snooze_f))
            
            tree[2].color = Color(colorchoice_2)
            time.sleep(float(snooze_e))
            
            tree[3].color = Color(colorchoice_3)
            time.sleep(float(snooze_f))
            
            tree[4].color = Color(colorchoice_4)
            time.sleep(float(snooze_e))
            
            tree[5].color = Color(colorchoice_5)
            time.sleep(float(snooze_f))
            
            tree[6].color = Color(colorchoice_6)
            time.sleep(float(snooze_e))
            
            tree[7].color = Color(colorchoice_7)
            time.sleep(float(snooze_f))
            
            tree[8].color = Color(colorchoice_8)
            time.sleep(float(snooze_e))
            
            tree[9].color = Color(colorchoice_9)
            time.sleep(float(snooze_f))
            
            tree[10].color = Color(colorchoice_10)
            time.sleep(float(snooze_e))
            
            tree[11].color = Color(colorchoice_11)
            time.sleep(float(snooze_f))
            
            tree[12].color = Color(colorchoice_12)
            time.sleep(float(snooze_e))
            
            tree[13].color = Color(colorchoice_13)
            time.sleep(float(snooze_f))
            
            tree[14].color = Color(colorchoice_14)
            time.sleep(float(snooze_e))
            
            tree[15].color = Color(colorchoice_15)
            time.sleep(float(snooze_f))
            
            tree[16].color = Color(colorchoice_16)
            time.sleep(float(snooze_e))
            
            tree[17].color = Color(colorchoice_17)
            time.sleep(float(snooze_f))
            
            tree[18].color = Color(colorchoice_18)
            time.sleep(float(snooze_e))
            
            tree[19].color = Color(colorchoice_19)
            time.sleep(float(snooze_f))
            
            tree[20].color = Color(colorchoice_20)
            time.sleep(float(snooze_e))
            
            tree[21].color = Color(colorchoice_21)
            time.sleep(float(snooze_f))
            
            tree[22].color = Color(colorchoice_22)
            time.sleep(float(snooze_e))
            
            tree[23].color = Color(colorchoice_23)
            time.sleep(float(snooze_f))
            
            tree[24].color = Color(colorchoice_24)        
            time.sleep(float(snooze_e))            
            
            for y in permutation(25):
                
                time.sleep(float(snooze_f))
                tree[y].color = Color(led_off)            
                       
        self.tree_off()
        
####################################### Turn Tree Off #############################################        
    def tree_off(self):
        
        self.button_0.setStyleSheet("background:#B2B1B9")
        self.button_1.setStyleSheet("background:#B2B1B9")
        self.button_2.setStyleSheet("background:#B2B1B9")
        self.button_3.setStyleSheet("background:#B2B1B9")
        self.button_4.setStyleSheet("background:#B2B1B9")
        self.button_5.setStyleSheet("background:#B2B1B9")
        self.button_6.setStyleSheet("background:#B2B1B9")
        self.button_7.setStyleSheet("background:#B2B1B9")
        self.button_8.setStyleSheet("background:#B2B1B9")
        self.button_9.setStyleSheet("background:#B2B1B9")
        self.button_10.setStyleSheet("background:#B2B1B9")
        self.button_11.setStyleSheet("background:#B2B1B9")
        self.button_12.setStyleSheet("background:#B2B1B9")
        self.button_13.setStyleSheet("background:#B2B1B9")
        self.button_14.setStyleSheet("background:#B2B1B9")
        self.button_15.setStyleSheet("background:#B2B1B9")
        self.button_16.setStyleSheet("background:#B2B1B9")
        self.button_17.setStyleSheet("background:#B2B1B9")
        self.button_18.setStyleSheet("background:#B2B1B9")
        self.button_19.setStyleSheet("background:#B2B1B9")
        self.button_20.setStyleSheet("background:#B2B1B9")
        self.button_21.setStyleSheet("background:#B2B1B9")
        self.button_22.setStyleSheet("background:#B2B1B9")
        self.button_23.setStyleSheet("background:#B2B1B9")
        self.button_24.setStyleSheet("background:#B2B1B9")              

        tree.off()
        
####################################### Variation 1 Settings ######################################
    def variation1_settings(self):        
        global range1
        global snooze_a
        global snooze_b
        
        range1 = self.set_cycles.currentText()
        snooze_a = self.set_delay1.currentText()
        snooze_b = self.set_delay2.currentText()
        
        self.run_cycle.setText("Run-1")
        self.run_cycle.setStyleSheet("background: Red")
        self.set_1.setStyleSheet("background:lightgreen")
        
        self.label_cycles_1.setText(range1)
        self.label_delay1_1.setText(snooze_a)
        self.label_delay2_1.setText(snooze_b)
        
        self.label_cycles_1.setStyleSheet("color: red")
        self.label_delay1_1.setStyleSheet("color: red")
        self.label_delay2_1.setStyleSheet("color: red")
        
        self.start_btn.setStyleSheet("background: red")
####################################### Variation 2 Settings ######################################
    def variation2_settings(self):
        global range2
        global snooze_c
        global snooze_d
        
        range2 = self.set_cycles.currentText()
        snooze_c = self.set_delay1.currentText()
        snooze_d = self.set_delay2.currentText()    
        
        self.run_cycle_2.setText("Run-2")
        self.run_cycle_2.setStyleSheet("background: red")
        self.set_2.setStyleSheet("background:lightgreen")
        
        self.label_cycles_2.setText(range2)
        self.label_delay1_2.setText(snooze_c)
        self.label_delay2_2.setText(snooze_d)
        
        self.label_cycles_2.setStyleSheet("color: red")
        self.label_delay1_2.setStyleSheet("color: red")
        self.label_delay2_2.setStyleSheet("color: red")
        
        self.start_btn.setStyleSheet("background: red")
####################################### Variation 3 Settings ######################################
    def variation3_settings(self):
        global range3
        global snooze_e
        global snooze_f
        
        range3 = self.set_cycles.currentText()
        snooze_e = self.set_delay1.currentText()
        snooze_f = self.set_delay2.currentText()    
        
        self.run_cycle_3.setText("Run-3")
        self.run_cycle_3.setStyleSheet("background: red")
        self.set_3.setStyleSheet("background:lightgreen")
        
        self.label_cycles_3.setText(range3) 
        self.label_delay1_3.setText(snooze_e)
        self.label_delay2_3.setText(snooze_f)
        
        self.label_cycles_3.setStyleSheet("color: red")
        self.label_delay1_3.setStyleSheet("color: red")
        self.label_delay2_3.setStyleSheet("color: red")
       
        self.start_btn.setStyleSheet("background: red")
####################################### Reset Values ##############################################
    def reset_values(self):
        global range1
        global range2
        global range3
        global snooze_a
        global snooze_b
        global snooze_c
        global snooze_d
        global snooze_e
        global snooze_f
        
        range1 = 5
        snooze_a = 0
        snooze_b = 0   
        
        range2 = 5
        snooze_c = 0
        snooze_d = 0    
        
        range3 = 5
        snooze_e = 0
        snooze_f = 0
        
        self.run_cycle.setText("Variation-1")
        self.run_cycle.setStyleSheet("background: #f5f5f5")
        self.set_1.setStyleSheet("background: #f5f5f5")
        
        self.run_cycle_2.setText("Variation-2")
        self.run_cycle_2.setStyleSheet("background: #f5f5f5")
        self.set_2.setStyleSheet("background: #f5f5f5")
        
        self.run_cycle_3.setText("Variation-3")
        self.run_cycle_3.setStyleSheet("background: #f5f5f5")
        self.set_3.setStyleSheet("background: #f5f5f5")
        
        self.run_order_1.setCurrentText("None")
        self.run_order_1.setStyleSheet("background: #f5f5f5; color: black")
        
        self.run_order_2.setCurrentText("None")
        self.run_order_2.setStyleSheet("background: #f5f5f5; color: black")
        
        self.run_order_3.setCurrentText("None")
        self.run_order_3.setStyleSheet("background: #f5f5f5; color: black")
        
        self.start_btn.setStyleSheet("background: #f5f5f5")
        
        self.label_cycles_1.setText(str(range1))
        self.label_delay1_1.setText(str(snooze_a))
        self.label_delay2_1.setText(str(snooze_b))
        
        self.label_cycles_2.setText(str(range2))
        self.label_delay1_2.setText(str(snooze_c))
        self.label_delay2_2.setText(str(snooze_d))
        
        self.label_cycles_3.setText(str(range3))
        self.label_delay1_3.setText(str(snooze_e))
        self.label_delay2_3.setText(str(snooze_f))
        
        self.label_cycles_1.setStyleSheet("color: black")
        self.label_delay1_1.setStyleSheet("color: black")
        self.label_delay2_1.setStyleSheet("color: black")
        
        self.label_cycles_2.setStyleSheet("color: black")
        self.label_delay1_2.setStyleSheet("color: black")
        self.label_delay2_2.setStyleSheet("color: black")
        
        self.label_cycles_3.setStyleSheet("color: black")
        self.label_delay1_3.setStyleSheet("color: black")
        self.label_delay2_3.setStyleSheet("color: black")
        
####################################### Start Cycles ##############################################
    def start_btn_clicked(self):
        global select_1
        global select_2
        global select_3
        
        select_1 = self.run_order_1.currentText()
        select_2 = self.run_order_2.currentText()
        select_3 = self.run_order_3.currentText()
        
        
        if select_1 == "Variation-1":
            self.cycle_run()
    
        if select_1 == "Variation-2":
            self.cycle2_run()
        
        if select_1 == "Variation-3":
            self.cycle3_run()
        
        
        if select_2 == "Variation-1":
            self.cycle_run()
        
        if select_2 == "Variation-2":
            self.cycle2_run()
        
        if select_2 == "Variation-3":
            self.cycle3_run()
        
        
        if select_3 == "Variation-1":   
            self.cycle_run()
        
        if select_3 == "Variation-2":
            self.cycle2_run()
        
        if select_3 == "Variation-3":
            self.cycle3_run()
        
####################################### Exit Program ############################################## 
    def closeEvent(self, event):
        tree.off()
        QApplication.instance().quit()
        
####################################### Set GUI ###################################################

app = QtWidgets.QApplication([])      
window = treegui()
window.show()
sys.exit(app.exec())