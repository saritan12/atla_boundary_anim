#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:29:30 2020

@author: sarita
"""

import turtle # import turtle library
import random  # import random library
turtle.colormode(255)   # Set color mode for window

# Create a panel to draw on. 
panel = turtle.Screen()  # Name screen
w = 1048  # width of panel
h = 802  # height of panel'

panel.setup(width=w,height=h)  #set up boundaries
panel.setworldcoordinates(0, w, h, 0)  #set up orgin and corners

#This code sets the background picture of the panel by accessing files of your computer
# https://python-forum.io/Thread-Turtle-canvas-background

panel.screensize(w,h)
panel.bgpic('landscape.gif')
landscape=turtle.Turtle()  #Add turtle to ensure background appears
landscape.ht()  #Hide landscape turtle

#>>>>>>>>> FINISH PANEL SETUP <<<<<<<<<<<<#


#>>>>>>>>> CODE STARTS <<<<<<<<<<<<#

#Define turtles

aang = turtle.Turtle()  #Define turtle for Aang gif
sokka = turtle.Turtle()  #Define turtle for Sokka gif
momo = turtle.Turtle()  #Define turtle for Momo gif
appa = turtle.Turtle()  #Define turtle for Appa gif


#Sokka turtle to starting position

sokka.ht()  #Hide turtle
move_speed = 10  #Start Sokka move to position
sokka.up()
sokka.lt(90)
sokka.forward(421) 
sokka.lt(90)
sokka.forward(30)  #Finish Sokka move to position
image1 = 'sokka.gif'  #Create path for program access to image1
panel.addshape(image1)  #Add image to panel
sokka.shape(image1)  #Change Sokka turtle shape to gif
sokka.st()  #Show turtle in ready position


#Momo turtle to starting position

momo.ht()  #Hide turtle
momo.up()  #Start Momo move to starting position
momo.lt(90)
momo.forward(390)
momo.rt(90)
momo.forward(300)  #Finish Momo move to position

#This code allows the turtle head to be changed to a desired image
#https://blog.trinket.io/using-images-in-turtle-programs/

image2='momo.gif'  #Create path for program to access image2
panel.addshape(image2)  #Add image 2 to panel
momo.shape(image2)  #Change Momo turtle head to gif
momo.st()  #Show turtle in starting position


#Appa turtle to starting position

appa.ht()  #Hide turtle
appa.up()  #Start Appa move to starting position
appa.rt(90)
appa.forward(600)
appa.rt(90)
appa.forward(150)  #Finish Appa move to starting position
image3 = 'appa_cut.gif' #Create path for program to access image3
panel.addshape(image3)  #Add image 3 to panel
appa.shape(image3)  #Change turtle head to Appa gif
appa.st()  #Show Appa turtle image in starting position


#Aang turtle to starting position

aang.ht()  #Hide turtle
move_speed = 10  #Start Aang move to starting position
turn_speed = 10
aang.up() 
aang.lt(90)
aang.forward(150)  #Complete Aang move to starting position
image4 = 'aang_cut.gif'  #Create path for program to access image4
panel.addshape(image4)  #Add image 4 to panel
aang.shape(image4)  #Change turtle head to Anng gif
aang.st()  #Show Aang turtle in starting position



#This code allows the setting of bounce boundaries for your panel present throughout the proceeding while loop
#https://drive.google.com/drive/u/1/folders/1sPswJV7ZBH-mpBL2hf-nkOt0Wkp-aJuN

aang.seth(random.randint(0,360))  #Set angle of header to random integer
count= 0  # Define count for end of while loop
loop= True #Set loop as true to begin with for while loop

while(loop):  #Begin while loop
    aang.pen(speed=6)  #Change Aang pen speed for movement
    aang.forward(15)  #Change distance Aang will travel
    aangx = aang.xcor() #Define Aang x coordinate
    aangy = aang.ycor() #Define Aang y coordinate
    aang.goto(aangx,aangy) # Find new position of Aang
    direction = aang.heading() # Define current head location
      
    if aangx < -300: #Left boundary
        AOI = 0 - 2 * direction #use angle of incedence to set new direction
        aang.goto(-300,aangy) # go to boundary
        aang.seth(AOI) # change heading angle
  
    elif aangx > 300: #Right boundary
        AOI = 180 - 2 * direction #use angle of incedence to set new direction
        aang.goto(300,aangy)  #go to boundary
        aang.seth(AOI) #change heading angle
            
    elif aangy < -360: #Top boundary
        AOI = 270 - 2 * direction #use angle of incedence to set new direction
        aang.goto(aangx,-360) #go to boundary
        aang.seth(AOI)  #change heading angle
       
       
    elif aangy > 360: #Bottom boundary
        AOI = 90 - 2 * direction #use angle of incedence to set new direction
        aang.goto(aangx,360)  #go to boundary
        aang.seth(AOI) #change heading angle
       
    else:
        continue #otherwise continue with loop
       
    if count >= 8: #set repition of while loop to 8
        loop = False #if greater, loop = False
        
    else:
        count = count + 1  # otherwise increase count by one if count is less that eight
        
        
        
#Bring aang back to origin        
aang.pen(speed=4)  #Change aang pen speed 
aang.goto(0,0)  #Bring aang turtle back to origin
        

#Momo movement for loop
for i in range(2):  #Momo for loop
  momo.pen(speed = 1) #momo pen speed
  momo.forward(300) #momo for loop movement start
  momo.ht()
  momo.pen(speed = 10)
  momo.goto(-600,390)
  momo.st()
  momo.pen(speed=1)
  momo.goto(300,390)
  

#Sokka movement for loop
sokkay = sokka.ycor() #Maintain Sokka y coordinate at current position
for i in range(8):
    sokkax = random.randint(-360,150) #Change Sokka x coordinate to random integer
    sokka.goto(sokkax,sokkay) #Go to random x location on y coordinate line
     

#Appa air movement
appa.pen(speed = 2) #Change appa pen speed to slower speed
appa.rt(180) #Turn head facing right forward
appa.forward(530)  #Move forward 530 spaces out of panel
appa.ht() #Hide turtle
appa.goto(-495,-600) #Bring turtle to left out of panel to creat wrap around effect
appa.st() #Show turtle
appa.goto(-28,-600) #Bring appa back to original position in panel


#End program
 



    

