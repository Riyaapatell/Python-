#1 create a custom math module and import it in another file
import mathmod
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number "))
print("Addition of both numbers:",mathmod.add(a,b))
print("Subtraction of both numbers:",mathmod.sub(a,b))
print("Multiplication of both numbers:",mathmod.mul(a,b))
print("Division of both numbers:",mathmod.div(a,b))

#2 create a module to perform string operation
import stringmod
text = input("Enter a string: ")
print("String in upper case:",stringmod.upper(text))
print("String in lower case:",stringmod.lower(text))
print("String in center:",stringmod.center(text))
print("String in encode:",stringmod.encode(text))

#3 random module to generate 5 random integer
import random
for i in range(5):
    num = random.randint(1,199)
    print(num)

# 4 datetime module to display current date and time
from datetime import datetime
current  = datetime.now()
print(current)

#5 use math module to find factorial of a number
import math1 

number = int(input("Enter a number for factorial: "))
print(math1.func(number))

#6 create a package shape and with module for circle and rectangle

from shape import circle
from shape import rectangle

print("Area of circle:", circle.area(3))
print("Area of rectangle:",rectangle.area(3,6))

#7 import multiple functions from one module and use them

from student import name,age,marks

print("Name:",name())
print("Age:",age())
print("Marks:",marks())

#8 write a program to shuffle a list using random module
import random

numbers = [3,45,5,32,4]
random.shuffle(numbers)
print(numbers)

#9 a program to calculates the diff between two dates
from datetime import datetime
date1 = datetime(2026,3,31)
date2 = datetime(2026,7,1)

difference = date2 - date1
print("Differnece:",difference.days, "days") 

#10 use os module to list files in a dictionary   

import os 
file = os.listdir(r"C:\Users\riya\Pictures\Screenshots")
print(file)