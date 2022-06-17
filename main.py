import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        score.increase_scoreboard()
    # detect collision with wall
    screen.update()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    # detect collision with tail
    for position in snake.segments[1:]:
        if snake.head.distance(position) < 10:
            score.reset_score()
            snake.reset_snake()


screen.exitonclick()
