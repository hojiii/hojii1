# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year%4!=0:
 print("평년")
elif year%100!=0:
 print("윤년")
elif year%400==0:
 print("윤년")
else:
 print("평년")


