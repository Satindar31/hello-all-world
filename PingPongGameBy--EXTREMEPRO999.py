#This is a game made by extremepro999
#this game is opensource
#you can make as many changes as you want but you cant remove these lanes or edit them
#Thank You ! 🙏

import turtle

wn = turtle.Screen()
wn.title("Ping Pong Gme By EXTREMEPRO999")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#padle_a
padle_a = turtle.Turtle()
padle_a.speed(0)
padle_a.shape("square")
padle_a.color("white")
padle_a.shapesize(stretch_wid=5, stretch_len=1)
padle_a.penup()
padle_a.goto(-350, 0)
input("promt")

#padle_b


#main game loop
while true:
    wn.update()
