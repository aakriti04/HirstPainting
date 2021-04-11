#import colorgram

#colors = colorgram.extract('img.png',30)
#colors_list=[]
#for color in colors:
#    colors_list.append((color.rgb.r,color.rgb.g,color.rgb.b))

#print(colors_list)
import turtle as turtle_module
import random

rgb_colors_list =[(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tiny = turtle_module.Turtle()

tiny.hideturtle()
turtle_module.colormode(255)
turtle_module.screensize(1000, 1000)
yCord = 0
tiny.penup()
for _ in range(10):
    for _ in range(10):
        tiny.dot(20, random.choice(rgb_colors_list))
        tiny.forward(50)
    tiny.home()
    yCord += 50
    tiny.sety(yCord)
    tiny.left(90)
    tiny.right(90)

tiny.home()

screen=turtle_module.Screen()
screen.exitonclick()
