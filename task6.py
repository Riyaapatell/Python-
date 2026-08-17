#1 function to check if the number is prime
def prime(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a % 2 == 0:
            return False
    return True

number = int(input("Enter a number: "))

if prime(number):
    print("prime number")
else:
    print("Not a prime number")

#2 reverse a string
def reverse(a):
    return a[::-1]
b = input("enter a string: ")
print(reverse(b))

#3 find factorial of a funcion 
def func(a):
    fact = 1
    if a < 1:
        return False
    for i in range(1,a+1):
        fact = fact * i
    return fact
number = int(input("Enter a number for factorial: "))

print(func(number))

#4 calculate simple interest
def interest(p,q,r):
    return p*q*r/100

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
r = int(input("Enter the value of r: "))
print(interest(p,q,r))

#5 check if the word is palindrome or not

def pali(a):
    return a == a[::-1]

text = input("Enter a word: ")

if pali(text):
    print("The word is palindrome")
else:
    print("The word is not palindrome")

#6 to count vowels in a string

def vowel(text):
    count = 0
    vowel = "aeiou"

    for char in text:
        if char in vowel:
            count += 1

    return count

user_input = input("Enter the string: ")
user_input = user_input.lower()
print(vowel(user_input))

#7 function to merge 2 lists
def merge(list1,list2):

    return list1 + list2
a = list(map(int, input("Enter for list1: ").split()))
b = list(map(int, input("Enter for list2: ").split()))

print("Merged list:",merge(a,b))

#8 GCD of 2 numbers 

def GCD(num1,num2):
    for i in range(1,min(num1,num2) +1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return i 
a = int(input("Enter 1st number for GCD: "))
b = int(input("Enter 2nd number for GCD: "))

print("GCD:",GCD(a,b))

#9 area of triangle 
def area(length, breath):
    return length * breath / 2

a = float(input("Enter the length of triangle: "))
b = float(input("Enter the breath of triangle: "))
print("Area:",area(a,b))

#10 check armstrong number 
def num(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    return total == original


user_input = int(input("Enter a number: "))

if num(user_input):
    print("Armstrong number")
else:
    print("Not an Armstrong number")