#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_nr = nr_letters + nr_numbers + nr_symbols
count_l = 0
count_s = 0
count_n = 0
pword = []

while (True):
  i = random.randint(1, 3)
  if i == 1 and count_l < nr_letters:
    pword.append(random.choice(letters))
    count_l += 1
  elif i == 2 and count_s < nr_symbols:
    pword.append(random.choice(symbols))
    count_s += 1
  elif i == 3 and count_n < nr_numbers:
    pword.append(random.choice(numbers))
    count_n += 1

  if len(pword) == total_nr:
    break

password = "".join(pword)

print(password)
