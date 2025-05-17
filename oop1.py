# 11. Class Methods 
# Assignment: Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    # class variable to track the total number of books
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

# Creating new book objects (outside the class definition)
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

# Accessing the class variable
print(f"Total Books: {Book.total_books}")


# 12. Static Methods
# Assignment:# Create a class Temperature Converter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        # formula to convert celsius to fahrenheit
        return (c * 9/5) + 32    

# Calling the static method without creating an instance of the class
celsius = 25
fahrenheit = Temperature.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")

# 13. Composition
# Assignment: Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class 
# during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        
    def start(self):
        return f"The {self.engine_type} engine is starting"
    
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        # composition passing engine object to the car class
        self.engine = engine
        
    def start_car(self):
        # Access a method of the Engine class via the Car class
        return f"{self.brand} car is starting {self.engine.start()}"
        
# creating an engine object
engine = Engine("v8")

# creating a car object and passing the engine object to it
car = Car("Ford", engine)

# calling the start_car method which uses the Engine start method
print(car.start_car())

# 14. Aggregation
# Assignment:Create a class Department and a class Employee.Use aggregation by having a Department 
# object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_employee_info(self):
        return f"Employee Name : {self.name} , position : {self.position}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee
        
    def get_department_info(self):
        return f"Department Name : {self.department_name} , Employee : {self.employee.get_employee_info()}"
    
employee1 =Employee("Rushdie sheikh", "Software Engineer")
    
    #creating a department object and passing the employee object to it
    
department1 = Department("IT Department :-" , employee1)

# calling method to get department and employee info

print(department1.get_department_info())
        
    
# # 15-15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A")
        
class B(A):
    def show(self):
        print("B")
        
class C(A):
    def show(self):
        print("C")
        
class D(B,C):
    pass
d= D()
print(d.show())
        
        
        
        