#1 create a car class with attributes like brand, model, speed and  methods to accelerate/brake
class Car():
    def __init__(self,brand,model,speed):
        self.brand =brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("after acceleration:",self.speed)
    def brake(self):
        self.speed -= 20
        print("after brake:",self.speed)

    def show(self):
        print(self.brand,self.model,self.speed)

car1 = Car("toyota","kia",40)
car2 = Car("swift","baleno",80)
car3 = Car("kia","carens",10)

cars = [car1,car2,car3]

for car in cars:
    car.show()
    car.accelerate()
    car.brake()
    
#2 BankAccount class with deposit and withdraw methods
class BankAccount():
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,depo):
        self.balance += depo
        print("After deposit",depo,":",self.balance)
    def withdraw(self,withd):
        if withd <= self.balance:
            self.balance -= withd
            print("After withdraw",withd,":",self.balance)

        else:
            print("Insufficient balance")
    def show(self):
        print("Current Balance:",self.balance)
acc1 = BankAccount(500)
acc1.show()
acc1.deposit(10)
acc1.withdraw(50)

#3 Student class with a method to calculate avg marks
class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        average = sum(self.marks)/len(self.marks)
        print("Your avg:",average)
    def show(self):
        print("Name",self.name)
        print("marks:",self.marks)

student1 = Student("Riya",[1,3,4])
student2 = Student("Jenu",[0,11,20])
student3 = Student("Jazzy",[13,15,17])

stu = [student1,student2,student3]
for stud in stu:
    stud.show()
    stud.avg()

#4 Rectangle class with with methods to find area and perimeter
class Rectangle():
    def __init__(self,length,witdh):
        self.length = length
        self.witdh = witdh
    def area(self):
        ar = self.length*self.witdh 
        print("Area of rectangle:",ar)
    def perimeter(self):
        peri = 2* (self.length+self.witdh )
        print("Perimeter of rectangle:",peri)
rect = Rectangle(1,4)
rect.area()
rect.perimeter()

#5 Employee class that display salary details
class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

emp1 = Employee("Riya",1000000)
emp2 = Employee("Jenu",9999)
emp3 = Employee("Jazzy",1)
names =[emp1,emp2,emp3]

for employ in names:
    employ.show()

#6 Book class to store title,author,price and display details
class Book():
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price 

    def show(self):
        print("Book title:",self.title)
        print("author name:",self.author)
        print("price:",self.price)
books = []
for i in range(2):
    title = input("Enter the title of book: ")
    author= input("Enter name of author: ")
    price = float(input("Enter price of book: "))
    book = Book(title,author,price)
    books.append(book)

print("--Book details--")
for book in books:
    book.show()

#7 Circle class to find area and circumference 
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area1 = 3.14 * (self.radius ** 2)
        print("Area of circle:",area1)
    def circumference(self):
        circum = 2 * 3.14 * self.radius
        print("Circumference of circle",circum)

value = float(input("Enter the value of radius: "))

circle1 = Circle(value)
circle1.area()
circle1.circumference()

#8 Laptop class with method to apply discount on price
class Laptop():
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def discount(self,dis_to_apply):
        dis = self.price * dis_to_apply / 100
        self.price = self.price - dis
        print("After discount price:",self.price)
    def show(self):
        print("Brand:",self.brand)
        print("Price before discount:",self.price)
laptop1 = Laptop("HP",6000)
laptop1.show()
value = int(input("Enter discount to apply: "))
laptop1.discount(value)

#9 Flight class with seat booking functionally
class Flight:
    def __init__(self,flight_name,destination,seat):
        self.flight_name = flight_name
        self.destination = destination
        self.seat = seat


    def book(self):
        if self.seat > 0:
            self.seat -= 1
            print("Seats booked successfully!!")
            print("Available seats:",self.seat)
        else:
            print("Seats are not available")

    def show(self):
        print("Flight name:",self.flight_name)
        print("Destination:",self.destination)
        print("seats:",self.seat)

flight1 = Flight("ABC","ACD",5)
flight1.book()
flight1.book()
flight1.show()

#10 Create a Shop class with method to add and list products
class Shop():
    def __init__(self):
        self.product = []
    def add(self,products):
        self.product.append(products)
    def list_products(self):
        for products in self.product:
            print(products)

shop = Shop()
num = int(input("Enter the numer of products you want: "))
for i in range(num):
    products = input("Enter the product: ")
    shop.add(products)
shop.list_products()
