import turtle
turtle.Screen().setup(width=600, height=600)
turtle.title("Sneak Gmae")
class Snake():
    def __init__(self):
        self.snake = turtle.Turtle()
        self.snake.penup()
        self.snake.goto(0,0)
        self.snake.direction = "stop"
    def go_up(self):
        if self.snake.direction != "down":
           self.snake.dirction = "up"
    def go_down(self):
        if self.snake.direction != "up":
           self.snake.dirction = "down"
    def go_left(self):
        if self.snake.direction != "right":
           self.snake.dirction = "left"
    def go_right(self):
        if self.snake.direction != "left":
           self.snake.dirction = "right"

    def movment(self):
        if self.snake.direction == "up":
           coord_y = self.snake.ycor()
           self.snake.sety(coord_y + 20)
        if self.snake.direction == "down":
           coord_y = self.snake.ycor()
           self.snake.sety(coord_y - 20)
        if self.snake.dirction == "left":
           coord_x = self.snake.xcor()
           self.snake.setx(cord_x - 20)
        if self.snake.dirction == "right":
           coord_x = self.snake.xcor()
           self.snake.setx(cord_x + 20)
snake1 = Snake()
turtle.Screen().listen()
turtle.Screen().onkeypress(snake1.go_up, "Up")
turtle.Screen().onkeypress(snake1.go_down, "down")
turtle.Screen().onkeypress(snake1.go_left, "left")
turtle.Screen().onkeypress(snake1.go_right, "right")
