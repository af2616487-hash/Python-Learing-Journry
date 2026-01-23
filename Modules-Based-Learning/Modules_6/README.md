# Python Mastery: OOP & Error Handling

This repository serves as a comprehensive guide to mastering **Object-Oriented Programming (OOP)** and **Robust Error Handling** in Python. 

---

# 🧬 Part 1: Object-Oriented Programming (OOP)

## 🎯 What You Will Learn
* The fundamental shift from **Procedural** to **Object-Oriented** thinking.
* How to define **Classes** and instantiate **Objects**.
* Implementing the four core pillars: **Encapsulation, Inheritance, Polymorphism, and Abstraction**.
* Managing state using `self` and the `__init__` constructor.

---

<div align="center">

## 🧠 Key Concepts



| Concept | Description |
| :--- | :--- |
| **Classes & Objects** | The blueprint vs. the actual instance created from that blueprint. |
| **Encapsulation** | Keeping data and methods safe inside a class to prevent outside interference. |
| **Inheritance** | Allowing one class to derive features from another, promoting code reuse. |
| **Polymorphism** | Allowing different objects to respond to the same method call in their own way. |
| **Abstraction** | Hiding complex implementation details and showing only necessary features. |

</div>

---
# 💻 Code Examples

Check out the code snippet below to see these concepts in action. You can replace this with your own implementation!

```python
#Code1
def safe_division():
    try:
        numerator_input = input()
        denominator_input = input()
        numerator = float(numerator_input)
        denominator = float(denominator_input)
        result = numerator / denominator
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    safe_division()


#Code2
def perform_division():
    try:
        num1 = input()
        num2 = input()
        numerator = float(num1)
        denominator = float(num2)
        
        result = numerator / denominator
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    perform_division()


#Code3
def division_with_else():
    try:
        num1 = input()
        num2 = input()
        
        numerator = float(num1)
        denominator = float(num2)
        
        result = numerator / denominator
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(result)

if __name__ == "__main__":
    division_with_else()


#Code4
def division_with_finally():
    try:
        # Code that might cause an error
        num1 = input()
        num2 = input()
        
        numerator = float(num1)
        denominator = float(num2)
        
        result = numerator / denominator
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("This message is from the finally block, always executed.")

if __name__ == "__main__":
    division_with_finally()


#Code5
class AgeEligibilityError(Exception):
    pass

def check_voting_eligibility():
    try:
        age_input = input()
        age = int(age_input)
        if age < 18:
            raise AgeEligibilityError("You must be at least 18 years old to vote.")
        else:
            print("You are eligible to vote.")
    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
    except AgeEligibilityError as e:
        print(e)

if __name__ == "__main__":
    check_voting_eligibility()


#Code6
def add_integers():
    try:
        val1 = input()
        val2 = input()
        num1 = int(val1)
        num2 = int(val2)
        
        result = num1 + num2
        print(result)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    add_integers()


#Code7
class NegativeNumberError(Exception):
    pass

def check_number():
    try:
        user_input = input()
        number = float(user_input)
        if number < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")
        else:
            print("Valid number.")
    except ValueError:
        print("Error: Please enter a valid numeric value.")
    except NegativeNumberError as e:
        print(e)

if __name__ == "__main__":
    check_number()


#Code8
def divide_numbers():
    try:
        numerator = float(input())
        denominator = float(input())
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    divide_numbers()


#Code9
def handle_integer_input():
    try:
        user_input = input()
        
        number = int(user_input)
        
        print(f"You entered the integer: {number}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

    except TypeError:
        print("Error: An inappropriate type was encountered.")

if __name__ == "__main__":
    handle_integer_input()


#Code10
def division_demo():
    try:
        numerator = float(input())
        denominator = float(input())
        
        result = numerator / denominator
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    except ValueError:
        print("Execution of the try-except block is complete.")
    finally:
        print("Execution of the try-except block is complete.")

if __name__ == "__main__":
    division_demo()


#Code11
def check_positive(number):
    if number <= 0:
        raise ValueError("The number must be positive.")
    else:
        print("The number is positive.")

def main():
    try:
        user_input = input()
        val = float(user_input)
        
        check_positive(val)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


#Code12
class NegativeValueError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise NegativeValueError("Negative values are not allowed.")
    else:
        print("The value is positive.")

def main():
    try:
        user_input = input()
        num = float(user_input)
        
        check_value(num)
    except NegativeValueError as e:
        print(e)
    except ValueError:
        print("Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    main()

```

---

<div align="center">

## 📝 Summary
Object-Oriented Programming organizes software design around **data**, or objects, rather than functions and logic. By mastering OOP, you make your code more **readable**, **maintainable**, and **scalable** for real-world applications.

</div>

---

# ⚠️ Part 2: Error Handling

## 🎯 What You Will Learn
* The difference between **Syntax Errors** and **Exceptions**.
* How to use the `try`, `except`, `else`, and `finally` blocks.
* Raising custom exceptions to enforce business logic.
* Writing "defensive code" that prevents program crashes.

---

<div align="center">

## 🧠 Key Concepts



**The Exception Lifecycle**

1. **Try:** Test a block of code for errors.
2. **Except:** Handle the error if one occurs.
3. **Else:** Execute code if *no* errors were raised.
4. **Finally:** Execute code regardless of the result (cleanup).

</div>

---

<div align="center">

## 📝 Summary
Error handling is about **graceful degradation**. Instead of allowing a program to crash with a traceback, you provide helpful feedback, ensure system stability, and make debugging much faster.

</div>

---

## 📚 Learning Resources

### OOP Resources
* [Official Python Docs: Classes](https://docs.python.org/3/tutorial/classes.html)
* [Real Python: OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)

### Error Handling Resources
* [Official Python Docs: Errors](https://docs.python.org/3/tutorial/errors.html)
* [Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

---

## 🛠️ Installation & Usage
1. Clone the repo: `git clone https://github.com/yourusername/repo-name.git`
2. Run the examples: `python main.py`
