#Step 5
from replit import clear
import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list #행맨월드로부터 리스트 가져오는법
chosen_word = random.choice(word_list)#월드리스트에서 임의의 단어 고르기
word_length = len(chosen_word)#선택된 단어 개수

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []#빈공간으로 디스플레이를 잡음
for _ in range(word_length):#풀어쓰면 range(0,단어수-1)
    display += "_"#단어수만큼 디스플레이에 줄 추가

while not end_of_game:#엔드 게임이 안되는동안 아래 질문계속 반복
    guess = input("Guess a letter: ").lower()#대문자도 소문자로 받아드림
    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print("you already used letter")
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"you gussed {guess}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages)