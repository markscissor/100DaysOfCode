############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Draw function
def draw():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pick = cards[random.randint(0,12)]
    return pick

# Score checker
def score(deck):
    total = sum(deck)
    if total == 21 and len(deck) == 2:
        return 0
    if 11 in deck and total > 21:
        total -= 10
    return total

def print_score(player, comp):
    print(f"   Your final hand: {player}, final score: {score(player)}")
    print(f"   Computer's final hand: {comp}, final score: {score(comp)}")

def result(player_score, comp_score):
    if player_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# game
def play_game():
    clear()
    print(logo)
    player_cards = []
    comp_cards = []
    game_over = False

    for _ in range(2):
        # Player drawing cards
        player_cards.append(draw()) 
        # Computer drawing cards 
        comp_cards.append(draw())

    while not game_over:
        # Prompt for another card
        print(f"   Your cards: {player_cards}, current score: {score(player_cards)}")
        print(f"   Computers first card: {comp_cards[0]}")

        get_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        # Computer decides to draw or not depending on its current score
        while score(comp_cards) < 17 and score(comp_cards) != 0:
            comp_cards.append(draw())

        # Player draws card
        if get_another == 'y':
            player_cards.append(draw())
        else:
            game_over = True

        if score(player_cards) > 21 or score(comp_cards) > 21:
            game_over = True
        
    print_score(player_cards, comp_cards)
    print(result(score(player_cards), score(comp_cards)))


# Main program
respond = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while respond == 'y':
    play_game()
    respond = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
