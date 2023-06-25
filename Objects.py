import turtle, random
class Snake:
    def __init__(self):
        self.snake_head = turtle.Turtle()
        self.InitialiseSnake()
        self.snake_body = []

    def InitialiseSnake(self):
        self.snake_head.speed(0)
        self.snake_head.shape("square")
        self.snake_head.color("green")
        self.snake_head.shapesize(1.3)
        self.snake_head.penup()
        self.snake_head.goto(0,100)
        self.snake_head.direction = "stop"

    def go_up(self):
        if self.snake_head.direction != "Down":
            self.snake_head.direction = "Up"
            print("Going Up")

    def go_down(self):
        if self.snake_head.direction != "Up":
            self.snake_head.direction = "Down"
            print("Going Down")

    def go_right(self):
        if self.snake_head.direction != "Left":
            self.snake_head.direction = "Right"
            print("Going Right")

    def go_left(self):
        if self.snake_head.direction != "Right":
            self.snake_head.direction = "Left"
            print("Going Left")

    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            x = self.snake_body[i-1].xcor()
            y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(x,y)
        if self.snake_body != []:
            x = self.snake_head.xcor()
            y = self.snake_head.ycor()
            self.snake_body[0].goto(x,y)
        if self.snake_head.direction == "Up":
            y = self.snake_head.ycor()
            self.snake_head.sety(y+20)
        if self.snake_head.direction == "Down":
            y = self.snake_head.ycor()
            self.snake_head.sety(y-20)
        if self.snake_head.direction == "Right":
            x = self.snake_head.xcor()
            self.snake_head.setx(x+20)
        if self.snake_head.direction == "Left":
            x = self.snake_head.xcor()
            self.snake_head.setx(x-20)
          
    def update(self):
        self.move()
            
    def grow(self, grow):
        for i in range(grow):
            part = turtle.Turtle()
            part.speed(0)
            part.shape("square")
            part.color("green")
            part.penup()
            self.snake_body.append(part)

    def snake_die(self):
        self.snake_head.goto(0,0)
        print("--------\nNew Game\n--------\n")
        self.snake_head.direction = "stop"
        for part in self.snake_body:
            part.hideturtle()
        self.snake_body = []

    def head_and_body_coll_check(self):
        for part in self.snake_body:
            if part.distance(self.snake_head) < 20:
                print("\n--------You Died!--------\n Head and Body collision\n--------You Died!--------\n\n")
                return True

class Food:
    def __init__(self):
        self.food_tier = ["circle","triangle","square"]
        self.food_colour = ["red","blue","purple"]
        self.item = turtle.Turtle()
        self.item.speed(0)
        self.shap = random.choice(self.food_tier)
        self.col = random.choice(self.food_colour)
        self.item.shape(self.shap)
        self.item.color(self.col)
        self.item.penup()
        self.item.shapesize(0.50,0.50)
        self.item.goto(200, 0)
        self.move = False
      
    def set_move(self, decision):
        self.move = decision
        
    def relocate(self):
        if self.move == True:
            x = random.randint(-290, 290)
            round(x, 20)
            y = random.randint(-290, 290)
            round(y, 20)
            self.item.goto(x,y)
            self.shap = random.choice(self.food_tier)
            self.col = random.choice(self.food_colour)
            self.item.shape(self.shap)
            self.item.color(self.col)
            self.set_move(False)
      
    def update(self):
        self.relocate()
