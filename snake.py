from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_SHAPE = "circle"
SNAKE_COLOR = "white"
class Snake:
    def __init__(self):
        """Intialise frame for snake body"""
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]
        self.snake_tail = self.snake_body[-1]
    def create_snake(self):
        "Creating snake body"
        for position in POSITIONS:
            temp = Turtle(shape=SNAKE_SHAPE)
            temp.color(SNAKE_COLOR)
            temp.penup()
            temp.goto(position)
            self.snake_body.append(temp)
    def move(self):
        """Move snake"""
        for i in range(len(self.snake_body) - 1, 0, -1):
            tempx = self.snake_body[i - 1].xcor()
            tempy = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x=tempx, y=tempy)
        self.snake_head.forward(MOVE_DISTANCE)

    def extend_snake(self,position):
        """Increase snake body after eating food"""
        temp = Turtle(shape=SNAKE_SHAPE)
        temp.color(SNAKE_COLOR)
        temp.penup()
        temp.goto(position)
        self.snake_body.append(temp)
    def grow_snake(self):
        """increasing snake body"""
        self.extend_snake(self.snake_tail.position())
    def up(self):
        """Directing Snake Up side"""
        if int(self.snake_head.heading()) != DOWN:
            self.snake_head.setheading(UP)
    def down(self):
        """Directing Snake Down side"""
        if int(self.snake_head.heading()) != UP:
            self.snake_head.setheading(DOWN)
    def left(self):
        """Directing Snake Left side"""
        if int(self.snake_head.heading()) != RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        """Directing Snake Right side"""
        if int(self.snake_body[0].heading()) != LEFT:
            self.snake_head.setheading(RIGHT)