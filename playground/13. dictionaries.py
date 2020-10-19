# customer = {
#   "name": "Jerry Olufayo",
#   "age": 27,
#   "is_verified": True
# }
# customer["name"] = "Jay Olufayo"
# customer["birthdate"] = "Jun 12 1990"
# print(customer["name"])
# print(customer.get("age"))
# print(customer.get("birthdate", "Jun 10 1990"))


# numbers = {
#   '0': 'Zero',
#   '1': 'One',
#   '2': 'Two',
#   '3': 'Three',
#   '4': 'Four',
#   '5': 'Five',
#   '6': 'Six',
#   '7': 'Seven',
#   '8': 'Eight',
#   '9': 'Nine'
# }
# # phone = int(input('Phone: '))
# phone = input('Phone: ')
# output = ''
# for digit in phone:
#   if digit == phone[0]:
#     output += numbers[digit]
#   else:
#     output += f' {numbers[digit]}'
# print(output)

message = input(">")
words = message.split(' ')
emojis = {
  ":)": "😁",
  ":(": "😞"
}
output = ""
for word in words:
  output += emojis.get(word, word) + " "
print(output)
