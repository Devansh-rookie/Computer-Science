# list1 = list(input("put"))

# list2=list1[0:4]

# print(list2)


# list1 = [90,20,69,50,79]
# s=0
# for i in list1:
#     s+=i
#     print(i)

# print(s)

# list1 = [1,2,3,4,5]
# a = len(list1)
# j=0
# for i in range(a):
    # j+=i
    # print(list1[i])
# print(j)
#

# '''Aliasing'''

# list1 = [1,2,3,4,5]

# list2 = list1

# list2[0]=10
# list2[0]=10
# print(list1)
# print(list2)

# '''
# Out put
# [10, 2, 3, 4, 5]
# [10, 2, 3, 4, 5]

# '''
# list1 = [1,2]
# list2 =[3,4]

# print(list1>list2)


# list1 = [1,2]
# list2 =[1,4]

# print(list1>list2)


# list1 = [10.4,2]
# list2 =[10.3,2]

# print(list1>list2)

"""True"""

# list1 = [1,2]
# list2 =[3,4,2]

# print(list1>list2)


# list1 = [10,20,30]
# list2 = [40,50,60]

# # list3 = list1+ [100]

# list3 = list1+ 100

# print(list3)

# list3 = list1+list2
# print(list3)



# list1 = [10,20,30]
# list2 = [40,50,60]
# list3 = list1*list2
# print(list3)




# list1 = [1,2,3,4,65,5,67,7]
#
# print(3 in list1)
#

# print(3 not in list1)



# list1 = [1,2,3,4,5]

# print(list1[3])

# list1 = [1,2,3,4,5]

# print(list1[:])

# print(list1[0:2])

'''Add an Element at the end of the list with append method'''
# list1 = ['a','b','c','d','e']

# list1.append('f')

# print(list1)


'''Add an element to the list only if the element is an odd number'''
# a = []
# number_of_numbers = int(input("How many numbers do you want to add"))


# for i in range(0,number_of_numbers):
#     element1 = int(input("What do you want to add?"))
#     if element1%2!=0:
#         a.append(element1)
# print(a)
'''OR'''

# a=[]
# i=0
# numberofnumbers = int(input("How many numbers to add?  "))

# while i<numberofnumbers:
#     add = int(input("What do you want to add?"))
#     if add%2!=0:
#         a.append(add)
#     i+=1
# print(a)


# list1 = [1,2,3,4,5]
# list2 = [12,344,54,3452]

# for i in list2:
#     list1.insert(0,i)
# print(list1)

#
# list1=['k','r','o','f']
#
# list1.reverse()
# print(list1)

# list1 = [1,2,3,4,5,6]
# print(list1.index(7))




# list1 = [1,2,3,4,5,6,5,5,5,5,5,5,5,5,5,5,5,5]
# flag=0

# for i in list1:
#     if i==5:
#         flag+=1

# print(flag)

# print(list1.count(5))



# list1=[1,1,1234,3,254,34,5312,456,32456,2346,2354,6,23]
# flag=0
# for i in list1:
#     flag+=1

# print(flag)

# print(len(list1))

# list1 = [1,4,3,5,2,65,6,2345,67893450]
# list1.sort()
# print(list1)


'''Error in bottom code Strings not allowed'''

# list1 = [1,4,3,5,2,65,6,2345,67893450,"7"]
# list1.sort()
# print(list1)


'''Sort and Sorted are 2 Different functions'''


# list1=[1,4,2,5,7,9,5]

# list1.sort(reverse=True)
# print(list1)


# list2=[1,4,2,5,7,9,5]


# print(sorted(list2))

# list3=[1,4,2,56,6,7,5] +1)):
#     print(list1.pop(i))

# list1= [1,2,3,4,5,6]
# print(list1.pop(2))
# print(list1)

# list1= [1,2,3,4,5,6]

# a=list1.pop()

# list1= [1,2,3,4,5,6]

# a=list1.pop() +1)):
#     print(list1.pop(i))

# list1= [1,2,3,4,5,6] +1)):
#     print(list1.pop(i))

# list1= [1,2,3,4,5,6]
# print(list1.pop(2))
# print(list1)

