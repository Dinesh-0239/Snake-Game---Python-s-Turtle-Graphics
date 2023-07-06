#-----------------------------------------------------------------------------------------------------------------
#***-------------------------------------------------Snake's Survival-----------------------------------------------***
"""
Date:-  05/07/2023
Developer:-  Dinesh Singh from Allahabad

Description of the game:- This game is based on classical snake game which pre-installed in keypad phone. In this game
you have to Control a snake by arrow keys on the keyboard. Your goal is to eat as much as food you can by avoiding the
snake from hitting the wall and hitting snake's own body.

Technology Used:-  This project is build using OPPs feature of Python and  Python's Turtle Graphics.
"""
#-----------------------------------------------------------------------------------------------------------------
# TODO 1(a) : Importing Necessary Module
from snake import Snake
from turtle import Screen
from time import sleep
from food import Food
from scoreboard import Scoreboard
#-----------------------------------------------------------------------------------------------------------------
# TODO 1(b): Creating Constant
LEFT_BOUNDARY = -290
RIGHT_BOUNDARY = 290
TOP_BOUNDARY = 290
BOTTOM_BOUNDARY = -290
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PLAYGROUND_COLOR = "black"
#-----------------------------------------------------------------------------------------------------------------
#TODO 2 (a) Setup Screen for snake game
playground = Screen()
playground.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
playground.title("Snake's Survival")
playground.bgcolor(PLAYGROUND_COLOR)
playground._root.iconbitmap("snake.ico")
playground.cv._rootwindow.resizable(False,False)
playground.tracer(0) #Animation is off until we call update()
#-----------------------------------------------------------------------------------------------------------------
# TODO 11: intilising snake speed. increase amount and points
game_level = {"easy":[0.3,1],"normal":[0.1,3],"hard":[0.08,5]}
#-----------------------------------------------------------------------------------------------------------------
# TODO 12: asking user for game difficulty
difficulty = ""
while difficulty not in list(game_level.keys()):
    difficulty = playground.textinput("Difficulty level","Select a difficulty level: easy/normal/hard: ").lower()
snake_speed = game_level[difficulty][0]
add_points = game_level[difficulty][1]
#-----------------------------------------------------------------------------------------------------------------
#TODO 3: Creating a snake body
snake = Snake()
#-----------------------------------------------------------------------------------------------------------------
#TODO 6: Putting the food
food = Food(snake.snake_body)
#-----------------------------------------------------------------------------------------------------------------
#TODO 8: Creating score board
scoreboard = Scoreboard()
#-----------------------------------------------------------------------------------------------------------------
#TODO 5: Controlling the Snake
playground.listen()
playground.onkey(fun=snake.up,key="Up")
playground.onkey(fun=snake.down,key="Down")
playground.onkey(fun=snake.left,key="Left")
playground.onkey(fun=snake.right,key="Right")
#-----------------------------------------------------------------------------------------------------------------
#TODO 4: Move the snake
game_is_on = True
while game_is_on:
    playground.update()
    sleep(snake_speed)
    snake.move()
    #TODO 7: Detect the collision of the snake with food
    if snake.snake_head.distance(food) < 20 :
        food.new_food(snake.snake_body)
        snake.grow_snake()
        scoreboard.get_scoreboard(add_points)
    #TODO 9: Detect Collision with wall
    if snake.snake_head.xcor() > RIGHT_BOUNDARY or snake.snake_head.xcor() < LEFT_BOUNDARY or snake.snake_head.ycor() > \
            TOP_BOUNDARY or snake.snake_head.ycor() < BOTTOM_BOUNDARY:
        game_is_on = False
        scoreboard.game_over()
    #TODO 10: Detect Collision with snake body
    for body in snake.snake_body[1:]:
        if snake.snake_head.distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()
#-----------------------------------------------------------------------------------------------------------------
# TODO 2 (b):- Hoding the screen
playground.exitonclick()
#-----------------------------------------------------------------------------------------------------------------
