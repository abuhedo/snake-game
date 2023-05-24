import turtle
import random
import time
window = turtle.Screen()
window.tracer(0)
window.setup(width=600, height=600)
window.title("Sneak Gmae")
window.bgcolor("black")
delay = 0.1
score = 0
high_score = 0
class Snake():
    def __init__(self):
        self.snake = turtle.Turtle()
        self.snake.penup()
        self.snake.color("white")
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
           self.snake.setx(coord_x - 20)
        if self.snake.dirction == "right":
           coord_x = self.snake.xcor()
           self.snake.setx(coord_x + 20)
class Fruit():
    def __init__(self):
       self.fruit = turtle.Turtle()
       self.fruit.shape("circle")
       self.fruit.speed(0)
       self.fruit.color("white")
       self.fruit.penup()
       self.fruit.goto(0,200)
       self.fruit.direction = "stop"

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
snake1 = Snake()
window.listen()
turtle.Screen().onkeypress(snake1.go_up, "w")
turtle.Screen().onkeypress(snake1.go_down, "s")
turtle.Screen().onkeypress(snake1.go_left, "a")
turtle.Screen().onkeypress(snake1.go_right, "d")
fruit = Fruit()
segments = []
while True:
    window.update()
    if snake1.snake.xcor() > 290 or snake1.snake.xcor() < -290 or  snake1.snake.ycor() > 290 or  snake1.snake.ycor() < -290:
        time.sleep(1)
        snake1.snake.goto(0, 0)
        snake1.snake.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
        if snake1.snake.distance(fruit.fruit) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            fruit.fruit.goto(x, y)
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("black") 
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
            for index in range(len(segments)-1, 0, -1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)
            if len(segments) > 0:
                x = snake1.snake.xcor()
                y = snake1.snake.ycor()
                segments[0].goto(x, y)
            snake1.movment()
            for segment in segments:
                if segment.distance(snake1.snake) < 20:
                    time.sleep(1)
                    snake1.snake.goto(0, 0)
                    snake1.snake.direction = "stop"
                    colors = random.choice(['red', 'blue', 'green'])
                    shapes = random.choice(['square', 'circle'])
                    for segment in segments:
                        segment.goto(1000, 1000)
                    segments.clear()
                    score = 0
                    delay = 0.1
                    pen.clear()
                    pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
            time.sleep(delay) 
    window.mainloop()
