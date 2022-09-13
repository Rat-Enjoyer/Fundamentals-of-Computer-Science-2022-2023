 #This is a comment
'''This is a comment too
 Flip a coin program
from random import choice, random 

#First method use random.random ()
#coin_flip_with_random = "Head" if random() > 0.5 else "Tails"

#Second method random.choice()
coin_flip_with_choice = choice(["Black Rat", "Brown Rat", "Kangaroo Rat","No Rat, Hamsters Rule -the evil league of hamsters", "Giant Rat", "Small Rat", "Two Rats", "Did you think you had escaped the league of Hamsters, no way. Get a hamster... join the dark side >:)", "Wood Rat", "Polynesian Rat"])
print (coin_flip_with_choice)'''
#Roll a dice 
#First import libraries
from random import randint
repeat = True 
while repeat :
  print("You Rolled" , randint (1,6))
  print("Do you want to try again?")
  repeat = ("y" or "yes") in input ().lower()
