# Number Guessing Game:
import random as r
from rich.console import Console
import time
import guess

def compare(result, guess):
    if (guess < result):
        print("Too low")
    elif (guess > result):
        print("Too High")
    
def number(difficulty):
    # console = Console()
    # console.clear()
    
    result = r.randint(1, 120)
        
    if (difficulty == 'easy'):
        for count in range(10, 0, -1):
            print(f"You have {count} attempts to guess the correct answer.")
            guess = int(input("Make a Guess: "))
            
            if (result == guess):
                print(f"Correct Guessed ✔️ -> Answer is {result}")
                break
            compare(result, guess)
        else:
            print("✨ Better Luck next time! ✨")
            print(f"Correct answer is {result}")
    
    elif (difficulty == 'medium'):
        for count in range(7, 0, -1):
            print(f"You have {count} attempts to guess the correct answer.")
            guess = int(input("Make a Guess: "))
            
            if (result == guess):
                print(f"Correct Guessed ✔️ -> Answer is {result}")
                break
            compare(result, guess)
        else:
            print("✨ Better Luck next time! ✨")
            print(f"Correct answer is {result}")
            
    else:
        for count in range(5, 0, -1):
            print(f"You have {count} attempts to guess the correct answer.")
            guess = int(input("Make a Guess: "))
            
            if (result == guess):
                print(f"Correct Guessed ✔️ -> Answer is {result}")
                break
            compare(result, guess)
        else:
            print("✨ Better Luck next time! ✨")
            print(f"Correct answer is {result}")

console = Console()
console.clear()
          
for t in range(10, 0, -1):
    print(guess.logo)
    
    print("Welcome to the Number Guessing Game")
    print("I am thinking a number between 1 to 120")
    
    print(f"Game start in {t} sec.")
    time.sleep(1)
    
    console = Console()
    console.clear()

print(guess.logo)
print(f"I had choose a number between 1 to 120. Now, your task is to guess it.")

start = input("Are you Ready? Type 'yes' or 'no' -> ").lower()

if (start == 'yes'):
    console = Console()
    console.clear()
    print(guess.logo)
    
    level = input("Choose a difficuly level. Type 'easy', 'medium', 'hard' -> ").lower()
    number(level)
else:
    print(" 😊 Run the program again to play the game 😊 ")