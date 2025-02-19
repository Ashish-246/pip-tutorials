import turtle

def draw_star(t, length):
    t.begin_fill()
    t.forward(length)
    t.right(72)
    
    for _ in range(4):
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.left(72)
    
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.end_fill()

def draw_stars_in_circle(t, num, star_length, radius):
    for i in range(num):
        t.penup()
        t.goto(0, 0)
        angle = 360 / num * i
        t.setheading(angle)
        t.forward(radius)
        t.right(36)
        t.pendown()
        draw_star(t, star_length)
        t.penup()

drawer = turtle.Turtle()
drawer.speed(10)
drawer.fillcolor('navy')
drawer.color('navy')

star_num = int(input("Enter no. of stars: "))
draw_stars_in_circle(drawer, star_num, 100, 200)
turtle.done()