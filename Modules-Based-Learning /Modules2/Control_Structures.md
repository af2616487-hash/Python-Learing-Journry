# Control Structures in Python

## Overview

Master conditional statements, loops, and decision-making in Python. Learn how to use if-elif-else statements, while and for loops, loop control statements (break, continue), and apply these concepts to solve practical problems involving iterations and conditions.

**Topics:** If-Elif-Else statements | For loops | While loops | Break & Continue | Nested structures | Loop patterns

**Learn to:** Write conditional logic | Use different loop types | Control loop flow | Create nested structures | Solve iteration problems

## Table of Contents

1. [If-Elif-Else Statements](#1-if-elif-else-statements)
2. [For Loops](#2-for-loops)
3. [While Loops](#3-while-loops)
4. [Break and Continue](#4-break-and-continue)
5. [Nested Loops](#5-nested-loops)
26
Statements

**Concept:** Conditional statements allow you to execute different code blocks based on different conditions. If-elif-else statements provide multiple condition branches.

```python
#Code1)
nums = list(map(int, input().split()))
target = int(input())

found = False

for i in range(len(nums)):
    if nums[i] == target:
        print(f"Number found at index {i}")
        found = True
        break

if not found:
    print("Number not found")

#Code2) 
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i, end=" ")

#Code3)
n = int(input())
m = int(input())

for i in range(n, m + 1):
    if i == 3:
        print("Skip 3!")
        pass
    else:
        print(i)

#Code4)
n, m = map(int, input().split())

for i in range(n, m + 1):
    if i == 3:
        print("Skipping number 3!")
        pass
    else:
        print(i)

#Code5) 
n = int(input())

result = []

for i in range(1, n + 1):
    if i > 10:
        break
    if i % 2 == 0:
        continue
    result.append(str(i))

print(" ".join(result))

#Code6) 
n = int(input())

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    total += i

print(total)

#Code7) 
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n <= 0:
        pass
    else:
        count += 1

print(count)


#Code8) 
n, k = map(int, input().split())
commands = [input().strip() for _ in range(n)]

escaped = False
i = 0

while i < n:
    cmd = commands[i]

    if cmd == "MOVE":
        i += 1
        continue

    elif cmd == "JUMP":
        i += k + 1
        continue

    elif cmd == "IGNORE":
        pass

    elif cmd == "BLOCK":
        break

    elif cmd == "END":
        escaped = True
        break

    i += 1

if escaped:
    print("ESCAPED")
else:
    print("TRAPPED")

```

## 2. For Loops

**Concept:** For loops are used to iterate over sequences (like lists, strings, ranges). They execute a block of code a specific number of times.

```python
#Code1
n = int(input())

for i in range(2, n + 1, 2):
  print(i)
  
#Code2
n = int(input())
m = int(input())

for i in range(m):
  print(n)

#Code3
n = int(input())

for i in range(n):
  print(i + 1)

#Code4
n = int(input())

for i in range(1, n + 1, 2):
  print(i)

#Code6
n = int(input())
total_sum = 0

for i in range(1, n + 1):
  total_sum += i * i
  
print(total_sum)

#Code7
n = int(input())

numbers = list(map(int, input().split()))


reversed_number = []

for i in range(n - 1, -1, -1):
  reversed_number.append(str(numbers[i]))
  
print(" ".join(reversed_number))

#Code8 
n = int(input())
temp = n 
prime_power_sum = 0
d = 2

while d * d <= temp:
  if temp % d == 0:
    current_factor_value = 1 
    while temp % d == 0:
      current_factor_value *= d 
      temp //= d 
    prime_power_sum += current_factor_value
  d += 1 
  
if temp > 1:
  prime_power_sum += temp
  
print(prime_power_sum)


```

## 3. While Loops

**Concept:** While loops repeat as long as a condition is true. They are useful when you don't know how many times you need to iterate.

```python
#Code1
n = int(input())
i = 0

while n >= 1:
  print(n, end=" ")
  n = n - 1


#Code2
n = int(input())
i = 1

while i <= n:
  print(i)
  i = i + 1

#Code3
n = int(input())
i = 1

while i <= n:
  print("Hello")
  i = i + 1

#Code4
n = int(input())
i = 2

while i <= n:
  print(i)
  i = i + 2

#Code5
n = int(input())

totalsum = 0
i = 1 

while i <= n:
  totalsum = totalsum + i 
  i =  i + 1 
  
print(totalsum)

#Code6
n = int(input())

if n < 1:
  print("Error: Factorial is not defined for negative numbers")
else:
  Factorial = 1 
  i = n 
  
  while i >= 1:
    Factorial = Factorial * i 
    i = i - 1 

print(Factorial)

#Code7
n = int(input())

if n < 0:
  print("Error: Sum of digits is not defined for negative numbers.")
else:
  digitsum = 0
  
  while n > 0:
    digit = n % 10
    digitsum += digit
    n = n // 10

print(digitsum)

#Code8 
n = int(input())

factor = 2

while factor * factor <= n:
  if n % factor == 0:
    n //= factor
  else:
    factor += 1 

print(n)


```

## 4. Nested Loops

**Concept:** Nested loops are loops inside loops. They are useful for working with multidimensional data structures or creating patterns.

```python
#Code1)
n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        print(f"Outer: {i}, Inner: {j}")

#Code2)
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Code3)
rows = int(input())
cols = int(input())

for i in range(rows):
    for j in range(1, cols + 1):
        print(j, end=" ")
    print()

#Code4)
n, m = map(int, input().split())

for i in range(n):
    print("*" * m)

#Code5)
n = int(input())

for i in range(n):
    print("*" * n)

#Code6)
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()
#Code7)
n = int(input())

grid = [[i * n + j + 1 for j in range(n)] for i in range(n)]

total_sum = 0

for d in range(2 * n - 1):
    elements = []
    for i in range(n):
        j = d - i
        if 0 <= j < n:
            elements.append(grid[i][j])
    if d % 2 == 0:
        elements.reverse()
    for val in elements:
        total_sum += val

print(total_sum)

#Code8)
n = int(input())
matrix = []

i = 0
while i < n:
    matrix.append(list(map(int, input().split())))
    i += 1

top = 0
bottom = n - 1
left = 0
right = n - 1

result = []

while top <= bottom and left <= right:
    j = left
    while j <= right:
        result.append(matrix[top][j])
        j += 1
    top += 1

    i = top
    while i <= bottom:
        result.append(matrix[i][right])
        i += 1
    right -= 1

    if top <= bottom:
        j = right
        while j >= left:
            result.append(matrix[bottom][j])
            j -= 1
        bottom -= 1

    if left <= right:
        i = bottom
        while i >= top:
            result.append(matrix[i][left])
            i -= 1
        left += 1

k = 0
while k < len(result):
    print(result[k], end=" ")
    k += 1


```

## 5. Control Statements: break, continue, pass

**Concept:** Common loop patterns include summing, counting, searching, and filtering. Understanding these patterns helps solve many problems efficiently.

```python
#Code1)
nums = list(map(int, input().split()))
target = int(input())

found = False

for i in range(len(nums)):
    if nums[i] == target:
        print(f"Number found at index {i}")
        found = True
        break

if not found:
    print("Number not found")

#Code2) 
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i, end=" ")

#Code3)
n = int(input())
m = int(input())

for i in range(n, m + 1):
    if i == 3:
        print("Skip 3!")
        pass
    else:
        print(i)

#Code4)
n, m = map(int, input().split())

for i in range(n, m + 1):
    if i == 3:
        print("Skipping number 3!")
        pass
    else:
        print(i)

#Code5) 
n = int(input())

result = []

for i in range(1, n + 1):
    if i > 10:
        break
    if i % 2 == 0:
        continue
    result.append(str(i))

print(" ".join(result))

#Code6) 
n = int(input())

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    total += i

print(total)

#Code7) 
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n <= 0:
        pass
    else:
        count += 1

print(count)


#Code8) 
n, k = map(int, input().split())
commands = [input().strip() for _ in range(n)]

escaped = False
i = 0

while i < n:
    cmd = commands[i]

    if cmd == "MOVE":
        i += 1
        continue

    elif cmd == "JUMP":
        i += k + 1
        continue

    elif cmd == "IGNORE":
        pass

    elif cmd == "BLOCK":
        break

    elif cmd == "END":
        escaped = True
        break

    i += 1

if escaped:
    print("ESCAPED")
else:
    print("TRAPPED")

```

