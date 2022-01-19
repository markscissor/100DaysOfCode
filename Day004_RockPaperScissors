rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

#player win conditions
p1 = (player == 0 and computer ==2)
p2 = (player == 1 and computer ==0)
p3 = (player == 2 and computer ==1)

#computer win conditions
c1 = (computer == 0 and player ==2)
c2 = (computer == 1 and player ==0)
c3 = (computer == 2 and player ==1)

hand = [rock,paper,scissors]

print(hand[player])
print("Computer choose:")
print(hand[computer])

if (p1 or p2 or p3):
  print("You win.")
elif (c1 or c2 or c3):
  print("You lose.")
else:
  print("It's a draw.")
