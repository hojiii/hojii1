rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
#Write your code below this line 👇
import random
User_choice = int(input(f"what do you choose?Type 0 for Rock,1 for paper or 2 for Scissors."))
if User_choice>=3 or User_choice<0 :
  print("You typed an invaild number,you lose!")
else:  
 print(f"{game_image[User_choice]}")
 computer_choice = random.randint(0,2)
 print(f"computer choice is {game_image[computer_choice]}")
 if User_choice>=3 or User_choice<0 :
  print("You typed an invaild number,you lose!")
 elif User_choice==0 and computer_choice==2:
  print("You win")
 elif User_choice==2 and computer_choice==0:
  print("You lose")
 elif User_choice > computer_choice:
  print("You win")
 elif User_choice == computer_choice:
  print("You draw")
 elif computer_choice > User_choice:
  print("You lose")
 elif User_choice>=3 or User_choice<0 :
  print("You typed an invaild number,you lose!")