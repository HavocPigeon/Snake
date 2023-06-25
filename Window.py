import turtle

class Window:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.title("OOP Snake")
        self.screen.bgcolor("#A6F562")
        self.screen.setup(width,height)
        self.screen.tracer(0)
        self.hud = turtle.Turtle()

    def drawHUD(self, score, score2):
        self.hud.clear()
        self.hud.color("black")
        self.hud.penup()
        self.hud.hideturtle()
        self.hud.goto(0,-400)
        self.hud.write("Score: %d High Score: %d" %(score, score2), font=("Courier", 22, "normal"), align="center")
        

