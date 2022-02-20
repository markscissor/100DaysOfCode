import random
import os
from art import logo, vs
from game_data import data

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def get_data():
    return random.choice(data)

def compare(data1, data2):
    if data1['follower_count'] > data2['follower_count']:
        return 1
    elif data1['follower_count'] < data2['follower_count']:
        return 2
    else:
        return 0

def print_vs(data1, data2):
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
    print(vs)
    print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}.")

def game():
    game_over = False
    data_a = get_data()
    data_b = data_a
    score = 0
    print(logo)

    while not game_over:


        # Get another data for B if they are same person
        while data_b == data_a:
            data_b = get_data()

        print_vs(data_a, data_b)
        result = compare(data_a, data_b)

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if result == 1 and guess == 'a':
            score += 1
        elif result == 2 and guess == 'b':
            score += 1           
        else:
            game_over = True
            break

        data_a = data_b
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
    
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


game()
