'''
Python Project Class 12
'''


'''
1 :Write a python script to take input for 3 numbers,check
and print the largest number.
'''

# a= int (input ('Enter the first number: '))
# b=int (input ('Enter the second number: '))
# c=int (input ('Enter the third number: '))
# list = [a, b, c]
# print('The largest number is:', max (list))

'''
Output:
Enter the first number 10
 Enter the second number 9
 Enter the third number 13
 The largest number is  13
'''


'''
2:Write a python script to take input for name and age of a
person and check and print whether the person can vote or
not.
'''

# Name = input('What is the Name of the Person?: ')
# Age = int(input('What is the Age of the Person?: '))

# if Age>=18:
#     print(Name, 'is Eligible to vote.')
# else:
#     print(Name, 'is too young to vote.')


'''
Output:
What is the Name of the Person?: Devansh
What is the Age of the Person?: 17
Devansh is too young to vote.
'''

'''
3: Write a program to input two numbers m
and n and display first m multiples of n.
'''

# n= int(input('What is the number?: '))
# m= int(input('How many multiples are needed?: '))
# j=0
# for i in range(1, m+1):
#     j+=1
#     mul = j*n
#     print(mul, 'is a multiple of', n)

'''
Output:
What is the number?: 13
How many multiples are needed?: 5
13 is a multiple of 13
26 is a multiple of 13
39 is a multiple of 13
52 is a multiple of 13
65 is a multiple of 13
'''


'''
4: Write a program to check if the entered
number is Armstrong or not.
'''
# num = int(input('What is the number to be checked(for Armstrong No.)?: '))
# # Changed num variable to string, 
# # and calculated the length (number of digits)
# order = len(str(num))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** order
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

'''
Output:
What is the number to be checked(for Armstrong No.)?: 1634
1634 is an Armstrong number
'''

'''
5: Write a program to input day number of a
week and display the corresponding day name .
'''
no_of_day = int(input('What is the number of the weekday(Valid Values= 1 to 7)?: '))

if no_of_day==1:
    print('The day is Monday')
elif no_of_day==2:
    print('The day is Tuesday')
elif no_of_day==3:
    print('The day is Wednesday')
elif no_of_day==4:
    print('The day is Thursday')
elif no_of_day==5:
    print('The day is Friday')
elif no_of_day==6:
    print('The day is Saturday')
elif no_of_day==7:
    print('The day is Sunday')
else:
    print('Please put in a valid value form 1 to 7')

'''
Output:
What is the number of the weekday(Valid Values= 1 to 7)?: 3
The day is Wednesday
'''




