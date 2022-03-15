#07072021: HW: WAP to print the sum of first 10 prime numbers using for loop

num = int(input("What number?"))
sum =0

for i in range(1,num+1):
    factor = 0 
    
    for j in range(1,i+1):
        if i%j==0:
            factor +=1
    if factor==2:
        print(i, end=", ")
        sum = sum +i

print("Sum:",sum)


