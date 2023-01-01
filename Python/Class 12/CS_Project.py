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
# no_of_day = int(input('What is the number of the weekday(Valid Values= 1 to 7)?: '))

# if no_of_day==1:
#     print('The day is Monday')
# elif no_of_day==2:
#     print('The day is Tuesday')
# elif no_of_day==3:
#     print('The day is Wednesday')
# elif no_of_day==4:
#     print('The day is Thursday')
# elif no_of_day==5:
#     print('The day is Friday')
# elif no_of_day==6:
#     print('The day is Saturday')
# elif no_of_day==7:
#     print('The day is Sunday')
# else:
#     print('Please put in a valid value form 1 to 7')

'''
Output:
What is the number of the weekday(Valid Values= 1 to 7)?: 3
The day is Wednesday
'''

'''
6: Write a menu driven program to calculate the
total surface area and volume of a cube,cuboid
or cylinder depending upon user's choice.
'''

'''
Output:
'''

'''
7: Write a program to read a string and print out the
following:
1)No. of capital alphabets.
2)No. of small alphabets.
'''

# def alphabet_count(x):
#     capicount=0
#     smallcount=0
#     for i in x:
#         if i.isupper():
#             capicount+=1
#         elif i.islower():
#             smallcount+=1
#     print('The number of Capital Letters in the string is',capicount)
#     print('The number of Small Letters in the string is',smallcount)
# string = input("Put in the string: ")
# alphabet_count(string)


'''
Output:
Put in the string: Happy New Year
The number of Capital Letters in the string is 3
The number of Small Letters in the string is 9
'''

'''
8: Write a program to read a string and print it after replacing
each of it's capital alphabets by the corresponding small
alphabets and each small alphabet by it's corresponding capital
alphabet.
'''

# def change_case(string):
#     print(string.swapcase())
# string = 'Happy New Year'
# change_case(string)

'''
Output:
hAPPY nEW yEAR
'''


'''
9: Write a python program to read a file named"
article.txt",the following from the file ?
(i) length of the file (total characters in the file)
(ii) total alphabets
(iii) total digits
(iv)total spaces
(v)total special characters
'''
# file_obj = open(r'F:\Computer Science\Project\sample3.txt','r+')
# text = file_obj.read()
# length=len(text)
# alpha=0
# digits=0
# space=0
# special=0
# for i in text:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digits+=1
#     elif i.isspace():
#         space+=1
#     else:
#         special+=1
# file_obj.close()
# print('Length of the file is', length)
# print('Number of alphabets in the file',alpha)
# print('Number of Digits in the file',digits)
# print('Number of spaces in the file',space)
# print('Number of Special Characters in the file',special)


'''
Output:
Length of the file is 3541
Number of alphabets in the file 2857
Number of Digits in the file 0
Number of spaces in the file 550
Number of Special Characters in the file 134
'''

'''
10: Write a python program to read a file named "sample1.txt",
count and print the total words starting with "a" or "A".
'''

# def count_words_withaorA():
#     w=0
#     fobj = open(r'F:\Computer Science\Project\sample1.txt','r+')
#     for line in fobj:
#         for word in line.split():
#             if (word[0]=='a' or word[0]=='A'):
#                 print(word)
#                 w=w+1
#     print('Total words starting with "a" or "A" are',w)

# count_words_withaorA()

'''
Output:
amicitia
amet,
adipiscing
An
a
At
absurdum,
Total words starting with "a" or "A" are 7
'''

'''
11: Write a python program to read a file named "story.txt",
count and print the total lines starting with vowels in the file.
'''

# vowels ='AEIOUaeiou'
# with open(r'F:\Computer Science\Project\story.txt') as f:
#     line = f.readline()#break lines and readlines does it in lists
#     count=0
#     while line:
#         if (line[0] in vowels):
#             print(line)
#             count+=1
#         line=f.readline()
#     print("\nThe total number of lines starting with vowels are : ",count)


'''
Output:
A short story is a piece of prose fiction that can typically be read 
in
a
The total number of lines starting with vowels are :  3
'''


'''
12: Write a program to enter a string and to check if it is in
palindrome or not using loop.
'''


'''
Output:

'''



'''
13: Write a python program to read a file named "sample.txt",
count and print the following from the file.
a) The number of lines present in the file.
b) The number of words present in the file
'''


'''
Output:

'''



'''
14: Create a binary file with name and roll no. Search for a
given roll no and display the name ,if not found display the
appropriate error message.
'''




'''
Output:

'''


'''
15 :Write a random number generator that generates random
numbers between 1 and 100.
'''

'''
Output:

'''

'''
16:Write a python program to increase the salary by Rs.2000/of
the employee having empno is 2521 in a binary file emp.dat.
'''

'''
Output:

'''



'''
17:Write a program in python to read a text file and remove
all the lines that contain character 'a' in a file and write it to
another file.
'''

'''
Output:

'''


'''
18: Write a program in python that swipe the first half of
sorted list with second half of list.
'''

'''
Output:

'''

'''
19: Write a program in python to get item details (icode,
description and price) for multiple items from the user and
create a csv file by writing all items in one go .
'''

'''
Output:

'''


'''
20:Write a program in python to find out the largest number
and sum of all numbers without using built in methods like
max() & sum().
'''

'''
Output:

'''
