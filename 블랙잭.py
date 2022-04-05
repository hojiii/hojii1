from art import logo
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
  card = random.choice(cards)
  return card

def coculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,com_score):
  if user_score == 21 and com_score == 21:
    return "게임에서 패배하였습니다."

  if user_score == com_score:
    return "무승부"
  elif user_score == 0:
    return "블랙잭으로 승리하였습니다"
  elif com_score == 0:
    return "상대가 블랙잭으로 인해 패배하였습니다."
  elif user_score>21:
    return "21이 넘어 패배하였습니다."
  elif  com_score>21:
    return "상대가 21이 넘어 승리하였습니다"
  elif user_score > com_score :
    return "당신이 승리하였습니다."
  else : 
    return "당신이 폐배하였습니다."

    
  

def paly_game():
  print(logo)
  user_cards = []
  com_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    com_cards.append(deal_card())
  while not is_game_over:
    user_score = coculate_score(user_cards)
    com_score = coculate_score(com_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {com_cards[0]}")
  
    if com_score == 0 or user_score == 0 or user_score>21:
      is_game_over = True
    else :
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        
      if user_should_deal == "y":
          user_cards.append(deal_card())
      else:
        is_game_over = True

  while com_score != 0 and com_score < 17 :
    com_cards.append(deal_card())
    com_score = coculate_score(com_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {com_cards}, final score: {com_score}")
  print(compare(user_score, com_score))

  while input("다시 게임을 진행 하시겠습니까? 'y' or 'n' : ") == "y" :
    paly_game()