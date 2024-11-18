from turtle import Turtle

with open("week4/Snake_Game/data.txt") as file:
    high_score_amount = int(file.read())
    

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0 # Starting score of 0
        self.high_score = high_score_amount
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score : {self.score} High score: {self.high_score}", align="center", font=("Arial", 22, "normal"))
        
        

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High score: {self.high_score}", align="center", font=("Arial", 22, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align="center", font=("Arial", 22, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("week4/Snake_Game/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0 # Reset the score
        self.update_score()

    def increase_score(self):
        self.score += 1 # Add one to score
        self.update_score()

