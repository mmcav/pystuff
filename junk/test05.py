import turtle

def windowmake(c, t): #color, title
    w = turtle.Screen()
    w.bgcolor(c)
    w.title(t)
    return w #window

def turtlemake(c, s): #color, size
    t = turtle.Turtle()
    t.color(c)
    t.pensize(s)
    return t #turtle

def squaredraw(t, s): #turtle, size
    for i in range(4):
        t.forward(s)
        t.left(90)

def polydraw(t, n, s): #turtle, num of sides, size
    for i in range(n):
        t.forward(s)
        t.left(360 / n)

wn = windowmake("lightblue", "Third one")
jeff = turtlemake("black", 4)

siz = 20
for i in range(5):
#    squaredraw(jeff, siz)
    polydraw(jeff, 8, siz)
    siz = siz + 20
    jeff.penup()
    jeff.forward(-10)
    jeff.left(-90)
    jeff.forward(10)
    jeff.left(90)
    jeff.pendown()
    

wn.mainloop()
