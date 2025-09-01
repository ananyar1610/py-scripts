from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if(difficulty=='easy'):
    number_of_guesses=5
    print("You have 10 attempts remaining to guess the number.")

elif(difficulty=='hard'):
    number_of_guesses=10
    print("You have 5 attempts remaining to guess the number.")

else:
    print("Invalid input!!")
guess = int(input("Make a guess:"))
check=False
comp_choice=random.randint(1,101)
while(check==False):
    if guess==comp_choice:
        check=True
        print("You've got it. Congratulations!")
        break
    elif(guess>comp_choice):
        check=False
        print("Too high.")
        print("Guess again")
        guess = int(input("Make a guess:"))
        continue
    elif(guess<comp_choice):
        check=False
        print("Too low.\nGuess again.")
        guess = int(input("Make a guess:"))
        continue
    else:
        break
