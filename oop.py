# 1. Using self Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize
# these values via a constructor. Add a method display() that prints student details.

from curses.textpad import rectangle
# from doctest import BLANKLINE_MARKER


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

# Example usage
student1 = Student("Asad", 88)
student1.display()

student2 = Student("Abid", 98)
student2.display()
    
 
# 2. Using cls Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and 
#a class method with cls to manage and display the count.   
    
class Counter:
    object_count = 0  # class variable
    
    def __init__(self):
        # har object name per count increment hoga
        Counter.object_count +=1
        
    @classmethod
        
    def display_count(cls):
        print("Total object created:", cls.object_count)
        

# 3 object created
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()

#3. Public Variables and Methods Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand   # public variable
        
        
    def start(self):    #public method
        #print("Student Name:", self.name)
        print(f"{self.brand}")

# obect bana rahy hain
my_car = Car("Toyota")

# public variable access
print("Car brand:", my_car.brand)

# public method call
my_car.start()

#4. Class Variables and Class Methods assignment:
#Create a class Bank with a class variable bank_name. Add a class method 
# change_bank_name(cls, name) that allows changing the bank name. Show that it 
# affects all instances.


class Bank:
    bank_name = "Default Bank"    # class variable
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
        
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name   # updating class variable

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Object creation
user1 = Bank("Ali")
user2 = Bank("Sara")

# Display initial bank name
user1.display()
user2.display()

# Change bank name using class method
Bank.change_bank_name("Pakistan National Bank")

# Display updated bank name
user1.display()
user2.display()


# 5. Static Variables and Static Methods  Assignment: 5
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables 
# should be used.

class MathUtils:
    
    @staticmethod
    def add(a,b):
        return a+b
    
#  static method call(no object needed)
result =   MathUtils.add(10 , 15)
print("the sum is:" , result)
      
# 6. Constructors and Destructors Assignment: 6
# Create a class Logger that prints a message when an object is created (constructor) 
# and another message when it is destroyed (destructor).

class Logger:
    
#constructor

 def __init__(self):
      print("Logger object has been created")
      
      #destructor

def __del__(self):
      print("Logger object has been destructed")
      
# create an object of  logger class

logger1 = Logger()

# delete the object explicitly to invoke the destructor
del logger1

# 7. Access Modifiers: Public, Private, and Protected
# Assignment:# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what # happens.

class Employee:
    # public variable
    name = "Asad"
    
    # protected variable
    _salary = 50000
     
    # private variable
    __ssn = "324-45-5780"

# create an object of Employee class
emp = Employee()

# Accessing the public variable
print("Name:", emp.name)

# Accessing the protected variable
print("Salary:", emp._salary)

# Accessing the private variable (this will raise an error)
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error:", e)

# Accessing the private variable via name mangling
print("SSN (via name mangling):", emp._Employee__ssn)


# 8. The super() Function
# Assignment: Create a class Person with a constructor that sets the name. Inherit a 
# class Teacher from it, add a subject field, and use super() to call the base class 
# constructor.

# Base class person
class Person:
       def __init__(self, name):
           self.name = name
           
# derived class Teacher
class Teacher(Person):
       def __init__(self, name, subject):
           # Calling the base class constructor using super 
           super().__init__(name)
           self.subject = subject
           
       def display(self):
            print(f"Name:{self.name}")
            print(f"Subject:{self.subject}")   
            
# teacher class ka object bna rahy hain
teacher = Teacher("Mr. Ali jawed" , "Mathematics") 

# Teacher ka detail display kr rahy hain
teacher.display()   



# 9. Abstract Classes and Methods
# Assignment: Use the abc module to create an abstract class Shape with an abstract method 
# area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract class shape
class Shape(ABC):
   @abstractmethod
   def area(self):
       pass
   
# class Rectangle that inherits from shape and implements the area 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
         return self.width *  self.height 
     
# creating an object of Rectangle and calling the area method 
    rect = rectangle(5, 10, 10, 40)
    print(f"Area of Rectangle: {rect.area()}")
 
# 10. Instance Methods
# Assignment: Create a class Dog with instance variables name and breed. Add an instance method bark() that prints 
# a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        # instance method that prints a message with the dog's name
        print(f"{self.name} says woof!")
        
    # creating an object of the class dog
my_dog = Dog("Buddy" , "Golden Retriever")

# calling the bark method
my_dog.bark()