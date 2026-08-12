#1 create a tuple with 5 numbers
a = (input("Enter any string or numbers")).split()
print(tuple(a))

#2 accesing 3rd element in tuple
a = input("Enter any string or numbers").split()
print(tuple(a))
print(a[2])

#3 unpacking tuple into seperate variable
limit = 5
fruits = []

while len(fruits)<limit:
    a = input("Enter any 5 string or number: ")
    fruits.append(a)
fruits = tuple(fruits) 

print("your tuple:", fruits)
print("unpacking")
a, b, c, d, e = fruits
print(a)
print(b)
print(c)
print(d)
print(e)

#4 creating a set of 5 fruits
limit = 5

fruits = set()

while len(fruits)<limit:
    a = input("Enter your 5 fruits: ")
    fruits.add(a)

print("Yours 5 fruits:", fruits)
fruits2 = input("add a fruit: ")
fruits.add(fruits2)
print(fruits)
fruits.remove("apple")
print("after removing apple: ", fruits)

#union of sets
limit = 5

fruits3 = set()

while len(fruits3)<limit:
    b = input("Enter your 5 fruits: ")
    fruits3.add(b)

print("Yours new set of fruits:", fruits3)
union_set = fruits | fruits3
print("union of 2 sets:",union_set)

intersection_set = fruits | fruits3
print("Intersection of 2 set:",intersection_set)

print(fruits.issubset(fruits3))

#5 convert a list with duplicate values into a set to remove duplicate
limit = 5
my_list = []

while len(my_list)<limit:
    a = input("Enter some values of list: ")
    my_list.append(a)

my_set = set(my_list)
print("list:",my_list)
print("set",my_set)

#6 create a dictionary storing students name and marks 

limit = 2
my_dict = {}

while len(my_dict) < limit:
    key = input("Enter keys: ")
    value = input("Enter value: ")
    my_dict[key] = value

print("Dictionary:",my_dict)

#adding a key value pair
key2 = input("Enter keys: ")
value2 = input("Enter value: ")
my_dict.update({key2 : value2})

print("Updated dictionary:",my_dict)

#deleting a key value pair
to_remove = input("Which key to remove?:")
value_removed = my_dict.pop(to_remove)

print("after deleting:",my_dict)

#merging dictionary
limit = 2
my_dict2 = {}

while len(my_dict2) < limit:
    print("Adding other dictionary")
    key = input("Enter keys: ")
    value = input("Enter value: ")
    my_dict2[key] = value

mergerd = my_dict | my_dict2
print("Mergerd Dictionary:",mergerd)

#checking if a key is exists in dictionary
to_search = input("Enter the key to search: ")

if to_search in mergerd:
    print("Exists")
else:
    print("Not exists")

#7 count word frequency in a string using a dictionary
string = input("Enter a string: ")

words = string.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] =1
print("frequency:",frequency)

print("Max value")
max_value = max(frequency, key=frequency.get)

print(max_value)


#8 reverse
limit = 2
my_dict = {}

while len(my_dict)<limit:
    keys = input("Enter keys: ")
    value = input("Enter Value: ")
    my_dict[keys] = value
print("Your dict:",my_dict)
print("after reversing")

reverse = {}

for keys, value in my_dict.items():
    reverse[value] = keys
print(reverse)

#9 update
limit = 2
my_dict = {}

while len(my_dict)<limit:
    keys = input("enter keys: ")
    value = input("enter value: ")
    my_dict[keys] = value
print(my_dict)

to_update_key = input("which key to update?:")
new_value = input("enter new value:")

my_dict[to_update_key] = new_value
print("updated dict:",my_dict)

#10 converting a list of tuples into list
limit = 2
my_tuple = []

while len(my_tuple)<limit:
    key = input("enter keys: ")
    value = input("enter value: ")
    my_tuple.append((key,value))
print("your tuple:",my_tuple)

my_dict = dict(my_tuple)
print("my_dict",my_dict)