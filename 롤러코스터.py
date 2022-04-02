print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
bill=0
if height >= 120:
  age= int(input("what is your age?"))
  if age<12:
    print("You should pay 5 dolloar")
    bill=5
  elif age<=18:
    print("You should pay 7 dolloar")
    bill=7
  elif age>=45 and age<=55:
    print("Free")
  else:
    print("You should pay 12 dolloar")
    bill=12
  wants_photo=input("Do you want a photo takes? Y or N")
  if wants_photo == "Y":
    bill+=3
  print(f"your final bill is{bill}.")
    
else:
  print("Sorry, you have to grow taller before you can ride.")


