#trig_table.py
#CSCI 111-900
#Last edited 10/01/19

import math

degrees = 10 #Enters first degree value

while(degrees <= 90): #loops until it calculates values for all 10th degrees from 10 to 90
    sin = math.sin(math.radians(degrees))
    cos = math.cos(math.radians(degrees)) #calculates sin and cos values of the current degree value
    print("Angle: ")
    print(degrees)
    print("Sin: ")
    print(round(sin, 4))
    print("cos: ")
    print(round(cos, 4))
    degrees += 10 #Adds 10 degrees each loop
