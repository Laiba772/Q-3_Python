import turtle
import random
import time

# Screen setup
wn = turtle.Screen()
wn.title("Turtle Game")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player setup
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Enemy setup
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(random.randint(-390, 390), random.randint(-290, 290))
enemy.setheading(random.randint(0, 360))
enemy.shapesize(stretch_wid=0.5, stretch_len=0.5)

# Game variables
score = 0
lives = 3
level = 1
enemy_speed = 2
start_time = time.time()

# Score display
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)

# Lives display
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("black")
lives_pen.penup()
lives_pen.hideturtle()
lives_pen.goto(-350, 260)

# Level display
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("black")
level_pen.penup()
level_pen.hideturtle()
level_pen.goto(350, 260)

# Timer display
timer_pen = turtle.Turtle()
timer_pen.speed(0)
timer_pen.color("black")
timer_pen.penup()
timer_pen.hideturtle()
timer_pen.goto(0, 230)

def update_display():
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    
    lives_pen.clear()
    lives_pen.write(f"Lives: {lives}", align="left", font=("Courier", 24, "normal"))
    
    level_pen.clear()
    level_pen.write(f"Level: {level}", align="right", font=("Courier", 24, "normal"))
    
    elapsed_time = int(time.time() - start_time)
    timer_pen.clear()
    timer_pen.write(f"Time: {elapsed_time}s", align="center", font=("Courier", 18, "normal"))

# Initial display update
update_display()

# Game Over display
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("black")
game_over_pen.penup()
game_over_pen.hideturtle()
game_over_pen.goto(0, 0)

# Movement functions
def move_left():
    x = player.xcor()
    x = max(x - 20, -390)
    player.setx(x)

def move_right():
    x = player.xcor()
    x = min(x + 20, 390)
    player.setx(x)

def move_up():
    y = player.ycor()
    y = min(y + 20, 290)
    player.sety(y)

def move_down():
    y = player.ycor()
    y = max(y - 20, -290)
    player.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

# Main game loop
game_running = True
while game_running:
    wn.update()

    # Move enemy
    enemy.forward(enemy_speed)

    # Check bounds and reset enemy
    if enemy.xcor() > 390 or enemy.xcor() < -390 or enemy.ycor() > 290 or enemy.ycor() < -290:
        enemy.setheading(random.randint(0, 360))
        enemy.goto(random.randint(-390, 390), random.randint(-290, 290))
        score += 1

        # Increase level every 5 points and speed up enemy
        if score % 5 == 0:
            level += 1
            enemy_speed += 0.5
        
        update_display()

    # Collision detection
    if player.distance(enemy) < 20:
        lives -= 1
        update_display()
        
        if lives == 0:
            player.hideturtle()
            enemy.hideturtle()
            game_over_pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
            wn.update()  # Draw final frame with game over text
            wn.exitonclick()  # Wait for user to click to close window
            game_running = False
        else:
            # Reset enemy position on collision
            enemy.setheading(random.randint(0, 360))
            enemy.goto(random.randint(-390, 390), random.randint(-290, 290))
    
    time.sleep(0.005)  # Roughly 60 FPS delay
