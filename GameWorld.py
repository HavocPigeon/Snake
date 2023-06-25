from Window import *
from Objects import *
import time, random

scores = []
file = open("Scores.txt", "r")
for line in file:
    scores.append(line.strip())
file.close()

HEIGHT = WIDTH = 800
LEFT = WIDTH * -0.5
RIGHT = WIDTH * 0.5
TOP = HEIGHT * 0.5
BOTTOM = HEIGHT * -0.5

class Game:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.snake = Snake()
        self.food = Food()
        self.player_score = 0
        self.high_score = int(scores[0])
        self.val3 = 0
        self.val2 = 0
        self.growVal = self.val3*self.val2


    def keyboardListener(self):
        self.window.screen.listen()
        self.window.screen.onkey(self.snake.go_up, "Up")
        self.window.screen.onkey(self.snake.go_down, "Down")
        self.window.screen.onkey(self.snake.go_right, "Right")
        self.window.screen.onkey(self.snake.go_left, "Left")

    def world_update(self):
        if self.food.shap == "circle":
            self.val3 = 1
        elif self.food.shap == "triangle":
            self.val3 = 2
        elif self.food.shap == "square":
            self.val3 = 3
        if self.food.col == "red":
            self.val2 = 1
        elif self.food.col == "blue":
            self.val2 = 2
        elif self.food.col == "purple":
            self.val2 = 3
        self.growVal = self.val3*self.val2
        if self.snake.snake_head.distance(self.food.item) < 15:
          self.food.set_move(True)
          self.player_score += self.growVal
          self.snake.grow(self.growVal)
          self.snake.move()
        condition1 = self.snake.snake_head.xcor() > RIGHT
        condition2 = self.snake.snake_head.xcor() < LEFT
        condition3 = self.snake.snake_head.ycor() > TOP
        condition4 = self.snake.snake_head.ycor() < BOTTOM
        if condition1 or condition2 or condition3 or condition4:
            if condition1:
                self.snake.snake_head.setx(LEFT)
            if condition2:
                self.snake.snake_head.setx(RIGHT)
            if condition3:
                self.snake.snake_head.sety(BOTTOM)
            if condition4:
                self.snake.snake_head.sety(TOP)

        if self.snake.head_and_body_coll_check() == True:
            self.snake.snake_die()
            if self.player_score > self.high_score:
                self.high_score = self.player_score
            self.player_score = 0
            file = open("Scores.txt", "w")
            file.write(str(self.high_score))
            file.close()



        self.window.drawHUD(self.player_score, self.high_score)

    def RunGame(self):

        while True:
            self.window.screen.update()
            self.keyboardListener()
            self.snake.update()
            self.food.update()
            self.world_update()
            try:
                if 1/len(self.snake.snake_body) > 0.5:
                    time.sleep(0.5)
                else:
                    time.sleep(1/len(self.snake.snake_body))
            except:
                time.sleep(0.5)

game = Game()


game.RunGame()
