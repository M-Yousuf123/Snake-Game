from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = self.read_score()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", ('Arial', 17, 'normal'))

    def read_score(self):

        with open("data.txt") as high:
            s = high.read()
        return int(s)

    def write_score(self):

        with open("data.txt", mode="w") as high:
            high.write(f"{self.score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ('Arial', 17, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def refresh_score(self):
        self.score += 1
        self.update_scoreboard()