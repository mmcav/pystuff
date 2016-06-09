import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

tsize = 5
tess.pensize(tsize)

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def colorred():
    tess.color("red")

def colorgreen():
    tess.color("green")

def colorblue():
    tess.color("blue")

def turtleplus():
    global tsize
    if tsize < 20:
        tsize += 1
        tess.pensize(tsize)

def turtleminus():
    global tsize
    if tsize > 1:
        tsize -= 1
        tess.pensize(tsize)


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(colorred, "r")
wn.onkey(colorgreen, "g")
wn.onkey(colorblue, "b")

wn.onkey(turtleplus, "+")
wn.onkey(turtleminus, "-")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
