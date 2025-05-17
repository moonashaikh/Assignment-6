#16. Function Decorators Assignment:
#Write a decorator function   log_function_call that prints "Function is being called" before a function executes.
#  Apply it to a function say_hello().

#  Decorator function
def log_function_call(fun):
    def wrapper():
        print("Function is being called")
        return fun()     # call the original function
    return wrapper

# function to be decorated
@log_function_call

def say_hello():
     print("Hello World")
    
     say_hello()
     
    
    
    # 17- 17. Class Decorators
# Assignment:Create a class decorator add_greeting that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class Person.
    
    # class Decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Rushdie")
print(p.greet())  

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price,
# @price.setter to update it, and @price.deleter to delete it.    

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Get the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price."""
        del self._price
        
p = Product(100)
print(p.price)   # Output: 100

p.price = 150
print(p.price)   # Output: 150

del p.price
# print(p.price)  # This will raise AttributeError if uncommented, because _price is deleted

# 20. Creating a Custom Exception
# Assignment:Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this 
# exception if age < 18. Handle it with try...except.

# Define custom exception
class InvalidAgeError(Exception):
    """Exception raised when age is below 18."""
    pass

# Function that checks age
def check_age(age):
    if age < 25:
        raise InvalidAgeError("Age must be at least 25.")
    else:
        print("Age is valid.")

# Using try...except to handle the custom exception
try:
    check_age(16)  # You can change this value to test
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")


# 21. Make a Custom Class Iterable
# Assignment:  Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object 
# iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage
for number in Countdown(5):
    print(number)
