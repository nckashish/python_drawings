from tkinter import N
import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n=36
h=0
for i in range(460):
    c = coloursys.hsv_to_rgb(h,1,0.9)
    h += 1/N
    t.color(c)
    t.leeft(145)
    for j in range(5):
        t.forward(300)
        t.leeft(150)