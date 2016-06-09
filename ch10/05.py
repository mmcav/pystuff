import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Patented traffic light!")
wn.bgcolor("lightgreen")

house2 = turtle.Turtle()
green2 = turtle.Turtle()
orange2 = turtle.Turtle()
red2 = turtle.Turtle()

def draw_housing(t):
    t.pensize(3)
    t.color("black", "darkgrey")
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(200)
    t.circle(40, 180)
    t.forward(200)
    t.left(90)
    t.end_fill()

def initposit2(t, color):
    t.penup()
    t.hideturtle()
    if color == "green":
        add = 0
    if color == "orange":
        add = 70
    if color == "red":
        add = 140
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(50+add)
    t.shape("circle")
    t.shapesize(3)
    if color == "green":
        t.fillcolor(color)
    else:
        t.fillcolor("gray")
    t.showturtle()

draw_housing(house2)
house2.hideturtle()
initposit2(green2, "green")
initposit2(orange2, "orange")
initposit2(red2, "red")

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:
        green2.fillcolor("green")
        orange2.fillcolor("orange")
        state_num = 1
        timer = 1000
    elif state_num == 1:
        green2.fillcolor("gray")
        orange2.fillcolor("orange")
        state_num = 2
        timer = 1000
    elif state_num == 2:
        orange2.fillcolor("gray")
        red2.fillcolor("red")
        state_num = 3
        timer = 2000
    else:
        red2.fillcolor("gray")
        green2.fillcolor("green")
        state_num = 0
        timer = 3000
    wn.ontimer(advance_state_machine, timer)


wn.ontimer(advance_state_machine, 4000)

wn.listen()
wn.mainloop()
