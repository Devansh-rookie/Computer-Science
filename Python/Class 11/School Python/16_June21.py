# Program 1

age = float(input("What is Your Age?(in Years)"))

if age>=18:
    print("Congratulations!!!, you can vote legally")
else:
    print("Sorry you can not vote.")


# Program 2


interest_5yrs_less = 12
interest_5yrs_more = 18

principal = float(input("What is the principal Value?"))
time = float(input("What is the time in years?"))

if time>5:
    si = interest_5yrs_more*principal*time/100
    
else:
    si = interest_5yrs_less*time*principal/100

print(si)


# Program 3

a_number = int(input("What is the number"))

if a_number%2 == 0:
    print(a_number,"is even.")
else:
    print(a_number,"is odd.")

# Program 4

year = int(input("What is the year?"))

if year%100==0:
    if year%400==0:
        print(year, "is Leap year")
    else:
        print(year, "not Leap year")
elif year%4:
    print(year, "is a Leap year.")

else:
    print(year,"is not a Leap year.")


'''
Sir I checked the condition of leap year on wikipedia.(I didn't know all conditions for leap years.)
'''
