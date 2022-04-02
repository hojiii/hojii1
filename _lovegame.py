# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name1=name1.lower()
lower_case_name2=name2.lower()
ture_count_name1=lower_case_name1.count("t") + lower_case_name1.count("u") + lower_case_name1.count("r") + lower_case_name1.count("e") 
ture_count_name2=lower_case_name2.count("t") + lower_case_name2.count("u") + lower_case_name2.count("r") + lower_case_name2.count("e")
Total_ture_count=ture_count_name1 + ture_count_name2

love_count_name1 = lower_case_name1.count("l")+lower_case_name1.count("o")+lower_case_name1.count("v")+lower_case_name1.count("e")
love_count_name2 = lower_case_name2.count("l")+lower_case_name2.count("o")+lower_case_name2.count("v")+lower_case_name2.count("e")
Total_love_count = love_count_name1 + love_count_name2
Love_score=str(Total_ture_count)+str(Total_love_count)
Love_score2=int(Love_score)
if (Love_score2)<10 or (Love_score2>90) :
  print(f"Your score is {Love_score2},you go together like coke and mentos.")
elif (Love_score2<=50) and (Love_score2>=40) :
  print(f"Your score is {Love_score2},you are alright together.")
else :
 print(f"Your score is {Love_score2}")
