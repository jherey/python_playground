temperature = 35

if temperature > 30:
  print("It's a hot day")
else:
  print("It's not a hot day")

# >=
# <=
# ==
# !=

# Exercise 1

# name = 'Jerry'
# length_of_name = len(name)

# if length_of_name < 3:
#   print('name must be at least 3 characters long')
# elif length_of_name > 50:
#   print('name can be a maximum of 50 characters')
# else:
#   print('name looks good')

# Exercise 2

weight = input('Weight: ')
kg_or_lb = input("(L)bs or (K)g: ")

# if kg_or_lb == 'K' or kg_or_lb == 'k':
if kg_or_lb.upper() == 'K':
  weight_in_lb = int(weight) * 2.20462
  print(f'You are {weight_in_lb} pounds')
elif kg_or_lb.upper() == 'L':
  weight_in_kg = int(weight) / 2.20462
  print(f'You are {weight_in_kg} kilos')
