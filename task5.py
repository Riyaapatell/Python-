#1 check if a person is eligiblt to vote
a = int(input("Enter your age: "))
if a >= 18:
    print("You are eligible to vote")
else:
    print("you are not eligible to vote")

#2 calculate grade 90+= A, 80+= B else C
a = int(input("Enter your marks: "))
if a >= 90:
    print("Your Grade is A")
elif a>=80:
    print("Your Grade is B")
else:
    print("Your Grade is C")

#3 traffic light 
a = input("Enter a sign: ")
b=a.lower()
if b == "red":
    print("Stop")
elif b == "yellow":
    print("wait")
elif b == "green":
    print("go")
else:
    print("error!")

#4 ATM withdrawal, sufficient balance or not
balance = 50000
a = int(input("Enter the amount: "))
if a > balance:
    print("Insufficient")
else:
    avl = balance - a
    print(avl)

#5 check if the no. is +,- or 0
a = int(input("Enter a number: "))

if a > 0:
    print("Number is positive")
elif a < 0:
    print("Number is negative")
else:
    print("Number is zero")

#6 check if a number lies within a given range
a = int(input("Enter a number: "))
in_range = range(19,27)
if a in in_range:
    print("Number is in range")
else:
    print("Number is not in range")

#7 username and password verification
print("Set your details")
username = input("Enter your username: ")
password = input("Enter your password: ")

print("Verifyting your username and password")
user1 = input("Enter your username: ")
pass1 = input("Enter your password: ")

if (username == user1 and password == pass1):
    print("Credentials cerified")
else:
    print("wrong username or password")

#8 electricity bill calculator based on units consumed 
a =  int(input("Enter the amount of units consumed: "))
bill = a * 80
if a > 90 and a < 100:
    print("bill:",bill)
elif a > 80 and a < 89:
    print("bill: ",bill)
else:
    print("invalid units!")

#9 simple calculator 
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = input("Enter which operator to do(+,-,*,/): ")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("Error!")

#10 check type of triangle (equiletral, isoscales, scalene)
a = int(input("Enter 1st side of triangle(cm/m): "))
b = int(input("Enter 2nd side of triangle(cm/m): "))
c = int(input("Enter 3rd side of triangle(cm/m): "))

if (a == b == c):
    print("Triangle is equilateral")
elif (a == b or b == c or c == a):
    print("Triangle is isoscales")
elif (a != b != c ):
    print("Triangle is scalene")
else:
    ("Error!")