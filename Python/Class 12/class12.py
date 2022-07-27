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





file_object = open("Test.txt","r")

value = file_object.read(3)
# parameter of of read represents number of bytes to be read like if it is 15 bytes it means
# 15 Characters are to be read.
print(value)
value1=file_object.read(5)
print(value1)
value2=file_object.read(5)
print(value2)
