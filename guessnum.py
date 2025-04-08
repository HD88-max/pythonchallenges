# Write a Python Program to create a Guess the number game. You can use different modules and functions to create this game. Every time the user guesses wrong, drop a hint. You can drop additional hints as well.
import random
number = random.randint(0,100)
if number%2 == 0:
    hint = ("The number is even")
else:
    hint =("The number is odd")
if number >= 50:
    hint2 = ("The number is more than or equal to 50 ")
else:
    hint2 = ("The number is less than 50 ")
hint3 = number//10
while True:
    guess = int(input("Guess my number 0-100. "))
    if guess == number:
        print("You won!")
        break
    question = input("Do you want a hint?(yes for hint1, Yes for hin2 and ye for hint3) ")
    if question == "yes":
        print(hint)
    elif question == "Yes":
        print(hint2)
    elif question == "ye":
        print("The 3rd hint is that the number is in the",hint3 * 10,end="s.")
    else:
        print("Carry on")

    
    
