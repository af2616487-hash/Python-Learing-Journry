# ========== TYPE CASTING IN PYTHON ==========
# This file contains consolidated examples of type casting and conversions

# ========== PROBLEM 01: Simple Interest Calculation ==========
principal = int(input())
rate = int(input())
time = int(input())
simple_interest = (principal * rate * time) / 100
print(simple_interest)

# ========== PROBLEM 02: Square of Sum ==========
n = int(input())
result = (n * (n + 1) // 2) ** 2
print(result)

# ========== PROBLEM 03: Integer to Float Conversion ==========
n = int(input())
print(float(n))

# ========== PROBLEM 04: Sum of Digits ==========
n = input()
total = 0
for c in n:
    total += int(c)
print(total)

# ========== PROBLEM 05: String to Integer Conversion ==========
n = input().strip('"')
print(int(n))

# ========== PROBLEM 06: Largest of Three Numbers ==========
str_int = input()
f_num = float(input())
str_float = input()
value1 = float(str_int)
value2 = float(f_num)
value3 = float(str_float)
largest = max(value1, value2, value3)
print(f"{largest:.2f}")

# ========== PROBLEM 07: Integer and Float Division ==========
data = input().split()
a = int(data[0])
b = int(data[1])
result1 = a // b
result2 = float(a) / float(b)
print(result1)
print(f"{result2:.2f}")

# ========== PROBLEM 08: Type Conversions ==========
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
