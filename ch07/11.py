import turtle

wn = turtle.Screen()
wn.title("Drunk Pirate Again")

tess = turtle.Turtle()
tess.color("red")

for (i, j) in [(160, 20), (-43, 10), (270, 8), (-43, 12)]:
    tess.left(i)
    tess.forward(j)

wn.mainloop()
