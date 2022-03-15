list1=[]
list2=[]
flag=0

for x in range(0,1000):
    for n in range(0,1000):

        a = x**n
        b = n**x
        if a==b:
            flag+=1
            list1.append(a)
            list2.append(b)
            print(a,b,end=" ")

print(flag)
print(list1,list2)
