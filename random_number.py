import random

levels = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print(f"{guess}는 정답보다 큽니다")
        return turns-1
    elif guess < answer:
        print(f"{guess}는 정답보다 작습니다.")
        return turns-1
    else:
        print("축하합니다 정답입니다.")
    


def game_level():
    level = input(f"레벨을 선택해주세요 'hard' or  easy:  ").lower
    if level == "easy" :
        return levels+5
    else: 
        return levels
        


def play_game():
    print(f"랜덤숫자 맞추기에 오신걸 환영합니다.")
    print(f"1~100 중 랜덤 숫자를 맞춰 주세요")
    answer = random.randint(1,100)
    print(answer)

    
    turns = game_level()
    guess = 0
    while guess != answer:
        guess = int(input("숫자 입력 : "))
        print(f"정답을 맞추지 못해 남은 턴수가 {turns}입니다.")
        turns = check_answer(guess,answer,turns)
        
    if turns == 0 :
        print(f"기회가 다하여 게임에서 졌습니다.")
        regame = input(f"리게임을 하시겠습니까? 'y' or 'n'").lower
        if regame =='y' :
            play_game()

play_game()      
           