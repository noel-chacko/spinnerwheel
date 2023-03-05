import turtle
from tkinter import *
import random

root = Tk()
root.title("What to do?")
root.eval('tk::PlaceWindow . center')

label = Label(root, text="Enter choices seperated by commas")
label.pack()

entry = Entry(root, bg="black")
entry.pack()

def on_submit():
  global choices
  choices = entry.get()
  close = Label(root, text="Press close to close")
  close.pack()

submit = Button(root, text="Submit", command=on_submit)
submit.pack()

close = Button(root, text="Close", command=root.destroy)
close.pack()

root.mainloop()

choiceList = choices.split(",")

win = turtle.Screen()
win.title("What to do?")
win.setup(400,600)
win.bgcolor("white")
win.tracer(0)

colors = ['#F44B27','#37F18C','#37DAF1','#CA37F1',
          '#F1376A','#EAD52A','#2A56EA','#873EEA']
pickedColors = []

"""
Dog,Hello,Cat
"""
def draw_color_wheel(colors, radius, center=(0, 0)):
    heading, position = 90, (center[0] + radius, center[1])
    for i in range(len(choiceList)):
        pickedColors.append(colors[i])
    slice_angle = 360 / len(pickedColors)
    for color in pickedColors:
        turtle.color(color, color)
        turtle.penup()
        turtle.goto(position)
        turtle.setheading(heading)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius, extent=slice_angle)
        heading, position = turtle.heading(), turtle.position()
        turtle.penup()
        turtle.goto(center)
        turtle.end_fill()
"""
Dog,Cat,Hello,Pizza,Bread,Chicken,Cheese,Ice
"""

turtle.hideturtle()
turtle.up()
for i in range(len(choiceList)):
    ypos = 260 - (i*20)
    turtle.goto(-145,ypos)
    turtle.write(choiceList[i], font=("Verdana", 20, "bold"))

draw_color_wheel(colors, 150, center=(0, 0))

for i in range(len(pickedColors)):
    ypos = 260 - (i*20)
    turtle.up()
    turtle.goto(-170,ypos)
    turtle.color(pickedColors[i])
    turtle.begin_fill()
    for i in range(4):
      turtle.forward(20)
      turtle.right(90)
    turtle.end_fill()

circle = turtle.Turtle()
turtle.hideturtle()
circle.up()
circle.speed(10)
circle.color("white")
circle.width(5)
circle.setpos(0,-50)
circle.down()
win.tracer(1)
long = random.randint(600,890)
circle.circle(50,long)
circle.shape("circle")
for i in range(20):
    circle.color("white")
    circle.shapesize(.5)
    circle.stamp()
    circle.color("black")
    circle.shapesize(.5)
    circle.stamp()

turtle.done()