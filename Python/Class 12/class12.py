'''
Functions
1. Built in Functions
2. Modules
3. User Defined


Built in Functions:- Already defied in Python that we can use without importing, eg. int function, Float
Modules:- Packages
User Defined Functions :- User Defined




'''

# print(int("123"))

# print(float(27))

# print(str(272))


'''
input:
by default we get str value


'''
#eval

# always takes str as the argument

# a= eval(10)
# print(a) # error (only str)




# x= [1,234,234,5,25,31,453,45,3,5]
# print(type(x))
# t= len(x)
# print(type(t))

# round(10.2)
# round(10.4,0)# 0 means 1 decimal point and the would always be 0

#round(10.45,)





# file_object = open("Test.txt","r")

# value = file_object.read(3)
# # parameter of of read represents number of bytes to be read like if it is 15 bytes it means
# # 15 Characters are to be read.
# print(value)
# value1=file_object.read(5)
# print(value1)
# value2=file_object.read(5)
# print(value2)


# fobj = open("Test.txt","r")

# print_value= fobj.readline()

# print(print_value)

# print_value= fobj.readline()

# print(print_value)

# f = open("Test.txt","r")
# value = f.readlines()
# print(value)
# '''Read Line by line'''
# f = open("Test.txt","r")

# str = " "

# while str:
#     str = f.readline()
#     print(str)
# f.close

# '''Displaying size of File with and without EOL'''


# f = open('Test.txt','r')

# size_EOL = 0
# size_NoEOL = 0
# str = ' '


# while str:
#     str = f.readline()
#     size_EOL = size_EOL + len(str)
#     size_NoEOL = size_NoEOL + len(str.strip())


# print(size_EOL)
# print(size_NoEOL)


# '''Read Complete file in a list'''

# f = open(r"Test.txt",'r')

# complete_file_list = f.readlines() ## .readlines gives us whole thing in a list form along with \n

# print(complete_file_list)




# f = open('new_file.txt','a+')  ## here a+,a,w,w+ can be used but we have to be careful with w because it can erase everything too

# for i in range(5):
#     input1 = input("Enter the Value to be added:  ")
#     f.write(input1)
#     f.write("\n")  ## here \n is for next line because other wise all will stick to each other here space can also be used

# f.close()



