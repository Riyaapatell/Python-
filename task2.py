#1 Calculate the remainder of two numbers
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

print("remainder:", a % b)


#2 Check if number is even or odd
num = int(input("enter a number: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")


#3 Compare two numbers and print the larger one
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

if a > b:
    print("larger number:", a)
elif b > a:
    print("larger number:", b)
else:
    print("both numbers are equal")


#4 Calculate the square and cube of number
num = int(input("enter number: "))

print("square:", num ** 2)
print("cube:", num ** 3)


#5 Check if two entered numbers are equal
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

if a == b:
    print("both numbers are equal")
else:
    print("numbers are not equal")


#6 Print true if both numbers are positive
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

if (a > 0 and b > 0):
    print("true")
else:
    print("false")



#7 Convert float to integer
num = float(input("enter a float number: "))

print("integer:", int(num))


#8 Take a number as a string, convert to int, and multiply by 10
num = input("enter a number: ")

num = int(num)
print("result:", num * 10)


#9 Use operators to check multiple conditions
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

print("both positive:", (a > 0 and b > 0))
print("at least one positive:", (a > 0 or b > 0))


#10 Divide two numbers and print quotient and remainder separately
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

print("quotient:", a // b)
print("remainder:", a % b)