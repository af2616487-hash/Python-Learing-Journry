<img src="Bytexl.svg" width="140" align="left"/>

<br clear="left"/>

# Introduction to Functions

## Python Learning Journey


<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=2000&color=00D4FF&center=true&width=900&lines=%F0%9F%93%8B+Plan+%F0%9F%8F%97%EF%B8%8F+Build+%F0%9F%9A%80+Deploy+%F0%9F%92%8E+Bytexl" />


## Overview

A function is a reusable block of code that performs a specific task. Instead of writing the same code again and again, you put it inside a function and call it whenever needed.

1. Why Functions Are Used

✅ Code reusability – write once, use many times

✅ Modularity – break big problems into smaller parts

✅ Readability – code becomes easier to understand

✅ Easy debugging – errors are easier to find and fix

2. Basic Structure of a Function

Most functions have:

Function name

Parameters (inputs) – optional

Function body – code to execute

Return value – optional output

---



## 1. Functions




```python

#code1) 
def demo(*args):
  print("Packed Arguments:", args)
  for x in args:
    print("Unpacked:", x)

nums = list(map(int, input().split()))
demo(*nums)

#code2) 
def operations(a, b):
  yield "Addition", a + b
  yield "Subtraction", a - b
  yield "Multiplication", a * b
  yield "Division", a // b

x = int(input())
y = int(input())

for name, value in operations(x, y):
    print(name + ":")
    print(value)

#code3) 
nums = list(map(int, input().split()))
doubled = list(map(lambda x: x * 2, nums))
print(doubled)


#code4) 
n = int(input())
square = lambda x: x * x
print(square(n))


#code5) 
def greet(name):
  print(f"Hello, {name}! Welcome!")
  
name = input()
greet(name)


#code6) 
n = int(input())
products = [tuple(input().split()) for _ in range(n)]
products = [(name, float(price)) for name, price in products]

filtered = list(filter(lambda x: x[1] >= 1000, products))
discounted = list(map(lambda x: (x[0], round(x[1]*0.85, 2)), filtered))

print(discounted)


#code7) 
def top_scorers(students):
  max_score = -1
  for score in students.values():
    if score > max_score:
      max_score = score
  result = [name for name, score in students.items() if score == max_score]
  return sorted(result)

n = int(input())
students = {}
for _ in range(n):
    name, score = input().split()
    students[name] = int(score)

print(top_scorers(students))


#code8
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    try:
        n = int(input_data[ptr])
        ptr += 1
    except:
        return
        
    students = []
    for _ in range(n):
        name = input_data[ptr]
        age = int(input_data[ptr+1])
        score = int(input_data[ptr+2])
        city = input_data[ptr+3]
        students.append({'name': name, 'age': age, 'score': score, 'city': city})
        ptr += 4
        
    try:
        m = int(input_data[ptr])
        ptr += 1
    except:
        m = 0
        
    filter_names = []
    for _ in range(m):
        filter_names.append(input_data[ptr].lower().strip())
        ptr += 1
        
    params = input_data[ptr:]
    p_ptr = 0
    
    conditions = []
    for f in filter_names:
        if f == "age_above":
            v = int(params[p_ptr]); p_ptr += 1
            conditions.append(lambda s, v=v: s['age'] > v)
        elif f == "age_below":
            v = int(params[p_ptr]); p_ptr += 1
            conditions.append(lambda s, v=v: s['age'] < v)
        elif f == "score_above":
            v = int(params[p_ptr]); p_ptr += 1
            conditions.append(lambda s, v=v: s['score'] > v)
        elif f == "score_below":
            v = int(params[p_ptr]); p_ptr += 1
            conditions.append(lambda s, v=v: s['score'] < v)
        elif f == "score_between":
            v1 = int(params[p_ptr]); v2 = int(params[p_ptr+1]); p_ptr += 2
            low, high = min(v1, v2), max(v1, v2)
            conditions.append(lambda s, l=low, h=high: l <= s['score'] <= h)
        elif f == "city_is":
            t = params[p_ptr].lower(); p_ptr += 1
            conditions.append(lambda s, t=t: s['city'].lower() == t)
        elif f == "name_starts_with":
            p = params[p_ptr].lower(); p_ptr += 1
            conditions.append(lambda s, p=p: s['name'].lower().startswith(p))
        elif f == "age_is":
            v = int(params[p_ptr]); p_ptr += 1
            conditions.append(lambda s, v=v: s['age'] == v)
    def student_matches(student):
        return all(cond(student) for cond in conditions)

    result_students = [s for s in students if student_matches(s)]
    names = sorted([s['name'] for s in result_students])
    if names:
        sys.stdout.write("\n".join(names) + "\n")

if __name__ == "__main__":
    solve()

```

