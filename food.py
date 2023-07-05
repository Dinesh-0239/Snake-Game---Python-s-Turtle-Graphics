from turtle import Turtle
from random import randint
FOOD_SHAPE = "square"
FOOD_COLOR = "green"

class Food(Turtle):
#    meal_no = 0
    def __init__(self,snake_body):
        """Initialising Food"""
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.new_food(snake_body)
    def new_food(self, snake_body):
        """Placing Food in the screen"""
        food_x = randint(-280,280)
        food_y = randint(-280,280)
        for snake in snake_body:
            dist = snake.distance(x=food_x,y=food_y)
            while dist < 20:
                food_x = randint(-280, 280)
                food_y = randint(-280, 280)
                dist = snake.distance(x=food_x, y=food_y)
        self.hideturtle()
        self.goto(x=food_x,y=food_y)
        self.showturtle()

