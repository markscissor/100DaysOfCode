#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

EASY_TURNS = 10
HARD_TURNS = 5

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS

def check_ans(guess, answer, turns):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return -1
    elif guess < answer:
            print("Too low.")
            return turns - 1
    else:
            print("Too high.")
            return turns - 1

def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    answer = random.randint(1, 100)
    # Debugging code
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_ans(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif turns == -1:
            break
        else:
            print("Guess again.")


main()
