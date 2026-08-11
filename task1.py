name = "Riya"
age = 21
city = "Valsad"

print(name, age, city)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)


celsius = float(input("Enter temperature in(C): "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

name = input("Enter your name: ")

print(name.upper())

birth = int(input("Enter your birth year: "))

current = 2026
age = current - birth

print("Your age is:", age)

a = input("Enter value of a: ")
b = input("Enter value of b: ")

print("Before swap:")
print("a =", a)
print("b =", b)

temp=a
a=b
b=temp

print("After swap:")
print("a =", a)
print("b =", b)


length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle =", area)


number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2

print("average =", average)