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

def polydraw(t, n, s): #turtle, num of sides, size
    for i in range(n):
        t.forward(s)
        t.left(360 / n)

def spiral(t, l, n, a): #turtle, increment, num of spins, angle
    init_f = 0
    for i in range(n):
        t.forward(init_f)
        t.left(-90 + a)
        init_f = init_f + l

wn = windowmake("lightblue", "Fifth one")
jeff = turtlemake("black", 2)

##jeff.left(180)
##for i in range(20):
##    polydraw(jeff, 4, 50)
##    jeff.left(-18)

john = turtlemake("white", 2)
john.speed(0)
john.penup()
john.forward(200)
john.pendown()
spiral(john, 5, 80, 1)
jeff.speed(0)
jeff.penup()
jeff.forward(-200)
jeff.pendown()
spiral(jeff, 5, 80, 0)

wn.mainloop()
