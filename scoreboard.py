from turtle import Turtle
class Scoreboard(Turtle):
    """Intialising Score Board"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x=0,y=250)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def get_score(self):
        return self.score
    
    def update_scoreboard(self):
        """Update Scoreboard"""
        self.write(f"Score = {self.score}\n", align="center", font=("Courier", 14, "bold"))
    def get_scoreboard(self,add_points):
        """Display Scoreboard"""
        self.score += add_points
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        """Display Game Over Msg"""
        self.home()
        self.color("red")
        self.write(f"Game Over", align="center", font=("Courier", 24, "bold"))
