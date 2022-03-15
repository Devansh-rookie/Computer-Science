
file1 = open("txt_random", "w+")

n=int(input("How many Lines do you want to print?"))
for i in range(1,n+1):
    print('A'*i)
    b='A'*i
    file1.write(b)

