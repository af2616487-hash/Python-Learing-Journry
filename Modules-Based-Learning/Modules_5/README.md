<img src="Bytexl.svg" width="140" align="left"/>

<br clear="left"/>

# Introduction to OOP in Python

## Python Learning Journey


<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=2000&color=00D4FF&center=true&width=900&lines=%F0%9F%93%8B+Plan+%F0%9F%8F%97%EF%B8%8F+Build+%F0%9F%9A%80+Deploy+%F0%9F%92%8E+Bytexl" />


## Overview

Welcome to the Introduction to Object-Oriented Programming (OOP) in Python repository! This project is designed to help you transition from writing linear, procedural scripts to building scalable, modular, and reusable code using classes and objects.

### 🎯 What You Will Learn:

By exploring this repository, you will gain a solid foundation in:

- The fundamental shift from Procedural to Object-Oriented thinking.

- How to define Classes and instantiate Objects.

- Managing data and logic using Attributes and Methods.

- Implementing the four core pillars of OOP to write "DRY" (Don't Repeat Yourself) code.

- Best practices for Pythonic class design.

### 🧠 Key Concepts:

1. Classes and Objects
Think of a Class as a blueprint (e.g., a drawing of a car) and an Object as the actual house built from that blueprint (e.g., the specific car in your driveway).

2. The Four Pillars of OOP
To master OOP, you must understand these four concepts:

   - Encapsulation: Grouping data (attributes) and methods together while hiding the internal state from the outside world using private variables.

   - Inheritance: Allowing a new class (child) to adopt the properties of an existing class (parent), promoting code reuse.

   - Polymorphism: The ability for different classes to be treated as instances of the same general class through the same interface (e.g., a square.draw() and  circle.draw() method).

   - Abstraction: Hiding complex implementation details and showing only the necessary features of an object.

3. The __init__ Method and self
In Python, the __init__ method is the constructor that initializes an object’s attributes when it is created. The self parameter represents the specific instance of the object.




## 1. Classes and Objects

---


```python
#Code1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Dog's Name: {self.name}, Age: {self.age}")


name = input()
age = int(input())


my_dog = Dog(name, age)
my_dog.display_info()


#Code2
class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_details(self):
        return f"{self.make} {self.model} has {Car.wheels} wheels."



if __name__ == "__main__":
  
    make1 = input()
    model1 = input()

    make2 = input()
    model2 = input()

    car1 = Car(make1, model1)
    car2 = Car(make2, model2)

    print(car1.display_details())
    print(car2.display_details())



#Code3
class Student:
    """
    Represents a student with a name and their marks.
    """
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


if __name__ == "__main__":
    user_input = input("")

    try:
        last_space_index = user_input.rfind(' ')
        if last_space_index == -1:
            raise ValueError("Invalid input format. Name and marks must be separated by a space.")
            
        name = user_input[:last_space_index]
        marks_str = user_input[last_space_index + 1:]
        
        marks = int(marks_str)
        student1 = Student(name, marks)
        print(student1.name)
        if student1.marks >= 40:
            print("Pass")
        else:
            print("Fail")

    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure marks are a valid integer and the format is correct.")




#Code4
class Vault:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds for withdrawal.")
            
    def display_final_balance(self):
        print(f"Vault {self.name}: Balance {self.balance}")


if __name__ == "__main__":
    vault_name = input()
    initial_balance = int(input())
    deposit_amount = int(input())
    withdraw_amount = int(input())
    my_vault = Vault(vault_name, initial_balance)
    my_vault.deposit(deposit_amount)
    my_vault.withdraw(withdraw_amount)
    my_vault.display_final_balance()



#Code5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        

if __name__ == "__main__":
    name_input = input().strip()
    age_input = int(input().strip())
    person = Person(name_input, age_input)
    person.display_info()



#Code6
class Book:
    pass

my_book = Book()

user_input = input().split()

my_book.title = user_input[0]
my_book.author = user_input[1]
my_book.price = float(user_input[2])

print(f"Title: {my_book.title}")
print(f"Author: {my_book.author}")
print(f"Price: {my_book.price:.2f}") 



#Code7
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_average(self):
        average = (self.mark1 + self.mark2 + self.mark3) // 3
        return average

    def display_result(self):
        average = self.calculate_average()
        status = "Pass" if average >= 40 else "Fail"
        print(f"Student {self.name}: Average {average} - {status}")


def get_multiline_user_input_and_run():
    try:
        name = input()
        m1 = int(input())
        m2 = int(input())
        m3 = int(input())

        user_student = Student(name, m1, m2, m3)


        user_student.display_result()

    except ValueError:
        print("Error: Invalid input for marks. Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_multiline_user_input_and_run()




#Code8
import sys

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course.course_name)
        course.enrolled_students.append(self.student_id)

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    line_ptr = 0
    
    s_count = int(input_data[line_ptr].strip())
    line_ptr += 1
    students_list = []
    students_dict = {}
    for _ in range(s_count):
        parts = input_data[line_ptr].strip().rsplit(' ', 1)
        name = parts[0]
        sid = int(parts[1])
        line_ptr += 1
        new_student = Student(name, sid)
        students_list.append(new_student)
        students_dict[sid] = new_student

    c_count = int(input_data[line_ptr].strip())
    line_ptr += 1
    courses_list = []
    courses_dict = {}
    for _ in range(c_count):
        parts = input_data[line_ptr].strip().rsplit(' ', 1)
        cname = parts[0]
        ccode = parts[1]
        line_ptr += 1
        new_course = Course(cname, ccode)
        courses_list.append(new_course)
        courses_dict[ccode] = new_course

    e_count = int(input_data[line_ptr].strip())
    line_ptr += 1
    for _ in range(e_count):
        enroll_parts = input_data[line_ptr].strip().split()
        if len(enroll_parts) < 2:
            continue
        sid = int(enroll_parts[0])
        ccode = enroll_parts[1]
        line_ptr += 1
        if sid in students_dict and ccode in courses_dict:
            students_dict[sid].enroll(courses_dict[ccode])

    for s in students_list:
        print(f"Student: {s.name}, ID: {s.student_id}, Courses: {s.courses}")

    for c in courses_list:
        print(f"Course: {c.course_name}, Code: {c.course_code}, Enrolled Students: {c.enrolled_students}")

if __name__ == "__main__":
    solve()

```

## 2. Attributes and Methods

---

```python
#Code1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def run_rectangle_program():
    try:
        length_input = int(input().strip())
        width_input = int(input().strip())
        if not (1 <= length_input <= 10000 and 1 <= width_input <= 10000):
            print("Error: Dimensions must be between 1 and 10000.")
            return
        rect = Rectangle(length_input, width_input)
        area = rect.calculate_area()
        perimeter = rect.calculate_perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

    except ValueError:
        print("Error: Please enter valid numeric floats for length and width.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    run_rectangle_program()



#Code2
class MathOperations:
    @staticmethod
    def square(number):
        return number * number

def run_square_program():
    try:
        input_number = int(input().strip())
        result = MathOperations.square(input_number)
        print(result)

    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    run_square_program()



#Code3
import math

class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.PI * self.radius * self.radius

    def calculate_circumference(self):
        return 2 * self.PI * self.radius

def run_circle_program():
    try:
        radius_input = float(input().strip())
        circle = Circle(radius_input)
        area = circle.calculate_area()
        circumference = circle.calculate_circumference()
        print(f"Area: {area:.2f}")
        print(f"Circumference: {circumference:.2f}")

    except ValueError:
        print("Error: Please enter a valid numeric float for the radius.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    run_circle_program()



#Code4
class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius

def run_circle_area_program():
    try:
        radius_input = float(input().strip())
        if not (1 <= radius_input <= 1000):
            return
        circle = Circle(radius_input)
        calculated_area = circle.area()
        print(calculated_area)

    except ValueError:
        print("Error: Please enter a valid numeric float for the radius.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    run_circle_area_program()



#Code5
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


title = input().strip()
author = input().strip()
book = Book(title, author)
book.print_info()



#Code6
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def display_product(self):
        print(f"{self.name} {self.price:.2f}")


name = input().strip()
price = float(input().strip())
discount_percentage = int(input().strip())

product = Product(name, price)

product.apply_discount(discount_percentage)
product.display_product()



#Code7
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient Balance")
            return False

    def display(self):
        print(self.balance)


account_holder = input().strip()
deposit_amount, withdraw_amount = map(int, input().split())

account = BankAccount(account_holder)

account.deposit(deposit_amount)
success = account.withdraw(withdraw_amount)

if success:
    account.display()
else:
    account.display()




#Code8
class Shape:
    def __init__(self, shape_type, size):
        self.shape_type = shape_type
        self.size = size

    def resize(self, factor):
        self.size *= factor

    def morph(self, new_shape_type):
        self.shape_type = new_shape_type

    def combine(self, other_shape):
        new_shape_type = self.shape_type + "-" + other_shape.shape_type
        new_size = self.size + other_shape.size
        return Shape(new_shape_type, new_size)


n = int(input())
shapes = []

for _ in range(n):
    shape_type, size = input().split()
    shapes.append(Shape(shape_type, int(size)))

m1 = int(input())
for _ in range(m1):
    index, factor = input().split()
    shapes[int(index) - 1].resize(int(factor))

m2 = int(input())
for _ in range(m2):
    index, new_shape_type = input().split()
    shapes[int(index) - 1].morph(new_shape_type)

m3 = int(input())
combined_shapes = []

for _ in range(m3):
    index1, index2 = map(int, input().split())
    new_shape = shapes[index1 - 1].combine(shapes[index2 - 1])
    combined_shapes.append(new_shape)

for shape in shapes + combined_shapes:
    print(f"Shape: {shape.shape_type}, Size: {shape.size}")


```

## 3. Encapsulation

---

```python
#Code1
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


initial_balance = float(input())
deposit_amount = float(input())
withdrawal_amount = float(input())

account = BankAccount(initial_balance)

account.deposit(deposit_amount)
account.withdraw(withdrawal_amount)

print(account.get_balance())



#Code2
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Successful: {self.__balance}")
        else:
            print("Deposit Failed")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal Successful: {self.__balance}")
        else:
            print("Withdrawal Failed")

    def display_balance(self):
        return self.__balance


initial_balance = int(input())
deposit_amount = int(input())
withdrawal_amount = int(input())

account = BankAccount(initial_balance)

account.deposit(deposit_amount)
account.withdraw(withdrawal_amount)



#Code3
class Student:
    def __init__(self):
        self.__grade = None  

    def set_grade(self, grade):
        if isinstance(grade, int) and 0 <= grade <= 100:
            self.__grade = grade
            print(f"Grade set to: {grade}")
        else:
            print("Grade must be between 0 and 100.")

    def get_grade(self):
        return self.__grade
grade_input = int(input().strip())
student = Student()
student.set_grade(grade_input)



#Code4
class BankAccount:
    def __init__(self):
        self.__balance = 0  

    def deposit(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__balance += amount
            print(f"Balance after deposit: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if isinstance(amount, int) and amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Balance after withdrawal: {self.__balance}")
            else:
                print("Withdrawal failed: Insufficient funds")
        else:
            print("Invalid withdrawal amount")
account = BankAccount()
deposit_amt = int(input().strip())
withdraw_amt = int(input().strip())
account.deposit(deposit_amt)
account.withdraw(withdraw_amt)



#Code5
class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 5 <= age <= 100:
            self.__age = age
        else:
            print(f"Invalid age. Age must be between 5 and 100.")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

student = Student()
name = input().strip()
age = int(input().strip())

student.set_name(name)
student.set_age(age)

print(f"Student Name: {student.get_name()}, Age: {student.get_age()}")



#Code6
import sys

class InventoryItem:
    def __init__(self, item_name):
        self.__item_name = item_name
        self.__stock = 0

    def restock(self, quantity):
        if quantity > 0:
            self.__stock += quantity

    def sell(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return self.__stock
        else:
            return "Insufficient stock"

    def get_stock(self):
        return self.__stock

    def get_item_name(self):
        return self.__item_name

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    item_name = data[0]
    num_ops = int(data[1])
    
    item = InventoryItem(item_name)
    
    idx = 2
    for _ in range(num_ops):
        operation = data[idx]
        quantity = int(data[idx+1])
        idx += 2
        
        if operation == "restock":
            item.restock(quantity)
        elif operation == "sell":
            result = item.sell(quantity)
            print(result)

if __name__ == "__main__":
    solve()


#Code7
import sys

class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            return True
        else:
            return False

    def get_marks(self):
        return self.__marks

    def display_info(self):
        print(self.__name)
        print(self.__marks)

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    name = input_data[0].strip()
    
    try:
        marks = int(input_data[1].strip())
    except (ValueError, IndexError):
        return

    student = Student(name)
    if student.set_marks(marks):
        student.display_info()
    else:
        print("Invalid Marks")

if __name__ == "__main__":
    solve()


#Code8
class Vault:
    def __init__(self, vault_id, balance):
        self._balance = balance
        self._vault_id = vault_id
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
    
    def display_vault(self):
        return f"Vault {self._vault_id}: Balance {self._balance}"

n = int(input().strip())
vaults = []

for i in range(n):
    line = input().strip().split()
    vault_id = line[0]
    balance = int(line[1])
    vaults.append(Vault(vault_id, balance))

q = int(input().strip())

for _ in range(q):
    line = input().strip().split()
    operation = line[0]
    vault_index = int(line[1]) - 1 
    amount = int(line[2])
    
    if 0 <= vault_index < len(vaults):
        if operation == "deposit":
            vaults[vault_index].deposit(amount)
        elif operation == "withdraw":
            vaults[vault_index].withdraw(amount)

for vault in vaults:
    print(vault.display_vault())


```

## 4. Inheritance

---


```python
#Code1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def introduce(self):
        print(f"{self.name} I am a student")

name = input().strip()
student = Student(name)
student.introduce()



#Code2
class Display:
    def show_display(self):
        print("Display: Touchscreen")

class Battery:
    def show_battery(self):
        print("Battery: 4000mAh")

class Smartphone(Display, Battery):
    def show_device(self):
        self.show_display()
        self.show_battery()
        print("Device: Smartphone")

def main():
    phone = Smartphone()
    
    try:
        user_input = input().strip().lower() 
    except EOFError:
        return

    if user_input == "display":
        phone.show_display()
    elif user_input == "battery":
        phone.show_battery()
    elif user_input == "smartphone":
        phone.show_device()
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()


#Code3
class Person:
    def show_name(self):
        print("I am a person")

class Employee(Person):
    def show_role(self):
        self.show_name()
        print("I am an employee")

class Manager(Employee):
    def show_department(self):
        self.show_role()
        print("I manage a department")

choice = input().strip().lower()
obj = None

if choice == "person":
    obj = Person()
    obj.show_name()
elif choice == "employee":
    obj = Employee()
    obj.show_role()
elif choice == "manager":
    obj = Manager()
    obj.show_department()



#Code4
class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def speak(self):
        print("I am a dog")

class Cat(Animal):
    def speak(self):
        print("I am a cat")

# Main execution
choice = input().strip().lower()

if choice == "dog":
    dog = Dog()
    dog.speak()
elif choice == "cat":
    cat = Cat()
    cat.speak()
else:
    print("Invalid Input")



#Code5
class ValueA:
    def __init__(self, val):
        self.a = val

class ValueB:
    def __init__(self, val):
        self.b = val

class Hybrid(ValueA, ValueB):
    def __init__(self, a, b):
        ValueA.__init__(self, a)
        ValueB.__init__(self, b)
    
    def calculate_sum(self):
        return self.a + self.b

a, b = map(int, input().split())
hybrid = Hybrid(a, b)
print(hybrid.calculate_sum())



#Code6
class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Staff(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    
    def get_department(self):
        return self.department

class Teacher(Staff):
    def __init__(self, name, department, subject):
        super().__init__(name, department)
        self.subject = subject
    
    def get_details(self):
        return f"{self.name} teaches {self.subject} in {self.department}"

class Admin(Staff):
    def get_role(self):
        return f"Admin - {self.name} from {self.department}"

role = input().strip()

if role == "Teacher":
    name = input().strip()
    department = input().strip()
    subject = input().strip()
    teacher = Teacher(name, department, subject)
    print(teacher.get_details())
elif role == "Admin":
    name = input().strip()
    department = input().strip()
    admin = Admin(name, department)
    print(admin.get_role())



#Code7
class WiFiEnabled:
    def wifi_status(self):
        return "WiFi On"

class BluetoothEnabled:
    def bluetooth_status(self):
        return "Bluetooth On"

class SmartDevice(WiFiEnabled, BluetoothEnabled):
    pass

class SmartSpeaker(SmartDevice):
    def __init__(self, model_name):
        self.model_name = model_name
    
    def get_status(self):
        return f"{self.model_name}: {self.wifi_status()}, {self.bluetooth_status()}"

model_name = input().strip()
speaker = SmartSpeaker(model_name)
print(speaker.get_status())



#Code8
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
    
    def show_employee(self):
        print(f"Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, team_size):
        Employee.__init__(self, name, age, employee_id)
        self.team_size = team_size
    
    def show_manager(self):
        print(f"Team Size: {self.team_size}")

class Trainer(Person):
    def __init__(self, name, age, specialization):
        Person.__init__(self, name, age)
        self.specialization = specialization
    
    def show_trainer(self):
        print(f"Specialization: {self.specialization}")

class TechLead(Manager, Trainer):
    def __init__(self, name, age, employee_id, team_size, specialization, project):
        Manager.__init__(self, name, age, employee_id, team_size)
        Trainer.__init__(self, name, age, specialization)
        self.project = project

data = input().strip().split()
name = data[0]
age = int(data[1])
emp_id = data[2]
team_size = int(data[3])
spec = data[4]
project = data[5]

techlead = TechLead(name, age, emp_id, team_size, spec, project)

techlead.show_person()
techlead.show_employee()
techlead.show_manager()
techlead.show_trainer()
print(f"Project: {techlead.project}")


```

## 5. Polymorphism

---

```python
#Code1
class Calculator:
    def add(self, num1, num2, num3=0):
        return num1 + num2 + num3

calc = Calculator()
num1 = int(input().strip())
num2 = int(input().strip())
try:
    num3 = int(input().strip())
except:
    num3 = 0

print(calc.add(num1, num2, num3))



#Code2
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

def make_animal_speak(animal):
    return animal.speak()

animal_type = input().strip()

if animal_type == "Cat":
    animal = Cat()
elif animal_type == "Dog":
    animal = Dog()
else:
    print("Unknown animal")
    exit()

print(make_animal_speak(animal))



#Code3
class Appliance:
    def calculateBill(self, hours):
        pass

class Fan(Appliance):
    def calculateBill(self, hours):
        units = (70 * hours * 30) / 1000
        bill = units * 6
        return "{:.2f}".format(bill)

class AirConditioner(Appliance):
    def calculateBill(self, hours):
        units = (1500 * hours * 30) / 1000
        bill = units * 6
        return "{:.2f}".format(bill)

class Refrigerator(Appliance):
    def calculateBill(self, hours):
        units = (200 * hours * 30) / 1000
        bill = units * 6
        return "{:.2f}".format(bill)

T = int(input().strip())

for _ in range(T):
    appliance_type = input().strip()
    H = int(input().strip())
    
    if appliance_type == "Fan":
        appliance = Fan()
    elif appliance_type == "AirConditioner":
        appliance = AirConditioner()
    elif appliance_type == "Refrigerator":
        appliance = Refrigerator()
    
    print(appliance.calculateBill(H))



#Code4
class Calculator:
    def multiply(self, num1, num2, num3=1):
        return num1 * num2 * num3

calc = Calculator()
num1 = int(input().strip())
num2 = int(input().strip())

try:
    num3 = int(input().strip())
except:
    num3 = 1

print(calc.multiply(num1, num2, num3))



#Code5
class DigitalDevice:
    def calculatePower(self, hours):
        pass

class Smartphone(DigitalDevice):
    def calculatePower(self, hours):
        return 15 * hours

class Laptop(DigitalDevice):
    def calculatePower(self, hours):
        return 50 * hours

class Smartwatch(DigitalDevice):
    def calculatePower(self, hours):
        return 5 * hours

T = int(input().strip())

for _ in range(T):
    device_type = input().strip()
    hours = int(input().strip())
    
    if device_type == "Smartphone":
        device = Smartphone()
    elif device_type == "Laptop":
        device = Laptop()
    elif device_type == "Smartwatch":
        device = Smartwatch()
    
    print(device.calculatePower(hours))



#Code6
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.1416
        return pi * self.radius * self.radius

shape = input().strip().lower()

if shape == "rectangle":
    length, breadth = map(int, input().strip().split())
    rect = Rectangle(length, breadth)
    print("{:.2f}".format(rect.area()))
elif shape == "circle":
    radius = int(input().strip())
    circle = Circle(radius)
    print("{:.2f}".format(circle.area()))



#Code7
class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, hours_worked, hourly_wage):
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage
    
    def calculate_salary(self):
        return self.hours_worked * self.hourly_wage

emp_type = input().strip().lower()

if emp_type == "fulltime":
    base, bonus = map(int, input().strip().split())
    emp = FullTimeEmployee(base, bonus)
elif emp_type == "parttime":
    hours, wage = map(int, input().strip().split())
    emp = PartTimeEmployee(hours, wage)

print(emp.calculate_salary())



#Code8
from abc import ABC, abstractmethod

class DigitProcessor(ABC):
    def __init__(self, digit_string):
        self.digit_string = digit_string

    @abstractmethod
    def process(self, extra_flag):
        pass


class SensorProcessor(DigitProcessor):
    def process(self, extra_flag):
        if extra_flag == "count_even":
            even_count = sum(1 for d in self.digit_string if int(d) % 2 == 0)
            print(f"[SUCCESS] Sensor processed {self.digit_string} with {even_count} even digits.")
        else:
            print("Error: Only Sensor can count even digits.")


class StreamProcessor(DigitProcessor):
    def process(self, extra_flag):
        if extra_flag != "None":
            print("Error: Only Sensor can count even digits.")
            return

        digit_sum = sum(map(int, self.digit_string))
        if digit_sum >= 100:
            print("Error: Digit sum exceeds limit.")
        else:
            print(f"[SUCCESS] Stream processed {self.digit_string} with digit sum {digit_sum}.")


class WirelessProcessor(DigitProcessor):
    def process(self, extra_flag):
        if extra_flag != "None":
            print("Error: Only Sensor can count even digits.")
            return

        digit_sum = sum(map(int, self.digit_string))

        for attempt in range(1, 4):
            print(f"Retrying Wireless processing for {self.digit_string}, attempt {attempt}...")

        if digit_sum % 2 != 0:
            print(f"Error: Wireless dispatch failed for {self.digit_string}")


priority_map = {"High": 1, "Medium": 2, "Low": 3}

n = int(input().strip())
entries = []

for _ in range(n):
    source, digit_string, priority, extra_flag = input().strip().split()
    entries.append((priority_map[priority], source, digit_string, extra_flag))

entries.sort(key=lambda x: x[0])

for _, source, digit_string, extra_flag in entries:
    if source == "Sensor":
        processor = SensorProcessor(digit_string)
    elif source == "Stream":
        processor = StreamProcessor(digit_string)
    elif source == "Wireless":
        processor = WirelessProcessor(digit_string)
    else:
        continue

    processor.process(extra_flag)


```

## 6. Abstraction

---

```python
#Code1
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def calculateToll(self, distance):
        pass

class Car(Vehicle):
    def calculateToll(self, distance):
        return distance * 1

class Bus(Vehicle):
    def calculateToll(self, distance):
        return distance * 2

class Truck(Vehicle):
    def calculateToll(self, distance):
        return distance * 3


T = int(input())

for _ in range(T):
    vehicle_type = input().strip()
    distance = int(input())

    if vehicle_type == "Car":
        vehicle = Car()
    elif vehicle_type == "Bus":
        vehicle = Bus()
    elif vehicle_type == "Truck":
        vehicle = Truck()

    print(vehicle.calculateToll(distance))




#Code2
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def calculateFee(self, amount):
        pass

class CreditCard(Payment):
    def calculateFee(self, amount):
        return amount * 0.02

class DebitCard(Payment):
    def calculateFee(self, amount):
        return amount * 0.01

class UPI(Payment):
    def calculateFee(self, amount):
        return 0.0


T = int(input())

for _ in range(T):
    method = input().strip()
    amount = float(input())

    if method == "CreditCard":
        payment = CreditCard()
    elif method == "DebitCard":
        payment = DebitCard()
    elif method == "UPI":
        payment = UPI()

    print(float(payment.calculateFee(amount)))



#Code3
from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def getGrade(self):
        pass

class TheoryCourse(Course):
    def __init__(self, scores):
        self.scores = scores

    def getGrade(self):
        avg = sum(self.scores) / 3

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

class LabCourse(Course):
    def __init__(self, result):
        self.result = result

    def getGrade(self):
        if self.result == 1:
            return "Pass"
        else:
            return "Fail"


T = int(input())

for _ in range(T):
    course_type = input().strip()

    if course_type == "TheoryCourse":
        scores = list(map(int, input().split()))
        course = TheoryCourse(scores)
    elif course_type == "LabCourse":
        result = int(input())
        course = LabCourse(result)

    print(course.getGrade())



#Code4
from abc import ABC, abstractmethod
import sys

class Employee(ABC):
    @abstractmethod
    def calculateSalary(self):
        pass

class Intern(Employee):
    def calculateSalary(self):
        return 5000

class FullTimeEmployee(Employee):
    def __init__(self, basic_pay):
        self.basic_pay = basic_pay
    def calculateSalary(self):
        return self.basic_pay + (0.3 * self.basic_pay) + (0.2 * self.basic_pay)

class Freelancer(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours
    def calculateSalary(self):
        return self.rate * self.hours

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        emp_type = data[idx]
        idx += 1
        
        if emp_type == "Intern":
            emp = Intern()
            print(emp.calculateSalary())
            
        elif emp_type == "FullTimeEmployee":
            pay = float(data[idx])
            idx += 1
            emp = FullTimeEmployee(pay)
            res = emp.calculateSalary()
            if res == int(res):
                print(f"{res:.1f}")
            else:
                print(res)
                
        elif emp_type == "Freelancer":
            rate = int(data[idx])
            hours = int(data[idx+1])
            idx += 2
            emp = Freelancer(rate, hours)
            print(emp.calculateSalary())

if __name__ == "__main__":
    solve()


#Code5
from abc import ABC, abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def calculateMonthlyFee(self):
        pass

class Bus(TransportMode):
    def calculateMonthlyFee(self):
        return 1500

class Van(TransportMode):
    def calculateMonthlyFee(self):
        return 2000

class Cycle(TransportMode):
    def calculateMonthlyFee(self):
        return 0


T = int(input())

for _ in range(T):
    mode = input().strip()

    if mode == "Bus":
        transport = Bus()
    elif mode == "Van":
        transport = Van()
    elif mode == "Cycle":
        transport = Cycle()

    print(transport.calculateMonthlyFee())



#Code6
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is now ON")

    def turn_off(self):
        print("Washing Machine is now OFF")


class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now ON")

    def turn_off(self):
        print("Refrigerator is now OFF")


try:
    n = int(input().strip())
except:
    n = 0

for _ in range(n):
    name = input().strip()

    appliance = None

    if name == "WashingMachine":
        appliance = WashingMachine()
    elif name == "Refrigerator":
        appliance = Refrigerator()

    if appliance:
        appliance.turn_on()
        appliance.turn_off()




#Code7
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


try:
    method = input().strip()
    amount = int(input().strip())
except:
    method = ""
    amount = 0


payment = None

if method == "CreditCard":
    payment = CreditCardPayment()
elif method == "UPI":
    payment = UPIPayment()

if payment:
    payment.pay(amount)




#Code8
from abc import ABC, abstractmethod
import sys

class Robot(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def move(self, direction, distance):
        pass

    @abstractmethod
    def energy_required(self, distance):
        pass

class WheeledRobot(Robot):
    def start(self):
        pass
    def stop(self):
        pass
    def energy_required(self, distance):
        return distance / 10.0
    def move(self, direction, distance):
        print(f"Wheeled robot moving {float(distance)}m towards {direction}.")
        print(f"Energy consumed: {self.energy_required(distance)} units")

class Drone(Robot):
    def start(self):
        pass
    def stop(self):
        pass
    def energy_required(self, distance):
        return distance * 2.0
    def move(self, direction, distance):
        if distance > 100:
            raise ValueError("Distance too far for drone")
        print(f"Drone flying {float(distance)}m towards {direction}.")
        print(f"Energy consumed: {self.energy_required(distance)} units")

class RoboticArm(Robot):
    def start(self):
        pass
    def stop(self):
        pass
    def energy_required(self, distance):
        return 5.0
    def move(self, direction, distance):
        valid_dirs = ['up', 'down', 'left', 'right']
        if direction not in valid_dirs:
            raise ValueError("Invalid direction for robotic arm")
        print(f"Robotic arm shifting {direction} by {float(distance)} units.")
        print(f"Energy consumed: {self.energy_required(distance)} units")

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        n = int(input_data[0].strip())
    except:
        return

    for i in range(1, n + 1):
        line = input_data[i].strip().split()
        if not line:
            continue
        
        r_type = line[0]
        direction = line[1]
        distance = float(line[2])

        if r_type == "Wheeled":
            bot = WheeledRobot()
        elif r_type == "Drone":
            bot = Drone()
        elif r_type == "RoboticArm":
            bot = RoboticArm()
        else:
            continue

        try:
            bot.start()
            bot.move(direction, distance)
            bot.stop()
        except ValueError:
            continue

if __name__ == "__main__":
    solve()

```

---
## 7. Decorators, iterators

---

```python
#Code1
import sys

def check_even_decorator(func):
    def wrapper(numbers):
        if all(n % 2 == 0 for n in numbers):
            return "All even"
        else:
            return "Not all even"
    return wrapper

@check_even_decorator
def process_numbers(numbers):
    pass

def main():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        
        nums = list(map(int, line.split()))
        result = process_numbers(nums)
        print(result)
        
    except EOFError:
        pass

if __name__ == "__main__":
    main()


#Code2
import sys

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

def solve():
    try:
        data = sys.stdin.read().split()
        if not data:
            return
            
        start = int(data[0])
        end = int(data[1])
        
        custom_range = MyRange(start, end)
        
        for num in custom_range:
            print(num)
            
    except (EOFError, IndexError):
        pass

if __name__ == "__main__":
    solve()


#Code3
import sys

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def solve():
    try:
        user_input = sys.stdin.read().strip()
        if not user_input:
            return

        @uppercase_decorator
        def get_string():
            return user_input

        print(get_string())
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()


#Code4
import sys

def repeat_three_times(func):
    def wrapper():
        result = func()
        for _ in range(3):
            print(result)
    return wrapper

def solve():
    try:
        user_input = sys.stdin.read().strip()
        if not user_input:
            return

        @repeat_three_times
        def get_message():
            return user_input

        get_message()
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()


#Code5
import sys

class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

def solve():
    try:
        data = sys.stdin.read().split()
        if not data:
            return
            
        start = int(data[0])
        end = int(data[1])
        
        my_iter = CustomRange(start, end)
        result = list(my_iter)
        print(result)
            
    except (EOFError, IndexError):
        pass

if __name__ == "__main__":
    solve()


#Code6
import sys

class EvenNumbers:
    def __init__(self, start, end):
        if start % 2 != 0:
            self.current = start + 1
        else:
            self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 2
            return val
        else:
            raise StopIteration

def solve():
    try:
        data = sys.stdin.read().split()
        if not data:
            return
            
        start = int(data[0])
        end = int(data[1])
        
        even_iter = EvenNumbers(start, end)
        
        for num in even_iter:
            print(num)
            
    except (EOFError, IndexError):
        pass

if __name__ == "__main__":
    solve()


#Code7
import sys

def square_decorator(func):
    def wrapper(n):
        result = func(n)
        return result * result
    return wrapper

@square_decorator
def get_number(n):
    return n

def solve():
    try:
        data = sys.stdin.read().strip()
        if not data:
            return
        
        n = int(data)
        print(get_number(n))
        
    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()


#Code8
import sys

class StringIterator:
    def __init__(self, strings):
        self.strings = strings
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.strings):
            res = self.strings[self.index]
            self.index += 1
            return res
        raise StopIteration

def capitalize_words(func):
    def wrapper(s):
        return func(s.title())
    return wrapper

def replace_vowels(func):
    def wrapper(s):
        vowels = "aeiouAEIOU"
        transformed = "".join(['*' if char in vowels else char for char in s])
        return func(transformed)
    return wrapper

def append_length(func):
    def wrapper(s):
        original_len = len(s)
        transformed = func(s)
        return f"{transformed} ({original_len})"
    return wrapper

def final_output(s):
    return s

@append_length
@replace_vowels
@capitalize_words
def transform_string(s):
    return final_output(s)

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0].strip())
    strings = input_data[1:n+1]
    
    it = StringIterator(strings)
    for s in it:
        print(transform_string(s))

if __name__ == "__main__":
    solve()


```
---
## 8. Generators, and Context Managers

---

```python
#Code1
import sys

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def solve():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        
        n = int(line)
        
        gen = fibonacci_generator(n)
        result = list(gen)
        print(result)
        
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    solve()


#Code2
import sys

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        n = int(input_data[0])
        labels = input_data[1:]
        
        published_count = labels.count("published")
        print(published_count)
        
    except (EOFError, ValueError, IndexError):
        pass

if __name__ == "__main__":
    solve()


#Code3
import sys

def generate_evens(n):
    for i in range(0, n, 2):
        yield i

def solve():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        
        n = int(line)
        evens = generate_evens(n)
        
        print(*(evens))
        
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    solve()


#Code4
import sys

def hello_decorator(func):
    def wrapper(message):
        return "Hello, " + func(message)
    return wrapper

@hello_decorator
def get_message(message):
    return message

def solve():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        
        print(get_message(input_data))
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()


#Code5
import sys
from contextlib import contextmanager

@contextmanager
def input_reader():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        yield []
    else:
        yield input_data

def solve():
    try:
        raw_input = sys.stdin.read().splitlines()
        if not raw_input:
            return
            
        n = int(raw_input[0].strip())
        lines = raw_input[1:n+1]

        with input_reader() as reader:
            for line in lines:
                print(line)
                
    except (EOFError, ValueError, IndexError):
        pass

if __name__ == "__main__":
    solve()


#Code6
import sys

class RangeGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total_sum = 0

    def __enter__(self):
        def generator():
            for i in range(self.start, self.end):
                self.total_sum += i
                yield i
        return generator()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.total_sum)

def solve():
    try:
        data = sys.stdin.read().split()
        if not data:
            return
            
        start = int(data[0])
        end = int(data[1])
        
        with RangeGenerator(start, end) as numbers:
            for num in numbers:
                pass
                
    except (EOFError, ValueError, IndexError):
        pass

if __name__ == "__main__":
    solve()


#Code7
import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

def solve():
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        
        n = int(line)
        gen = prime_generator(n)
        
        for prime in gen:
            print(prime)
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    solve()


#Code8
import sys

class LogFilterEnvironment:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.count)

def log_streamer(logs):
    for log in logs:
        yield log

def solve():
    try:
        input_data = sys.stdin.read().splitlines()
        if not input_data:
            return
            
        n = int(input_data[0].strip())
        logs = input_data[1:n+1]
        keyword = input_data[n+1].strip().lower()
        min_length = int(input_data[n+2].strip())

        with LogFilterEnvironment() as env:
            for log in log_streamer(logs):
                if keyword in log.lower() and len(log) >= min_length:
                    print(log)
                    env.count += 1
                    
    except (EOFError, ValueError, IndexError):
        pass

if __name__ == "__main__":
    solve()


```
---

## 📝 Summary

Object-Oriented Programming is a paradigm that organizes software design around data, or objects, rather than functions and logic. In Python, everything is an object. By mastering OOP, you make your code:

 1.  More Readable: It mirrors real-world entities.

 2. Easier to Maintain: Changes in one part of the code don't necessarily break others.

 3. Scalable: Large-scale applications are much easier to manage when broken down into objects.

## 📚 Learning Resources

Ready to dive deeper? Check out these highly recommended resources:

 - Official Python Documentation: Classes in Python

 - Real Python: Object-Oriented Programming (OOP) in Python 3

 - FreeCodeCamp: Python OOP Tutorial - YouTube

 - Interactive Practice: Exercism Python Track

