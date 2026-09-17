#1 handle division by zero error
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

try:
    c = a/b 
    print(c)
except ZeroDivisionError:
    print("cannot be divided by zero")

#2 handle invalid integer input 
a = int(input("Enter a integer"))

try: 
    print("Your integer:",a)
except ValueError:
    print("Its's not a integer")

#3 open a file and handle filenotfound error
try:
    file = open("file.txt","r")
    a = file.read()
    print(a)
    file.close()
except FileNotFoundError:
    print("File dosen't exist")

#4 to demonstrate multiple exception blocks
try: 
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cannot be divisible by zero")
except ValueError:
    print("Enter valid integers")

#5 use finally for resource cleanup
try: 
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cannot be divisible by zero")
except ValueError:
    print("Enter valid integers")
finally: 
    print("Program ended")

#6 create a custom exception for invalid age(<18)
class error(Exception):
    pass
try: 
    age = int(input("Enter your age: "))
    if age<18:
        raise error("You are underage")
    else:
        print("You are eligible for voting")
except error as e:
    print(e)

#7 handle indexerror when accessing a list
limit = 5

movies = []

while len(movies)<5:
    a = input("Enter your 5 fav movies: ")
    movies.append(a)

print("Yours fav movies:", movies)

try:
    index = int(input("Enter the index you want: "))
    print(movies[index])
except IndexError:
    print("Index is out of range")
except ValueError:
    print("Enter a valid integer")

#8 takes 2 number and handles all possible error
try: 
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Number is not divisible by zero")
except ValueError:
    print("Enter valid integer")
except Exception:
    print("Something went wrong")

#9 log errors to a file instead of printing them

try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = a/b
    print(c)
except Exception as e:
    file = open("file.txt","a")
    file.write(str(e) + "\n")
    file.close()
    print("Check file.txt")

#10 validates a email format an raise an expection for invalid ones
class error(Exception):
    pass
try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email or email.startswith("@"):
        raise error("Invalid email format")
    else:
        print("Valid email")
except Exception as e:
    print(e)