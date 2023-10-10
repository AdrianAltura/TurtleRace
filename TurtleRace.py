import turtle
import random

run = False
color = ['red','blue','purple','yellow','green','brown']
screen = turtle.Screen()
screen.setup(width = 500, height=400)
all_turtle = []
user_bet = screen.textinput(title='Bet',prompt='Choose your Turtle. pick a color: ')
y = -75

for turtle_index in range(6):
  child = turtle.Turtle(shape='turtle')
  child.color(color[turtle_index])
  child.penup()
  child.goto(-230,y)
  y += 30
  all_turtle.append(child)

if user_bet:
  run = True

while run:

  for tur in all_turtle:
    if tur.xcor() > 230:
      run = False
      if tur.pencolor()== user_bet:
        print(f'you won! The winning turtle is color {tur.pencolor()}')
      else:
        print(f'you lose! The winning turtle is color {tur.pencolor()}')

    ran = random.randint(0,10)
    tur.fd(ran)






screen.exitonclick()