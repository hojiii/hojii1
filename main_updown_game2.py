import random
from game_data import data
from art_updown import vs
from art_updown import logo
from replit import clear

def random_account():
  return random.choice(data)
#게임 데이터에서 랜덤 데이터 출력

def format_data(account):
  name = account["name"]#게임데이터 안의 name 이라는 정보 표기
  description = account["description"]
  country = account["country"]

  return f"{name}, {description}, {country}"
#  출력 데이터 설정
def check_answer(guess,a_follwer,b_follwer):
  if a_follwer > b_follwer:
    return guess == 'a'
  else :
    return guess == 'b'
#정답 체크 입력값이랑 동일한지 ture false 체크
    


def game():
  score = 0#스코어 전역
  a_account = random_account()
  b_account = random_account()
  play_game = True
  #출력문을 뭘 출력할지 선언
  while play_game:
    print(f"A : {format_data(a_account)}") #보여줄 데이터 프린트
    print(vs)
    print(f"B : {format_data(b_account)}")
  
    guess = input("'A' or 'B' : ").lower() #입력값 받기
    a_f_count = a_account["follower_count"]#팔로우수 선언
    b_f_count = b_account["follower_count"]
    answer = check_answer(guess,a_f_count,b_f_count)#정답 체크
  
    clear()
    print(logo)
    if answer : 
      score +=1
      print(f"정답입니다 스코어는{score}입니다")
    else :
      print("틀렸습니다")
      play_game = False
game()