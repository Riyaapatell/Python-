#1 take string input, print its length
a = input("Enter a name: ")
print(len(a))

#2 convert a sentence to lowercase
a = input("write something in UPPERCASE: ")
print(a.lower())

#3 replace space with underscore
a = input("write something: ")
print(a.replace(" ","_"))

#4 extract 1st and last character of string
a = input("Write something: ")
print("First:",a[0])
print("Last:",a[-1])

#5 reverse string using slicing
a = input("Type a string: ")
print(a[::-1])

#6 count how many times a letter appeares 
from collections import Counter
a = input("enter a string")
print(Counter(a))

#7 check if a word is present in sentence
a = input("Enter a sentence")
word = "riya"
present = word in a
print(present)

#8 take name & age and print in f string

a = input("enter your name: ")
b = int(input("enter your age: "))

print(f"hello {a}, thanks for confirming that you are {b} years old.")

#9 remove extra space from start and end of string
a = input("Enter a string: ")
print(a.strip())

#10 join a list of words from a string and - inbetween
a = ["hello", "good", "morning"]
print("-".join(a))

#11 create a list of your 5 movies
limit = 5

movies = []

while len(movies)<5:
    a = input("Enter your 5 fav movies: ")
    movies.append(a)

print("Yours fav movies:", movies)

#adding a movie tothe list 
b = input("add one more movie: ")
movies.append(b)
print(movies)

#removing 1st movie 
print("removing 1st movie")
movies.pop(0)
print(movies)

#12 sort a number of list in ascending order
number = (input("Enter number with space in between: "))

lists = list(map(int,number.split()))
print(lists)
print("After sorting")
lists.sort()
print(lists)

#reversing
print("reversing")
print(lists[::-1])

#finding largest number in list
print("largets number in list:", max(lists))   

#merging 2 list
number2 = (input("Enter number with space in between: "))
lists2 = list(map(int,number2.split()))
merged = lists + lists2
print("After merging both lists")
print(merged)
print("removing last element")
print(merged.pop())
print(merged)

#13 create nested list and access a inner elemet
list = [
    ["apple","mango"],
    ["banana","blueberry"]
]

print(list[0][1])

#14 count how many times a element appeares in a list
a = (input("Enter number with space in between: "))

lists = list(a.split())

print(lists)
b=lists.count("apple")
print(b)