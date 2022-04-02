alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):
  cipher_text = ""
  for letter in plain_text:#입력 택스트안에 레터를 반복 
    position = alphabet.index(letter)#위치=레터 있는 알파벳의 자리 ->글자의 자리를 찾는 함수는 인덱스를사용
    new_position = position + shift_amount#새로운 자리는 포지션+이동할 수
    new_letter = alphabet[new_position]#새로운 글자는 =알파벳의 새로운 글자 자리 
    cipher_text+= new_letter#사이퍼 텍스트를 공란으로 주고 새로운 글자를 더해감
  print(f"The encoded text is {cipher_text}")

def decrypt(encode_text,shift_amount):
  decode_text=""
  for letter in encode_text:
    new_position = alphabet.index(letter)
    position = new_position - shift_amount
    new_letter = alphabet[position]
    decode_text += new_letter
  print(f"The decode text is {decode_text}")
a="encode"
b="decode"
if direction == a.lower():
  encrypt(text,shift)
elif direction == b.lower():
  decrypt(text,shift)
  
  #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
