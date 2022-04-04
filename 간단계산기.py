from art_coculatr import logo
def add(n1,n2):
  return n1 + n2#반환

def Subtract(n1,n2):
  return n1 - n2

def Multiply(n1,n2):
  return n1 * n2

def Divide(n1,n2):
  return n1 / n2

operation = {
  "+" : add,
  "-" : Subtract,
  "*": Multiply,
  "/": Divide,
}
def calculator():#재귀함수 
  print(logo)
  num1 = float(input("What's the frist number?: "))
  for symbol in operation:
    print(symbol)#opertation안의 키값 출력
  should_continue= True
  while should_continue:
    operation_symbol= input("원하는 연산을 고르세요: ")
    num2 = float(input("What's the next number?: "))
    caculation_funtion = operation[operation_symbol]#계산방식 설정
    answer = caculation_funtion(num1,num2)#답설정
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"{answer}값에서 계속하실꺼면 'y',초기화는 'c': ") == "y":
      num1 = answer
    else:
      should_continue : False
      calculator()
calculator()