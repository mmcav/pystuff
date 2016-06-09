import turtle

def graphdraw(turt, inputlist):
    for (i, j) in inputlist:
        turt.left(i)
        turt.forward(j)

wn = turtle.Screen()
wn.title("Graphs!")

tess = turtle.Turtle()
tess.color("red")
tess.pensize(3)

#70.71, 100.00, 141.42
#test1 = [(45, 141.42), (90, 70.71), (90, 70.71), (90, 141.42), (135, 100), (90, 100), (90, 100), (90, 100)]
#test1 = [(-90, 100), (90, 100), (90, 100), (45, 70.71), (90, 70.71), (135, 100)]
#test1 = [(180, 100), (90, 100), (90, 100), (90, 100), (45, 70.71), (90, 70.71), (90, 141.42)]
#test1 = [(180, 100), (-90, 100), (-90, 100), (-90, 100), (135, 70.71), (90, 70.71), (0, 70.71), (90, 70.71), (0, 70.71), (90, 70.71)]
test1 = [(-45, 141.42), (135, 100), (90, 100), (90, 100), (-135, 70.71), (-90, 70.71), (0, 70.71), (-90, 70.71), (0, 70.71), (-90, 70.71), (-45, 100), (-135, 141.42)]

graphdraw(tess, test1)

wn.mainloop()