from turtle import *


speed(30)
width(7)

#HOuse

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#door


left(90)
forward(70)
color("green")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
goto(200,200)
pendown()

#roof

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(130,125)
pendown()
color("pink")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
penup()
left(90)
forward(60)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()








exitonclick()
