import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lcomb = "" # init empty string
for i in range(nr_letters):
  l_int = random.randint(1, len(letters))
  lcomb = lcomb + letters[l_int-1] 
#print("lcomb: ") 
#print(lcomb)

scomb = "" # init empty string
for i in range(nr_symbols):
  s_int = random.randint(1, len(symbols))
  scomb = scomb + symbols[s_int-1] 
#print("scomb: ") 
#print(scomb)

ncomb = "" # init empty string
for i in range(nr_numbers):
  n_int = random.randint(1, len(numbers))
  ncomb = ncomb + numbers[n_int-1] 
#print("ncomb: ") 
#print(ncomb)
#print("\n")
comb = lcomb + scomb + ncomb
#print(f"comb: {comb}")

# convert to list of strings
comb = list(comb)
random.shuffle(comb)
#print(f"shuffled comb list before joined: {comb}")

# Shuffle
shuffled_comb = "".join(comb)
#print(f"shuffled_comb: {shuffled_comb}")

print(shuffled_comb)
