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
pi=3.14159
def area_cube():
    a= float(input('what is the side of the cube?: '))
    area = 6*a*a
    print("The area of cube is",area)

def area_cylinder():
    r= float(input('what is the radius of the cylinder?: '))
    l= float(input('what is the length of the cylinder?: '))
    
    area = 2*pi*r*r + 2*pi*r*l
    print("The area of cube is",area)

def area_cuboid():
    l= float(input('what is the length of the cuboid?: '))
    b= float(input('what is the breadth of the cuboid?: '))
    h= float(input('what is the height of the cuboid?: '))
    area = 2*(l*b + b*h + l*h)
    print("The area of cuboid is",area)

def vol_cube():
    a= float(input('what is the side of the cube?: '))
    vol = a*a*a
    print("The area of cube is",vol)

def vol_cylinder():
    r= float(input('what is the radius of the cylinder?: '))
    l= float(input('what is the length of the cylinder?: '))
    
    vol = pi*r*r*l
    print("The area of cube is",vol)

def vol_cuboid():
    l= float(input('what is the length of the cuboid?: '))
    b= float(input('what is the breadth of the cuboid?: '))
    h= float(input('what is the height of the cuboid?: '))
    vol = l*b*h
    print("The area of cuboid is",vol)


while True:
    print("Welcome to the Program \n")
    print("What would you like to calculate\n"
    "1. Total Surface Area\n"
    "2. Volume\n"
    "3. Exit"
    )
    
    ch= int(input())
    if ch==1:
        print("Whose Total Surface Area would you like to calculate?\n"
"1. Cube\n"
"2. Cuboid\n"
"3. Cylinder\n"
"4. Exit")        
        i=int(input())
        if i==1:
            area_cube()
        elif i==2:
            area_cuboid()
        elif i==3:
            area_cylinder()
        elif i==4:
            break
        else:
            print("Please enter a number between 1 and 4")
    elif ch==2:
        print("Whose Volume would you like to calculate?\n"
"1. Cube\n"
"2. Cuboid\n"
"3. Cylinder\n"
"4. Exit")        
        i=int(input())
        if i==1:
            vol_cube()
        elif i==2:
            vol_cuboid()
        elif i==3:
            vol_cylinder()
        elif i==4:
            break
        else:
            print("Please enter a number between 1 and 4")
    elif ch==3:
        break
    else:
        print("Please enter a number between 1 and 4")

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
# def isPalindrome(s):
#     return s == s[::-1]
 
 
# # Driver code
# s = input('Enter the string to be checked: ')
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes, it is a Palindrome")
# else:
#     print("No, it is not a Palindrome")

'''
Output:
Enter the string to be checked: AvA
Yes, it is a Palindrome
'''



'''
13: Write a python program to read a file named "sample.txt",
count and print the following from the file.
a) The number of lines present in the file.
b) The number of words present in the file
'''
# f = open(r'F:\Computer Science\Project\sample3.txt','r+')
# count=0
# wcount=0
# for line in f:
#     if line!='\n':
#         count+=1
#         word = line.split()
#         for i in word:
#             wcount+=1
# print('Total Lines', count)
# print('Total Words', wcount)



'''
Output:
Total Lines 16
Total Words 546
'''



'''
14: Create a binary file with name and roll no. Search for a
given roll no and display the name ,if not found display the
appropriate error message.
'''

# import pickle

# #creating the file and writing the data

# f=open("records.dat", "wb")

# pickle.dump(["Wakil", 1], f)

# pickle.dump(["Tanish", 2], f)

# pickle.dump(["Priyashi", 3], f)

# pickle.dump(["Kanupriya", 4], f)

# pickle.dump(["Aaheli", 5], f)

# f.close()

# #opeining the file to read contents

# f=open("records.dat", "rb")

# n=int(input("Enter the Roll Number: "))

# flag = False

# while True:

#    try:

#        x=pickle.load(f)

#        if x[1]==n:

#            print("Name: ", x[0])

#            flag = True

#    except EOFError:

#        break

# if flag==False:

#    print("This Roll Number does not exist")




'''
Output:
Enter the Roll Number: 3
Name:  Priyashi
'''


