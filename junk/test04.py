import turtle
wn = turtle.Screen()
#wn.bgcolor("lightgreen")      # Set the window background color
#wn.title("Hello, Tess!")      # Set the window title

tess = turtle.Turtle()
#tess.color("blue")            # Tell tess to change her color
#tess.pensize(3)               # Tell tess to set her pen width

#tess.forward(50)
#tess.left(90)
#tess.forward(50)

##wncolor = input("Set the bg color: ")
##wn.bgcolor(wncolor)
##wntitle = input("Set the window title: ")
##wn.title(wntitle)
##
##while True:
##    userinput = input("'Forward or left ('f' or 'l')? Press 'x' to stop.\n")
##    if (userinput == "x"):
##        print("Now close the window.")
##        break
##    if ((userinput == "f") or (userinput == "l")):
##        uservalue = int(input("Set the new value: "))
##    if (userinput == "f"):
##        tess.forward(uservalue)
##    if (userinput == "l"):
##        tess.left(uservalue)

##total = 0
##for j in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
##    tess.forward(100)
##    tess.left(j)
##    total = total + j
##final = total % 360
##print("Drunk pirate: ", final)

##tess.hideturtle()
##for j in range(5):
##    tess.forward(100)
##    tess.left(-144)
##print("Tess is a ", type(tess))

wn.bgcolor("lightgreen")
tess.shape("turtle")
tess.color("blue")
tess.pensize(5)
tess.penup()
tess.speed(0)
for j in range(12):
    tess.forward(70)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.left(180)
    tess.forward(100)
    tess.left(150)
tess.stamp()

wn.mainloop()
