import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.pendown()
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write("  "+ str(height))
    else:
        t.penup()
        t.forward(-15)
        t.write("  "+ str(height))
        t.forward(15)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.penup()
    t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
#tess.color("blue", "red")
tess.pensize(3)
tess.penup()

xs = [48,-100,117,200,-10,240,160,260,220,-50]

for a in xs:
    if a >= 200:
        tess.color("blue", "red")
    elif a >= 100:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")
    draw_bar(tess, a)

wn.mainloop()
