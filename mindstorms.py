import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")

    #draw_square()
    #draw_circle()
    #draw_triangle()
    #draw_art()
    draw_flower()
    window.exitonclick()

def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)

def draw_line(some_line):
    for i in range(1,2):
        some_line.right(90)
        some_line.forward(300)

def draw_flower():
    rhombus = turtle.Turtle()
    rhombus.shape("turtle")
    rhombus.color("Red")
    rhombus.speed(2)
    for i in range (1, 37):
        draw_rhombus(rhombus)
        rhombus.right(10)
    for i in range (37, 38):
        draw_line(rhombus)
        
'''
def draw_art():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(2)
    for i in range(1,37):
        loop=0
        while(loop<4):
            brad.forward(100)
            brad.right(90)
            loop = loop+1
        brad.right(10)


def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(2)
    loop=0
    while(loop<4):
        brad.forward(100)
        brad.right(90)
        loop = loop+1
    brad.right(10)
        
def draw_circle():
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.circle(100)

def draw_triangle():
    rob = turtle.Turtle()
    rob.color("red")
    rob.shape("turtle")
    loop1 = 0
    while(loop1<4):
        rob.forward(100)
        rob.right(120)
        loop1 = loop1+1
'''
draw_shapes()
