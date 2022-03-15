# import os

# location_of_files = "D:\\Coding\\Python"

# file_name = "hi.txt"

# with open(os.path.join(location_of_files,file_name)) as file:
#     print(file.read())

# who = "Gary"

# how_many = 12

# string = f'{who} bought {how_many} apples today!'

# print(string)

def calc(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y

operation = calc(7,3,'div')
print(operation)