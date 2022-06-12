import turtle as t
from time import sleep
from random import choice


class Snake:
    def __init__(self):

        self.screen = t.Screen()
        self.snake_segments = []
        self.x_pos = 0

    def spawn_snake(self, amount):
        for _ in range(amount):
            snake = t.Turtle(shape="square")
            snake.penup()
            self.snake_segments.append(snake)
            snake.color("gainsboro", "white")

    def move(self):
        self.screen.update()
        sleep(0.07)

        next_pos = self.snake_segments[0].pos()
        self.snake_segments[0].forward(20)

        for segment in self.snake_segments[1:]:
            current_pos = segment.pos()
            segment.goto(next_pos)
            next_pos = current_pos
            self.snake_segments[1].setheading(self.snake_segments[0].heading())

    def turn_up(self):
        if self.snake_segments[0].heading() == self.snake_segments[1].heading():
            if self.snake_segments[0].heading() != 270:
                self.snake_segments[0].setheading(90)

    def turn_down(self):
        if self.snake_segments[0].heading() == self.snake_segments[1].heading():
            if self.snake_segments[0].heading() != 90:
                self.snake_segments[0].setheading(270)

    def turn_left(self):
        if self.snake_segments[0].heading() == self.snake_segments[1].heading():
            if self.snake_segments[0].heading() != 0:
                self.snake_segments[0].setheading(180)

    def turn_right(self):
        if self.snake_segments[0].heading() == self.snake_segments[1].heading():
            if self.snake_segments[0].heading() != 180:
                self.snake_segments[0].setheading(0)

    def head_xcor(self):
        return self.snake_segments[0].xcor()

    def head_ycor(self):
        return self.snake_segments[0].ycor()

    def add_segment(self):
        for _ in range(1):
            snake = t.Turtle(shape="square")
            snake.goto(-500, 0)
            snake.penup()
            self.snake_segments.append(snake)
            snake.color("gainsboro", "white")

    def segments_position(self):
        coordinate_list = []
        coordinate_list.clear()
        for segment in self.snake_segments[1:]:
            x_coord = round(segment.xcor())
            y_coord = round(segment.ycor())
            x_y = (x_coord, y_coord)
            coordinate_list.append(x_y)
        return coordinate_list


class Food:
    def __init__(self):

        self.food = t.Turtle(shape="circle")
        self.food.penup()
        self.food.shapesize(0.5)
        self.food.color("white")
        self.food.goto(choice(range(-420, 420, 20)), choice(range(-280, 240, 20)))

    def food_xcor(self):
        return self.food.xcor()

    def food_ycor(self):
        return self.food.ycor()

    def goto_random_pos(self):
        self.food.goto(choice(range(-420, 420, 20)), choice(range(-280, 240, 20)))


class Scoreboard:
    def __init__(self):
        self.score = t.Turtle()
        self.score.color("white")
        self.score.hideturtle()
        self.score.setposition(0, 260)

        self.background = t.Turtle()
        self.background.color("dim gray")
        self.background.hideturtle()
        self.background.penup()
        self.background.setposition(-450, 300)
        self.background.speed(11)

        self.gameover = t.Turtle()
        self.gameover.hideturtle()
        self.gameover.color("white")

        self.gameover_screen = t.Screen()
        self.gameover_screen.tracer(0)

    def draw_background(self):

        self.background.pendown()
        self.background.begin_fill()
        for _ in range(2):
            self.background.forward(880)
            self.background.right(90)
            self.background.forward(47)
            self.background.right(90)
        self.background.end_fill()

    def show_score(self, score):

        self.score.clear()
        self.score.write(arg=f"Score: {score}", move=False, align="center", font=('Courier', 20, 'bold'))

    def game_over(self, score):
        sleep(0.2)
        self.gameover_screen.clearscreen()
        self.gameover_screen.bgcolor("black")
        self.draw_background()
        self.show_score(score)
        self.gameover.write(arg=f"Game Over", move=False, align="center", font=('Courier', 40, 'bold'))
        self.gameover_screen.update()
        sleep(2)
