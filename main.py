import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #차랑 충돌했을때
    for car in car_manager.all_cars:
        if car.distance(player)< 20:
            game_is_on = False
            scoreboard.game_over()

        #결승선에 도착했을떄
        if player.finish_line():
            player.go_to_star()
            car_manager.level_up()
            scoreboard.increate_level()



screen.exitonclick()