'''
15 :Write a random number generator that generates random
numbers between 1 and 100.
'''
# import random
# print("The Random number between 1 and 100 is", random.randint(1,100))

'''
Output:
The Random number between 1 and 100 is 67
'''

'''
16:Write a python program to increase the salary by Rs.2000/of
the employee having empno is 2521 in a binary file emp.dat.
'''

# import pickle
# emp ={}
# found = False
# fin = open('emp.dat','rb+')
# try:
#     while True:
#         rpos=fin.tell()
#         emp=pickle.load(fin)
#         if emp['emp_no']==2521:
#             fin.seek(rpos)
#             pickle.dump(emp,fin)
#             found = True
# except EOFError:
#     if found==False:
#         print('Sorry, no matching record found')
#     else:
#         print('Record(s) successfully updated')

#     fin.close()


'''
Output:
Sorry, no matching record found
'''



'''
17:Write a program in python to read a text file and remove
all the lines that contain character 'a' in a file and write it to
another file.
'''

# fo= open(r'F:\Computer Science\Project\story.txt','r')
# fi = open('writehp.txt','w')
# l=fo.readlines()
# for i in l:
#     if 'a' in i:
#         i=i.replace('a','')
#         fi.write(i)
# fo.close()
# fi.close()



'''
Output:
Before Program:
A short story is a piece of prose fiction that can typically be read 
in 
a
 single sitting and focuses on a self-contained incident or series of linked incidents, with 
 the intent of evoking a single effect or mood. The 
short story is one of the oldest types of literature and has existed in 

the form of legends, mythic tales, folk tales, fairy tales, t
all tales, fables, and anecdotes in various ancient communities around the world. The mod
ern short story developed in the early 19th century



After Program:
A short story is  piece of prose fiction tht cn typiclly be red 

 single sitting nd focuses on  self-contined incident or s
 eries of linked incidents, with the intent of evoking  single effect or mood. The 
short story is one of the oldest types of literture nd hs existed in 
the form of legends, mythic tles, folk tles, firy tles, tll 
tles, fbles, nd necdotes in vrious ncient communities round the world. The modern short st
ory developed in the erly 19th century

'''


'''
18: Write a program in python that swipe the first half of
sorted list with second half of list.
'''
# def swap(list):
#     l=len(list)
#     for i in range(l//2):
#         list[i],list[l//2+i]=list[l//2+i],list[i]
#     print(list)

# list = eval(input("Enter the list: "))
# swap(list)


'''
Output:
Enter the list: [1,3,6,7,34,7]
[7, 34, 7, 1, 3, 6]
'''

'''
19: Write a program in python to get item details (icode,
description and price) for multiple items from the user and
create a csv file by writing all items in one go.
'''
# import csv
# fh = open("Items.csv", "w")
# iwriter = csv.writer (fh)
# ans = 'y'
# itemrec = [['Item_Name', 'Description"', 'Price']]
# print("Enter item details ")
# while ans == 'y' :
#     iname = input("Enter Item code : ")
#     desc = input("Enter description : ")
#     price = float(input("Enter price: "))
#     itemrec.append([iname, desc, price])
#     ans = input ("Want to enter more items? (y/n)... ")
# else:
#     iwriter.writerows(itemrec)
#     print("Records written successfully.")
# fh.close()

'''
Output:
Enter item details 
Enter Item code : 1
Enter description : A headphone
Enter price: 5000 
Want to enter more items? (y/n)... n
Records written successfully.
'''


'''
20:Write a program in python to find out the largest number
and sum of all numbers without using built in methods like
max() & sum().
'''
# def myMax(list1):
#     max=list1[0]
#     for x in list1:
#         if x>max:
#             max=x
#     return max
# def listsum(list1):
#     total =0
#     for ele in range(0, len(list1)):
#         total =total + list1[ele]
#     print(total)   
# lst=eval(input("Enter the List: "))
# print("Sum of all elements in given list: ")
# listsum(lst)
# print("Largest element is: ", myMax(lst))

'''
Output:
Enter the List: [1,2]
Sum of all elements in given list: 
3
Largest element is:  2
'''
