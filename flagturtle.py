import turtle
turtle.getscreen().bgcolor("black")
godard = turtle.Turtle()
godard.color("white",'brown')
turtle.title("B-W Indian Flag ARD")

godard.speed(5)

godard.hideturtle()
godard.penup()
godard.right(90)
godard.forward(200)
godard.right(90)
godard.forward(200)
godard.left(90)

godard.pendown()
godard.left(180)
godard.forward(500)
godard.right(90)
godard.forward(400)
godard.right(90)
godard.forward(270)
godard.right(90)
godard.forward(370)
godard.left(90)
godard.forward(230)
godard.right(90)
godard.forward(30)
godard.penup()
godard.backward(30)
godard.right(90)
godard.forward(230)
godard.pendown()
godard.forward(270)
godard.penup()
godard.right(90)
godard.forward(370)
godard.right(90)
godard.forward(90)
godard.pendown()
godard.right(90)
godard.forward(370)
godard.penup()
godard.left(90)
godard.forward(90)
godard.pendown()
godard.left(90)
godard.forward(370)
godard.penup()
godard.left(90)
godard.forward(90)
godard.left(90)
godard.forward(370/2)
godard.pendown()
r = 45
godard.circle(r)
godard.left(90)
for i in range(19):
    godard.forward(90)
    godard.left(170)




turtle.done() 
