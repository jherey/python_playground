# STRINGS

course = 'Python for Beginners'
print(course[1:-1])

first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a coder'
print(message)

course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course) # it doesn't change the original string
print(course.find('P'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
