#space invaders
#python2.7

import turtle
import math
import random

#setupscreen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space.gif")

#register the shapes
turtle.register_shape("xwing.gif")
turtle.register_shape("T.gif")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.setposition(-2250,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#creat player turtle
player = turtle.Turtle()
player.color("yellow")
player.shape("xwing.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#scoring
score = 0

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-300, 260)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", 
        font=("Arial", 14, "normal"))
score_pen.hideturtle()

playerspeed = 15
enemyspeed = 2
#choose number of enemies
number_of_enemies = 5

#create enemies to list
enemies = []

#add enemies
for i in range (number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("T.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready - bullet to fire
#fire - bullet ist firing
bulletstate = "ready"

def fire_bullet():
    #declare bulletstate as a global if needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"

        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 15)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) 
            + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else: 
        return False





#check collision bullet - enemy

#move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -290:
        x = -290
    player.setx(x)
  
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 290:
        x = 290
    player.setx(x)


#create keybindings

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main gameloop
while True:
    for enemy in enemies:
        #move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
    
        #move the enemy back and down
        if enemy.xcor() > 290:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -290:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1
            
    
        if isCollision(bullet, enemy):
            #Reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            
            #update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", 
                    font=("Arial", 14, "normal")) 
            
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over.")
            break

    #move the bullet
    if bulletstate == "fire":   
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #border checking bullet
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"
    

delay = raw_input("Press enter to finish.")
