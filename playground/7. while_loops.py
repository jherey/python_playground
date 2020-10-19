# i = 1
# while i <= 5:
#   # print(i)
#   print('*' * i)
#   i += 1
# print("Done")


# guess = int(input('Guess: '))
# secret_number = 9

# num_of_tries = 1
# while num_of_tries < 3 and guess != secret_number:
#   guess = int(input('Guess: '))
#   num_of_tries += 1

# if num_of_tries < 3 and guess == 9:
#   print('You win!')
# else:
#   print('You lose!')

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
  guess = int(input('Guess: '))
  guess_count += 1

  if guess == secret_number:
    print('You won!')
    break
else:
  print('You lose!')
