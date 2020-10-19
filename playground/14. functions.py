# def greet_user(first_name, last_name):
#   print(f'Hi {first_name} {last_name}')
#   print('Welcome aboard')


# print('Start')
# greet_user('Jerry', 'Olufayo')
# greet_user(last_name='Jerry', first_name='Olufayo')
# print('Finish')


# return statement
# def square(number):
#   return number * number

# print(square(5))

message = input(">")

def emoji_converter(message):
  words = message.split(' ')
  emojis = {
    ":)": "😁",
    ":(": "😞"
  }
  output = ""
  for word in words:
    output += emojis.get(word, word) + " "
  return output


print(emoji_converter(message))
