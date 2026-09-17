#1 create a base class Animal and subclass Dog and Cat
class Animal:
      def eat(self):
            print("Ice-cream")
   
class Dog(Animal):
        def bark(self):
            print("Dog barks")
class Cat(Animal):
        def meow(self):
            print("Cat meows")
dog = Dog()
cat = Cat()
dog.eat()
dog.bark()
cat.meow()

#2 create a class heirarchy of Vehicle Car ElectricCar
class Vehicle():
    def speed(self):
        print("speed is speeding")
class Car(Vehicle):
    def caru(self):
        print("Car is also a vehicle")
class ElectricCar(Vehicle):
    def ele(self):
        print("Electric vehicle is also")

car = Car()
electric = ElectricCar()
car.speed()
car.caru()
electric.ele()

#3 Implement method overriding in a base and derived class
class Vehicle():
    def speed(self):
        print("Speed is normal")
class Car(Vehicle):
    def speed(self):
        print("Speed is fast")
car = Car()
car.speed()

#4 multiple inheritance with 2 parent class
class Father():
    def cook(self):
        print("Father cooks good")
class Mother():
    def drive(self):
        print("Mother drives crazy")
class Kid(Father,Mother):
    pass
kid1 = Kid()
kid1.cook()
kid1.drive()

#5 create a polymorphic function that works with different shapes
class Triangle():
    def shape(self):
        print("Triangle have 3 sides")
class Square():
    def shape(self):
        print("Square have 4 sides")
class Rectangle():
    def shape(self):
        print("Rectangle's opposite sides same")
def show(shapes):
    shapes.shape()
triangle = Triangle()
square = Square()
rectangle = Rectangle()
show(triangle)
show(square)
show(rectangle)

#6 bank system with SavingAccount and CurrentAccount class
class BankAccount():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def show(self):
        print("Name:",self.name)
        print("Balance",self.balance)
class SavingAccount(BankAccount):
    def save(self):
        interest = self.balance * 5 / 100
        self.balance += interest
        print("Updated balance:",self.balance)
class CurrentAccount(BankAccount):
    def current(self):
        print("Yayy")

savingaccount = SavingAccount("Riya", 100)
currentaccount = CurrentAccount("Riya1",2000)

savingaccount.show()
currentaccount.show()

#7 class with private attributes and getter/setter methods
class Age():
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get_age(self):
        print(self.__age)
    def set_age(self,age):
        if age >= 18:
            self.__age = age
            print("New age:",self.__age)
            print("Allowed to vote")
        else:
            print("Not allowed to vote")
age1 = Age("Riya",17)   
age1.get_age()
age1.set_age(21)

        

#8 create Teacher and Student class to show inheritance
class Head():
    def __init__(self,name):
        self.name = name
    def show(self):
        print("Name:",self.name)
class Teacher(Head):
    def teach(self):
        print("Teacher teaches")
class Student(Head):
    def study(self):
        print("Student studiess")
teacher = Teacher("Riya")
student = Student("Riya1")

teacher.show()
teacher.teach()
student.show()
student.study()

#9 MusicPlayer class and subclass Spotify to override play method

class MusicPlayer():
    def play(self):
        print("Play musiccccccccc")
class Spotify(MusicPlayer):
    def play(self):
        print("QQ")
music = Spotify()
music.play()

#10 use of super() in inheritance

class MusicPlayer():
    def play(self):
        print("Play musiccccccccc")
class Spotify(MusicPlayer):
    def play(self):
        super().play()
        print("QQ")
music = Spotify()
music.play()