import turtle              # 1. import the modules
import random


wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
finish_line = turtle.Turtle()

lance.color('red')
andy.color('blue')
finish_line.color('black')

lance.shape('turtle')
andy.shape('turtle')
finish_line.hideturtle()
finish_line.shape('classic')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
finish_line.up()

andy.goto(-100, 20)
lance.goto(-100, -20)
finish_line.goto(150, 40)
finish_line.down()
finish_line.goto(150, -40)

random_click = random.randrange(1, 5)

while True:

    andy_position = andy.xcor()
    lance_position = lance.xcor()

    andy.forward(random.randrange(1, 5))
    if andy_position >= 150:
        print("Andy Wins!")
        break

    lance.forward(random.randrange(1, 5))
    if lance_position >= 150:
        print("Lance Wins!")
        break


wn.exitonclick()
