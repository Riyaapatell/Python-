#1 program to read a file and display its content
file = open("file.txt","r")

a = file.read()# read
print(a)#display
file.close()

#2 to count the number of line in a file 
file = open("file.txt", "r")

a = file.readlines()

print("Lines:",len(a))

#3 how many time each word appears in a file
file = open("file.txt")

words = file.read().split()
lists = {}

for word in words:
    if word in lists:
        lists[word] += 1
    else:
        lists[word] = 1
print(lists)
file.close()

#4 write 5 user typed sentence in file
file = open("file.txt" , "a")

for i in range(5):
    user_input = input("Enter sentences to add: " )
    file.write(user_input + "\n")

file.close()

#5 append a list of string to a existing file 
lists= []

for i in range(5):
    strng = input("Enter sentence: ")
    lists.append(strng)

file = open("file.txt", "a")

for strng in lists:
    file.write(strng + "\n")

file.close()

#6 read a file and print only lines containing a specific word 
word = input("Enter the word you want: ")
file = open("file.txt" , "r")
for line in file:
    if word in line:
        print(line)
file.close()

#7 to replace a specific word and save changes
word = input("Enter a specific word that you want to replace: ")
to_replace = input("Enter the word you want to add: ")

file = open("file.txt")
change = file.read()
change = change.replace(word,to_replace)

file = open("file.txt","w")
file.write(change)
file.close()
print("Replaced sucessfully")

#8 merge content of 2 file into 3rd

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("file3.txt", "w")

content1 = file1.read()
content2 = file2.read()

file3.write(content1)
file3.write(content2)

file1.close()
file2.close()
file3.close()

print("merged successfully")

#9 read csv file and display its content in a formatted way

import csv
file = open("file.csv", "r")

reader = csv.reader(file)

for row in reader:
    print("  ".join(row))

file.close()

#10 to backup a file by coyping its content to another
file = open("file.txt", "r")
content = file.read()

file1 = open("file3.txt", "w")
file1.write(content)
file1.close()

print("Backup created successfully")
