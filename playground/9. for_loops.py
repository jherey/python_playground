# for item in 'Python':
#   print(item)

# for item in ['Jerry', 'John', 'Sarah']:
#   print(item)

# for item in [1,2,3,4]:
#   print(item)

# for item in range(10):
#   print(item)

# prices = [10, 20, 30]
# total_price = 0
# for price in prices:
#   total_price += price
# print(f'Total: {total_price}')


# Nested Loop
# for x in range(4):
#   for y in range(3):
#     print(f'({x}, {y})')

# numbers = [5,2,5,2,2]
numbers = [2,2,2,5]
for num in numbers:
  str = ''
  for i in range(num):
    str += 'x'
  print(str)