# list1= [1,2,3,4,5,6]

# a=list1.pop()


# list1= [1,2,3,4,5,6]


# del list1[3]

# print(list1)

# a=list1.remove(5)
# '''<list>.remove(element)'''
# print(a,list1)


# list1= [1,2,3,4,5,6]

# list1.remove(3450978)


# list1= [1,2,3,4,5,6]

# print(list1.index(5))


# list1= [1.435,412345.5413,1]

# list2 = ["sadfg",1234,65,236,546,4,6724,7,426,7,462,'23456shfg']

# a=max(list1)

# # b=max(list2)

# print(a)


# list1 = [100,-100,101,-101,102,-102,103,-103]
#
# length = len(list1)
# i=0
# while i<length:
#     if list1[i]>0:
#         del list1[i]
#         length-=1
#         i-=1
#     elif list1[i]%2==0:
#         del list1[i]
#         length-=1
#         i-=1
#     i+=1
#
# print(list1)# values = [[5,1,6],[9,1,4]]
# for row in values:
#     row.sort()
#     for element in row:
#         print(element,end=" ")
#     print()


# list1 = eval(input('Enter a list of NUMBERS'))
# num = int(input("Enter number for finding index"))
# length = len(list1)
#
# for i in range(0,length):
#     if num == list1[i]:
#         print(i)
#         break
# else:
#     print("Value not found")
#
#
# list_str = "[1,3,5,6,7,8,9,9,456,43,54,57,5]"
#
# list1 = eval(list_str)
# print(list1[2])
# print(list_str[2])
#
# print(type(list1), type(list_str))

# x= [1,2,3,4,5]
# print(x[3:]+x[:2])
#

# values = [[5,1,6],[9,1,4]]
# for row in values:
#     row.sort()
#     for element in row:
#         print(element,end=" ")
#     print()


# l = [1,3,4,40,48,4967,66,4333,5,555335]
#
# i = l.index(5)
# l[i]=100
# print(l)

# list1 = ['abc','cdc','121','xyz']
# count = 0
#
# for i in list1:
#     a=len(i)
#     if a>1 and i[0]==i[-1]:
#         count+=1
# print(count)

# sample_list = ["Rinku", "AUSHIM", "VIJAYA", "AKHTAR", "AMAR", "LEENA",'aSHIF']
#
# for i in sample_list:
#     if i[0]=='a' or i[0]=="A":
#         print(i)
#
# t = (1,2,)
# print(t,type(t))
#
#

# t = tuple()
# value = eval(input('Enter your number of values:'))
#
# i=1
# while i<=value:
#     val = input("enter your value")
#     t = t +(val,)
#     i+=1
# print(t)
#
#
# t1= (1,2,3,4,5)
# t2 =(1,2,3,4,5)
# t3=t1+t2
# print(t1+t2)
#


# t1=(12,234,12)
# t2=(123,14,1,4)
# print(t1*t2)
#
#
# tup = (1,2,3,4,5)
# print(len(tup))

# t =  (1,1,2,21,423,42,41,1,1,13,4,34141,1,1,1,1,1)
# print(t.count(1))

# t=(1,2,3,4,5,6)
# print(any(t))
# t=()
# print(any(t))

# t=(1,2,3,4,5,6)
# print(max(t),min(t))

# t=(1,2,3,4,5,6.0)
# print(max(t))
# t=('f', 'a')
# print(sum(t))


# t = eval(input("Please enter a tuple you would like to find the Sum Average Maximum Value and Minimum Value"))
# sigma= sum(t)
# n_terms = len(t)
# maxi = max(t)
# mini = min(t)
# mean = sigma/n_terms
# print(sigma,n_terms,maxi,mini,mean)
'''
t = tuple()
n = int(input("Number of terms in tuple?:"))

for i in range(0,n):
    num = int(input("Enter you value:-"))
    t = t + (num,)
print(t)
'''

# t=(1,2,3,4,5,6)
# del t
# print(t)

# d1 = {'a':"Apple",'b':"Boy"}
# print(d1)
# d1["a"]="test"
# print(d1)



