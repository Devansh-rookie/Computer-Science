# import random

# i = 0
# k=0

# while (i<10):
#     i=i+1
#     a=random.randrange(1000,9999,137)
#     print(a)

# while (k<10):
#     k=k+1
#     b=random.randrange(1000,1000000,3)
#     print(b)
# ab = [1,35,24,234,2345]

# print(ab[-3])
# print(len(ab))

# i = 0

# while (i<100):
#     i = i + 1
#     print(i)

# mark = int(input("Tell Your Marks?:"))


# if mark>0:
#     if mark>33:
#         if mark>41:
#             if mark>51:
#                 if mark>61:
#                     if mark>71:
#                         if mark>81:
#                             if mark>91:
#                                 if mark>101:
#                                     print("Marks Not Valid")
#                                 else:
#                                     print("Congrats You Got 'A1' Grade")
#                             else:
#                                 print("Congrats You Got 'A2' Grade")
#                         else:
#                             print("Congrats You Got 'B1' Grade")
#                     else:
#                         print("Congrats You Got 'B2' Grade")
#                 else:
#                     print("Congrats You Got 'C1' Grade")
#             else:
#                 print("Congrats You Got 'C2' Grade")
#         else:
#             print("Congrats, You Got 'D' Grade")
#     else:
#         print("Sorry you Got 'E' and Failed")
# else:
#     print("Marks not Valid")

# import math

# a = math.sqrt(3)
# print(a)

# import math

# a = int(input("Tell the number to square root:"))

# sq = math.sqrt(a)

# print(sq)

'''
Iteration and Looping

Entry Controlled Loops == for loop

'''
'''
sum = 0

for i in range(1,11):
    sum = sum + i
    print("Inner Workings", i , sum)
print(sum)
'''
# To find factorial

# num = int(input("What factorial do you want?"))
# fact = 1
# for i in range(num ,0 ,-1):
#     fact = fact*i
# print(fact)

#To find if the number is prime or not
'''
flag =0
a = 0
num = int(input("What is your number?"))

for i in range(2,num//2):#num//2 gives only the integer part of the Expression
    if num%i==0:
        a+=1#a= a+1
        flag = 1    # flag can be any variable it will tell us if any variable has passed through the if statement or loop
        print("Divisor",a,":",i)     # because the variable is divided by i then and only then it would be printed
                            # here we can add a break if we only want the first divisor and make our code more Efficient
if flag==0:    #if flag 0 it means that the number didn't pass through any loop and wasn't divided
    print(num, "is a prime number.")
else:
    print("The number is not prime.")
'''
'''
## Only check for the first factor
flag =0
a = 0
num = int(input("What is your number?"))

for i in range(2,num//2):#num//2 gives only the integer part of the Expression
    if num%i==0:
        a+=1#a= a+1
        flag = 1    # flag can be any variable it will tell us if any variable has passed through the if statement or loop
        print("Divisor",a,":",i)     # because the variable is divided by i then and only then it would be printed
        break                    # here we can add a break if we only want the first divisor and make our code more Efficient because it will break the loop as soon as it enters and reaches it
if flag==0:    #if flag 0 it means that the number didn't pass through any loop and wasn't divided
    print(num, "is a prime number.")
else:
    print("The number is not prime.")


'''
## How to only check for prime factors.
## How to add decimal point and scientific notation
'''
#07072021: HW: WAP to print the sum of first 10 prime numbers using for loop

num = int(input("What number?"))
sum =0

for i in range(1,num+1):
    factor = 0 #why this works only inside not outside
    
    for j in range(1,i+1):
        if i%j==0:
            factor +=1
    if factor==2:
        print(i)
        sum = sum +i

print(sum)


'''