## 2. Function Arguments Basics




```python
#Code1) 
def add_numbers(a, b):
  return a + b

x = int(input())
y = int(input())

result = add_numbers(x, y)
print(result)


#Code2) 
def add_numbers(a, b):
  return a + b

x = int(input())
y = int(input())

print(add_numbers(x, y))

#Code3) 
def sum_all(*args):
  return sum(args)

numbers = list(map(int, input().split()))
print(sum_all(*numbers))


#Code4) 
def calculate(a, b):
  return a + b, a - b

x = int(input())
y = int(input())

sum_result, diff_result = calculate(x, y)
print(sum_result)
print(diff_result)


#Code5) 
def calculate_average(a, b, c):
  return (a + b + c) / 3

a, b, c = map(int, input().split())

avg = calculate_average(a, b, c)
print(f"{avg:.2f}")


#Code6) 
def generate_bill(name, items, discount=0):
  total = sum(items)
  total -= total * (discount / 100)
  return total

name = input().strip()
items = list(map(float, input().split()))

try:
    discount = int(input().strip())
except:
    discount = 0

final_amount = generate_bill(name, items, discount)
print(f"{final_amount:.2f}")

#Code7) 
def grade_student(name, score, passing_score=40, grade='F'):
 result = "Passed" if score >= passing_score else "Failed"
 return f"{name}: {result} with grade {grade}"

name = input().strip()
score = int(input().strip())

passing_score = 40
grade = 'F'

try:
    extra = input().strip()
    parts = extra.split()
    for part in parts:
        key, value = part.split('=')
        if key == "passing_score":
            passing_score = int(value)
        elif key == "grade":
            grade = value
except:
    pass

print(grade_student(name, score, passing_score=passing_score, grade=grade))


#Code8) 
import sys

def dynamic_processor(operation, *args):
    if not args:
        if operation == 'add': return 0
        if operation == 'multiply': return 0
        return None

    if operation == 'add':
        return sum(args)
    
    elif operation == 'multiply':
        product = 1
        for num in args:
            product *= num
        return product
    
    elif operation == 'find_max':
        return max(args)
    
    elif operation == 'find_min':
        return min(args)

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    for _ in range(n):
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        operation = parts[0]
        params = list(map(int, parts[1:]))
        result = dynamic_processor(operation, *params)
        
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()

```

## 3. Advanced Function Arguments



```python
#Code1
def greet(name, greeting="Hello"):
  if greeting.strip() == "":
      greeting = "Hello"
  print(f"{greeting}, {name}!")

name = input().strip()
greeting = input()

greet(name, greeting)


#Code2
def describe_pet(name, pet_type="dog"):
  print(f"I have a {pet_type} named {name}.")

name = input().strip()
pet_type = input().strip()

if pet_type == "":
    describe_pet(name=name)
else:
    describe_pet(name=name, pet_type=pet_type)


#Code3
def greet_user(name, greeting="Hello"):
  print(f"{greeting}, {name}!")

parts = input().strip().split()

if len(parts) == 1:
    name = parts[0]
    if name.isalpha():
        greet_user(name)
    else:
        print("Invalid input format.")
elif len(parts) == 2:
    name, greeting = parts
    if name.isalpha() and greeting.isalpha():
        greet_user(name, greeting)
    else:
        print("Invalid input format.")
else:
    print("Invalid input format.")


#Code4
def add_numbers(a, b=10):
  print(a + b)

parts = input().split()

if len(parts) == 1:
    add_numbers(int(parts[0]))
else:
    add_numbers(int(parts[0]), int(parts[1]))


#Code5
def full_name(first, last, sep=" "):
  return first + sep + last

parts = input().split()

if len(parts) == 2:
    first, last = parts
    print(full_name(first, last))
else:
    first, last, sep = parts
    print(full_name(first, last, sep=sep))


#Code6
def merge_and_multiply(a, b, *args):
  nums = [a, b] + list(args)
  nums.sort(reverse=True)
  product = 1
  for x in nums:
    product *= x
  return nums, product

a, b = map(int, input().split())
line = input().strip()

if line == "":
    sorted_list, prod = merge_and_multiply(a, b)
else:
    args = list(map(int, line.split()))
    sorted_list, prod = merge_and_multiply(a, b, *args)

print(sorted_list)
print(prod)


#Code7
def filter_and_sum(limit, *numbers):
  total = 0
  for x in numbers:
    if x < limit and x % 2 == 0:
          total += x
  return total

limit = int(input().strip())
numbers = list(map(int, input().split()))

print(filter_and_sum(limit, *numbers))


#Code8
n = int(input().strip())

params = []
defaults = {}

for _ in range(n):
    line = input().strip()
    if '=' in line:
        name, default = line.split('=')
        params.append(name)
        defaults[name] = default
    else:
        params.append(line)

m = int(input().strip())

for _ in range(m):
    call = input().strip()
    if call == "":
        args = []
    else:
        args = call.split(',')

    values = {}
    pos_index = 0
    error = False

    for arg in args:
        if '=' in arg:
            key, val = arg.split('=')
            if key not in params or key in values:
                error = True
                break
            values[key] = val
        else:
            if pos_index >= len(params):
                error = True
                break
            if params[pos_index] in values:
                error = True
                break
            values[params[pos_index]] = arg
            pos_index += 1

    if error:
        print("ERROR")
        continue

    result = []
    for p in params:
        if p in values:
            result.append(values[p])
        elif p in defaults:
            result.append(defaults[p])
        else:
            error = True
            break

    if error:
        print("ERROR")
    else:
        print(result)

```

