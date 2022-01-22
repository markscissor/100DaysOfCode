from replit import clear
#from art import logo --> commented out to get code in 1 file
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.
bids = {}
def bid_add():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

def get_highest():
    winner = ""
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            winner = bidder
            highest_bid = bids[bidder]
    
    return winner, highest_bid


# main program
print(logo)
ans = 'yes'
while ans == 'yes':
    bid_add()
    ans = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ans == 'yes':
        clear()

name_of_winner, bid_of_winner = get_highest()

print(f"The winner is {name_of_winner} with a bid of ${bid_of_winner}")
