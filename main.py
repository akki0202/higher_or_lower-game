import random
from game_data import data
import art

# print ascii
print(art.logo)

# selecting random item from data
i=random.randint(0,49)
j=random.randint(0,49)
to_continue=1
score=0
while to_continue==1 and i!=j: 
#printing the two random datas from dictionary
  print("Compare A: " + data[i]["name"] + ", a " + data[i]["description"] + ", from " + data[i]["country"])
  fA= data[i]["follower_count"]
  # print(fA)
  print(art.vs)
  fB= data[j]["follower_count"]
  print("Compare B: " + data[j]["name"] + ", a " + data[j]["description"] + ", from " + data[j]["country"])
  # print(fB)
  guess=input("Who has more followers? Type'A' or 'B': ")
#main code
  if guess=="A" or guess == "a":
    if fA>fB:
      score += 1
      print(f"You're right! current score: {score}")
      j=random.randint(1,49)
    else:
      print(f"Sorry that's wrong. final score: {score}") 
      to_continue=0
  elif guess=="B" or guess=="b":
    if fA<fB:
      score += 1
      print(f"You're right! current score: {score}")
      i=random.randint(2,49)
    else :
      print(f"Sorry that's wrong. final score: {score}")
      to_continue=0 
  else:
    print("Invalid response!")   
    to_continue=0


