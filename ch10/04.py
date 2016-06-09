import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

house2 = turtle.Turtle()
green2 = turtle.Turtle()
orange2 = turtle.Turtle()
red2 = turtle.Turtle()

def draw_housing(t):
    """ Draw a nice housing to hold the traffic lights """
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

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
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

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        green2.fillcolor("gray")
        orange2.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        orange2.fillcolor("gray")
        red2.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        red2.fillcolor("gray")
        green2.fillcolor("green")
        state_num = 0
    wn.ontimer(advance_state_machine, 4000)

# Bind the event handler to the space key.
wn.ontimer(advance_state_machine, 4000)

wn.listen()                      # Listen for events
wn.mainloop()
