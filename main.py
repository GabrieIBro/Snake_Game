import turtle as t
from classes import Snake, Scoreboard, Food


def gameloop():

    screen = t.Screen()
    screen.setup(width=880, height=600)
    screen.title("Snake")
    screen.bgcolor("black")
    screen.tracer(0)
    screen._root.resizable(False, False)

    snake = Snake()
    score = Scoreboard()
    food = Food()

    screen.listen()
    screen.onkeypress(fun=snake.turn_up,    key="w")
    screen.onkeypress(fun=snake.turn_left,  key="a")
    screen.onkeypress(fun=snake.turn_down,  key="s")
    screen.onkeypress(fun=snake.turn_right, key="d")

    score_count = 0

    snake.spawn_snake(3)
    score.draw_background()

    while True:
        score.show_score(score_count)
        snake.move()
        segments = snake.segments_position()

        if (food.food_xcor(), food.food_ycor()) in segments:
            food.goto_random_pos()

        elif food.food_xcor() == round(snake.head_xcor()) and food.food_ycor() == round(snake.head_ycor()):
            food.goto_random_pos()
            score_count += 1
            snake.add_segment()

        if (round(snake.head_xcor()), round(snake.head_ycor())) in segments:
            score.game_over(score_count)
            break

        if snake.head_xcor() < -425 or snake.head_ycor() < -285:
            score.game_over(score_count)
            break
        elif snake.head_xcor() > 425 or snake.head_ycor() > 245:
            score.game_over(score_count)
            break

    play_again = screen.textinput("GAME OVER!:", "Press OK to play again")
    if play_again in ' ':
        score.gameover_screen.clear()
        gameloop()


gameloop()
