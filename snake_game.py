from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
scoreboard = ScoreBoard()
snake = Snake()
food= Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#먹이를 먹었는지 확인코드
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()<-290:
        game_is_on = False
        scoreboard.game_over()

    #꼬리와 충돌감지
    for segment in snake.segments:#모든 세그먼트를 하나씩 반복해서 가져옴
        if segment == snake.head:#만약 세그먼트가 머리일경우는 패스
            pass
        elif snake.head.distance(segment)<10:#반복문을 실행시켰을때 첫번째 세그먼트가 머리임으로 바로 게임 종료가 됨으로 위의 이프문 필요
            game_is_on = False
            scoreboard.game_over()
    #만약 머리가 꼬리의 아무세그먼트와 충돌시:
        #게임종료













screen.exitonclick()
