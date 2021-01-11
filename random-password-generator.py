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

passwordLen = nr_symbols + nr_symbols + nr_numbers

lettersUsed = 0
symbolsUsed = 0
numbersUsed = 0
password = []


i = 0
while i < passwordLen:
  order = random.randint(0, 2)
  if order == 0 and lettersUsed < nr_letters:
    password.append(random.choice(letters))
    lettersUsed += 1
  elif order == 1 and symbolsUsed < nr_symbols:
    password.append(random.choice(symbols))
    symbolsUsed += 1
  elif order == 2 and numbersUsed < nr_numbers:
    password.append(random.choice(numbers))
    numbersUsed += 1
  else:
    passwordLen += 1
  i += 1


password = ''.join(password)
print(password)
print(len(password))