## 4. Recursion



```python
#Code1
def factorial(n):
  if n == 0 or n == 1:
      return 1
  return n * factorial(n - 1)

try:
    n = int(input().strip())
    if 0 <= n <= 20:
        print(factorial(n))
    else:
        print("Invalid input")
except:
    print("Invalid input")


#Code2
def print_reverse(n):
  if n == 0:
      return
  print(n, end=" ")
  print_reverse(n - 1)

n = int(input().strip())
print_reverse(n)


#Code3
n, m = map(int, input().split())
print(sum(range(n, m + 1)))


#Code4
def print_even(n):
  if n < 2:
      return
  print_even(n - 1)
  if n % 2 == 0:
      print(n)

N = int(input().strip())
print_even(N)


#Code5
def power(a, b):
  if b == 0:
      return 1
  return a * power(a, b - 1)

a, b = map(int, input().split())
print(power(a, b))


#Code6
def sum_alternate_digits(n):
  if n == 0:
      return 0
  return n % 10 + sum_alternate_digits(n // 100)

n = int(input().strip())
print(sum_alternate_digits(n))


#Code7
def count_ways(n):
  if n == 0:
      return 1
  if n < 0:
      return 0
  return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

n = int(input().strip())
print(count_ways(n))


#Code8
def matrix_multiply(A, B, n):
  result = [[0]*n for _ in range(n)]

  def multiply_cell(i, j, k):
      if k == n:
          return 0
      return A[i][k] * B[k][j] + multiply_cell(i, j, k + 1)

  def fill_matrix(i, j):
      if i == n:
          return
      if j == n:
          fill_matrix(i + 1, 0)
          return
      result[i][j] = multiply_cell(i, j, 0)
      fill_matrix(i, j + 1)

  fill_matrix(0, 0)
  return result


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

res = matrix_multiply(A, B, n)
for row in res:
    print(*row)

```


## Summary

🧾 Summary (Exam-Friendly)

A function is defined once and can be used multiple times

It may accept input (parameters) and may return output

Functions improve reusability, modularity, and readability

  - Types of functions:

  - Built-in functions

User-defined functions

Functions help break complex problems into smaller, manageable parts

Variables inside functions usually have local scope

## Learning Resources

Beginner (Strong Basics)

W3Schools – Python Functions
Easy language, good examples
👉 https://www.w3schools.com/python/python_functions.asp

GeeksforGeeks – Functions in Python
Concept + examples + interview focus
👉 https://www.geeksforgeeks.org/python-functions/

Python Official Docs (Simple Explanation)
👉 https://docs.python.org/3/tutorial/controlflow.html#defining-functions

🔹 Practice-Based Learning

HackerRank – Python Functions Practice
👉 https://www.hackerrank.com/domains/tutorials/10-days-of-python

CodeChef – Beginner Python Problems
👉 https://www.codechef.com/practice/python

🔹 Video Learning (Recommended for You)

CodeWithHarry – Python Functions (Hindi)
Very clear for Indian students 🇮🇳
👉 YouTube: CodeWithHarry Python Functions

Apna College – Python in One Shot
👉 YouTube: Apna College Python
