import turtle

#change background
turtle.Screen().bgcolor("black")

#configure pointer
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.setpos(-150, 150)
pen.pendown()

#draws koch fractal in a line
def koch_fractal(n, length):
    if n == 0:
        pen.forward(length)
    else:
        koch_fractal(n-1, length)
        pen.left(60)
        koch_fractal(n-1, length)
        pen.right(120)
        koch_fractal(n-1, length)
        pen.left(60)
        koch_fractal(n-1, length)

n = 3
length = 10

for i in range(3):
  koch_fractal(n, length)
  pen.right(120)


turtle.done()