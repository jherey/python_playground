names = ['Jerry', 'Olufayo', 'Dan', 'Seyi', 'Jay']
# print(names)
# print(names[2])
# print(names[-1])
# print(names[2:])
# print(names[2:4])
# names[0] = 'Jhery'
# print(names)


# largest number in a list
# numbers = [2,4,10,1,5,6]
# largest_num = numbers[0]
# for num in numbers:
#   if num > largest_num:
#     largest_num = num
# print(f'The largest number is {largest_num}')

# 2 Dimensional List
# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# print(matrix[0][1])

# for row in matrix:
#   for item in row:
#     print(item)


# Functions on a List
# numbers = [5,2,1,5,7,4]
# numbers.append(13)
# numbers.insert(0, 9)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()
# print(numbers.index(50))
# print(50 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)

# Remove duplicates in a list
numbers = [1,3,6,5,1,4]
for num in numbers:
  if numbers.count(num) > 1:
    numbers.remove(num)
print(numbers)
# OR
numbers = [1,3,6,5,1,4]
uniques = []
for num in numbers:
  if num not in uniques:
    uniques.append(num)
print(uniques)
