# Variables and Data Types in Python

## Overview
Learn the fundamentals of Python: variables, data types, type casting, and operators. Master working with integers, floats, strings, booleans, and apply these concepts through practical examples like temperature conversion and data classification.

**Topics:** Variables & case sensitivity | Data types | Type casting | String/Arithmetic operations | Logical operators | Real-world applications

**Learn to:** Create and manipulate variables | Work with different data types | Convert between types | Perform operations | Solve practical problems
[](url)---

## Table of Contents
1. [Variable Naming & Case Sensitivity](#1-variable-case-sensitivity)
2. [String Concatenation](#2-string-concatenation)
3. [String Data Type](#3-string-data-type)
4. [Float Arithmetic Operations](#4-float-arithmetic-operations)
5. [Temperature Conversion](#5-temperature-conversion)
6. [Mixed Data Type Operations](#6-mixed-data-type-operations)
7. [Data Type Classification](#7-data-type-classification)
8. [File Path Construction](#8-file-path-construction)

---

## 1. Variable And Data Type

**Concept:** Variables in Python are case-sensitive. `x` and `X` are different variables.

```python
#code1
x =int(input())
X =int(input())
print("Value of x:",x)
print("Value of x:",X)

#code2
greeting = "Hello"
name = input()

print(greeting + ", " + name + "!")

#code3
A = str(input())
print(A)

#code4
a = float(input())
print(a * a)

#code5
celsius = float(input())
fahren = (celsius * 9/5) + 32
print(fahren)

#code6
x = int(input())
y = float(input())
z = int(input())
print(x + y + z)
product = x * y * z
print(f"{product:.2f}")

#code7
import sys

def solve():
    data = sys.stdin.read().strip()
    
    if data == "True" or data == "False":
        print("Boolean")
        
    elif data.isdigit():
        print("Integer")
        
    elif data.count('.') == 1:
        parts = data.split('.')
        if (parts[0].isdigit() or parts[0] == "") and (parts[1].isdigit() or parts[1] == ""):
            if data != ".":
                print("Float")
            else:
                print("String")
        else:
            print("String")
            
    else:
        print("String")

if __name__ == "__main__":
    solve()

#code8 
folder_name = input()
subfolder_name = input()
file_base_name = input()
drive_number = int(input())
file_extension = input()
separator_type = input()

full_file_name = file_base_name + file_extension
forward_sep = "/"
backward_sep = "\\\\"

drive3 = 'D'
drive4 = 'F'
drive5 = 'H'
drive6 = 'J'
drive7 = 'L'
drive8 = 'N'
drive9 = 'P'
drive10 = 'R'

drive_letter = (drive_number == 3) * drive3 + (drive_number == 4) * drive4 + (drive_number == 5) * drive5 + (drive_number == 6) * drive6 + (drive_number == 7) * drive7 + (drive_number == 8) * drive8 + (drive_number == 9) * drive9 + (drive_number == 10) * drive10

linux_path = forward_sep + folder_name + forward_sep + subfolder_name + forward_sep + full_file_name
windows_path = drive_letter + ":\\\\" + folder_name + "\\\\" + subfolder_name + "\\\\" + full_file_name

final_path = (separator_type == "forward") * linux_path + (separator_type == "backward") * windows_path
print(final_path)
```

---

## 2. Type-Casting

```python
#code1
principal = int(input())
rate = int(input())
time = int(input())

simple_intereast = (principal * rate * time) / 100

print(simple_intereast)

#code2
n = int(input())

result = (n * (n + 1) // 2) **2

print(result)

#code3
n = int(input())

print(float(n))

#code4
n = input()

total = 0

for c in n:
  total += int(c)
  
print(total)

#code5
n = input().strip('"')

print(int(n))

#code6
str_int = input()
f_num = float(input())
str_float = input()

value1 = float(str_int)
value2 = float(f_num)
value3 = float(str_float)

largest = max(value1, value2, value3)

print(f"{largest:.2f}")

#code7
data = input().split()

a = int(data[0])
b = int(data[1])

result1 = a // b 

result2 = float(a) / float(b)

print(result1)
print(f"{result2:.2f}")

#code8 
data = input().split()

val1_str = data[0].strip('"')
val2_float = data[1].strip('"')
val3_int = data[2].strip('"')

converting_float = float(val1_str)

converting_integer = int(float(val2_float))

converting_string = str(val3_int)

print(converting_float)
print(converting_integer)
print(f'"{converting_string}"')

```

---

## 3. Operators

```python
n = int(input())
m = float(input())
t = str(input())

print(n)
print(m)
print(t)

#2
a = int(input())
b = int(input())

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#3
a = int(input())
b = int(input())

print(a == b)

#4
a_int = int(input())
b_int = int(input())

a = bool(a_int)
b = bool(b_int)

print(a and b)
print(a or b)
print(not a)
print(not b)

#5
expre = input()

result = eval(expre)

print(float(result))

#6
a = input().strip()
b = input().strip()

user = (a == "True")
pass_ = (b == "True")

both_correct = user and pass_

any_one_incorrect = (not user) or (not pass_)

print(both_correct)
print(any_one_incorrect)


```

---
