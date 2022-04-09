from art import logo
from game_data import data
import random
from art import vs
from replit import clear
#가져온정보 보여주기 아래 데이터 가져 오기에게 보내줄려면 위에 작성되어야함
def format_data(account) :
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr} , from {account_country}"

def check_answer(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess =="a" #정답이 a이면 True 반환 아닐경우 False반환
  else : 
    return guess == "b"
#디스플래이 아트

print(logo)
score = 0
#반복하게 하기
Game_should_countinue = True
account_b = random.choice(data) #b 데이터를 랜덤함수로 출력후 이 데이터가 a가됨
while Game_should_countinue:
  #랜덤 데이터 가져오기
  account_a = account_b
  account_b = random.choice(data) 
  """어카운트 a가 b가 되고 b는 새로운 랜덤데이터를 출력하여 a가 위로 올라가게 변경 """
  if account_a == account_b:
    account_b = random.choice(data) #a와 b 출력값이 같을경우 재출력
  
  print(f"Compare A : {format_data(account_a)}.")
  print(vs)
  print(f"Compare B : {format_data(account_b)}.")  
  
  
  #유저에게 정답 물어보기
  guess = input("who has more followers Type 'A' or 'B'").lower()
  
  #유저가 맞췄는지 확인하기
  ##각자의 팔로워 나타내기
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  #유저가 선택한 정답의 대한 답변 하기
  clear()#클리어 위치가 위로 가면 와일문이 작동하자마자 데이터가 클리어됨으로 정답 판단을 못함 고로 정답 판단 밑으로 들어가야함
  print(logo)
  if is_correct:
    score +=1
    print(f"You're right! Current score : {score}")
    
  else : 
    Game_should_countinue = False
    print(f"sorry,that's wrong.Final score : {score}")

