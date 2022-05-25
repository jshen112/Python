from random import random
import turtle as t
import os

  
#create a window and declare a variable called window and call the screen()
window=t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)
  
#Creating the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)
  
#Creating the right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)
  
#Code for creating the ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
  
#Code for creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',20,'normal'))

button = t.Turtle()

#code for moving the leftpaddle
def leftpaddleup():
    if leftpaddle.ycor() < 290:
        leftpaddle.sety(leftpaddle.ycor() + 45)
  
def leftpaddledown():
    if leftpaddle.ycor() > -290:
        leftpaddle.sety(leftpaddle.ycor() - 45)
  
#code for moving the rightpaddle
def rightpaddleup():
    rightpaddle.sety(rightpaddle.ycor() + 15)
  
def rightpaddledown():
    rightpaddle.sety(rightpaddle.ycor() - 15)
  
#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
#window.onkeypress(rightpaddleup,'Up')
#window.onkeypress(rightpaddledown,'Down')

def playGame(x,y):
    button.clear()
    if x < 0:
        level = 1
    elif x < 50:
        level = 2
    else:
        level = 3
    print("Level=", level)
    
    playerAscore=0
    playerBscore=0
    ballxdirection=1
    ballydirection=1
    while True:
        window.update()
        #moving the ball
        ball.setx(ball.xcor()+ballxdirection)
        ball.sety(ball.ycor()+ballydirection)
    
        #border set up
        if ball.ycor()>290:
            ball.sety(290)
            ballydirection *= -1

        if ball.ycor()<-290:
            ball.sety(-290)
            ballydirection *= -1
            
        if ball.xcor() > 390:
            ball.goto(0,0)
            ballxdirection *= -1
            playerAscore += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',20,"normal"))
        # os.system("afplay wallhit.wav&")
    
        if ball.xcor() < -390: # Left width paddle Border
            ball.goto(0,0)
            ballxdirection *= -1
            playerBscore  += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',20,"normal"))
        # os.system("afplay wallhit.wav&")

        # Handling the collisions with paddles.
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40:
            ball.setx(340)
            ballxdirection *= -1
            #os.system("afplay paddle.wav&")
    
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40:
            ball.setx(-340)
            ballxdirection *= -1
            #os.system("afplay paddle.wav&")
        
        #AI for right paddle
        if random() < random() * level/3:
            if ball.ycor() < rightpaddle.ycor() - 45:
                rightpaddledown()
            if ball.ycor() > rightpaddle.ycor() + 45:
                rightpaddleup()

FONT = ('Arial', 20, 'bold')

button.hideturtle()
button.penup()
button.goto(0, 50)
button.write("Level:   Easy          Medium             Hard", align='center', font=FONT)
window.onclick(playGame, 1, add=False)
window.mainloop()