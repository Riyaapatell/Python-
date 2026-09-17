#1 print number from 1 to 10
for i in range(1,11):
    print(i)

# 2 display multiplication table for given number
num = int(input("Enter a number for multiplication: "))
for i in range(1,11):
    print(num , "*", i , "=" , num * i )

#3 factorial of number
num = int(input("Enter a number for factorial: "))
count = 1
if num>0:
    for i in range(1,num+1):
        count = count * i

    print("factorial:",count)
elif num == 0:
    print("factorial: 1")
else:
    print("enter valid number")

#4 generate the first N fibonacci numbers
n = int(input("Enter how many Fibonacci numbers: "))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b

#5 check if the number is prime
num = int(input("Enter a number to check if it is prime or not: "))

if num <= 1:
    print("Number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")

#6 reverse a number
num  = (input("Enter 3-4 digits to reverse a number: "))
reverse = ""
for i in num:
    reverse = i + reverse
print(reverse)

#7 count digits in a number
num = int(input("Enter number to count digits: "))
digit = 0

while num > 0:
    num = num // 10
    digit = digit + 1
print("Number of digits:", digit)

#8 find sum of even number between 1 to 100
sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i

print("Sum of even numbers:", sum)

#9 print a pyramid pattern
num = int(input("Enter how many lines you want in pyramid: "))
for i in range(1,num+1):
    print(" "*(num-i) + "* "*i)

#10 find all divisor of a number
num = int(input("Enter a number: "))
for i in range(1,num):
    if num % i == 0:
        print(i)