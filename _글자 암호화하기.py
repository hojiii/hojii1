alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):#이전 함수를 묶어서 정리
  end_text = ""#빈공간 최종 텍스트
  if cipher_direction == "decode":#디코드값일때
    shift_amount *= -1#만약 5일경우 곱하기-1을 하면 -5가됨
  for char in start_text:#스타트 텍스트에 케릭터 값을 반복했을때
    if char in alphabet:#케릭터값이 알파벳 안에 있다면
      position = alphabet.index(char)#위치는=알파벳 인덱스.(값안에 서의 위치를 봐주는 명령어)안에 케릭위치
      new_position = position + shift_amount
      end_text += alphabet[new_position]#최종 텍스트는 알파벳안에있는 새로운위치의 값을 더해간것
    else:
      end_text += char#알파벳안에없는 것일경우 ex 숫자 문자 공란등등
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_continue = True#계속할지의 대한 변수 설정후 
while should_continue:#should_continue값인 동안에는 아래 반복
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift=shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == 'no':#만약 결과가 no이면
    should_continue = False#변수를 False로 바꿔서 반복 종료
    print("GoodBye")