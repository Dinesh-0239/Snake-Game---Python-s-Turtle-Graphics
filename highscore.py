from turtle import Turtle
import json

class Highscore(Turtle):
    def __init__(self,level):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x=20,y=-300)
        self.hideturtle()
        self.display_highscore(level)
        self.score = 0
    
    def get_highscore(self,level):
        with open("High_Score.json","r") as highscore:
            self.score = json.load(highscore)
        return self.score[level]
    
    def display_highscore(self,level):
        self.clear()
        with open("High_Score.json","r") as highscore:
            self.score = json.load(highscore)
        self.write(f"High Score = {self.score[level]}\n", align="center", font=("Courier", 14, "bold"))
    
    def update_highscore(self,level,score):
        with open("High_Score.json","r") as highscore:
            self.score = json.load(highscore)
        self.score[level] = score

        with open("High_Score.json","w") as highscore:
            json.dump(self.score,highscore)
        
        