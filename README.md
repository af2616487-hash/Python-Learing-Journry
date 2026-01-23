# 🎯 Pattern Programming Guide

<div align="center">

![Pattern Programming](https://img.shields.io/badge/Pattern-Programming-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-yellow?style=for-the-badge)

**Master the art of pattern programming with comprehensive examples and step-by-step explanations**

[⭐ Star Patterns](#star-patterns) • [🔢 Number Patterns](#number-patterns) • [📚 How It Works](#understanding-patterns)

</div>

---

## 📖 Table of Contents
- [Introduction](#introduction)
- [Understanding Patterns](#understanding-patterns)
- [Star Patterns](#star-patterns)
- [Number Patterns](#number-patterns)
- [Pattern Logic Breakdown](#pattern-logic-breakdown)

---

## 🌟 Introduction

Pattern programming is a fundamental concept in coding that helps develop:Pattern programming develops **logical thinking**, **loop control**, and **problem-solving skills** using nested loops.

---

## 🧠 Understanding Patterns

### Key Concepts

Every pattern follows a systematic approach:

1. **Rows** → Outer loop (controls how many lines)
2. **Columns** → Inner loop (controls elements per line)
3. **Logic** → Relationship between row and column

### Pattern Formula

```
For each row i (from 1 to n):
    For each column j (from 1 to condition):
        Print element based on condition
    Move to next line
```

---

## ⭐ Star Patterns

### 1️⃣ Right Triangle Star Pattern


<table>
<tr>
<td>

**Code:**
```python
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
```

</td>
<td>

**Output:**
```
*
**
***
****
*****
```

</td>
</tr>
</table>


### 2️⃣ Inverted Right Triangle


<table>
<tr>
<td>

**Code:**
```python
n = 5
for i in range(1, n+1):
    for j in range(n-i+1):
        print("*", end="")
    print()
```

</td>
<td>

**Output:**
```
*****
****
***
**
*
```

</td>
</tr>
</table>

---

### 3️⃣ Pyramid Star Pattern


<table>
<tr>
<td>

**Code:**
```python
n = 5
for i in range(1, n+1):
    # Print spaces
    for j in range(n-i):
        print(" ", end="")
    # Print stars
    for j in range(2*i-1):
        print("*", end="")
    print()
```

</td>
<td>

**Output:**
```
    *
   ***
  *****
 *******
*********
```

</td>
</tr>
</table>


### 4️⃣ Diamond Star Pattern

<table>
<tr>
<td>

**Code:**

```python
n = 5

# Upper half (pyramid)
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))

# Lower half (inverted pyramid)
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))
```

</td>
<td>

**Output:**

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

</td>
</tr>
</table>

---

## 🔢 Number Patterns

### 1️⃣ Number Triangle

<table>
<tr>
<td>

**Code:**

```python
n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
```

</td>
<td>

**Output:**

```
1
12
123
1234
12345
```

</td>
</tr>
</table>

### 2️⃣ Floyd's Triangle

<table>
<tr>
<td>

**Code:**

```python
n = 5
num = 1

for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

</td>
<td>

**Output:**

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

</td>
</tr>
</table>


### 3️⃣ Number Pyramid

<table>
<tr>
<td>

**Code:**

```python
n = 5

for i in range(1, n+1):
    # Spaces
    print(" " * (n-i), end="")
    
    # Ascending numbers
    for j in range(1, i+1):
        print(j, end="")
    
    # Descending numbers
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    print()
```

</td>
<td>

**Output:**

```
    1
   121
  12321
 1234321
123454321
```

</td>
</tr>
</table>

### 4️⃣ Pascal's Triangle

<table>
<tr>
<td>

**Code:**

```python
n = 5

for i in range(n):
    # Spaces
    print(" " * (n-i), end="")
    
    # Calculate and print numbers
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    
    print()
```

</td>
<td>

**Output:**

```
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
```

</td>
</tr>
</table>
## 📊 Pattern Logic Breakdown

### Understanding Nested Loops

```python
for i in range(1, n+1):     # Outer loop → Controls ROWS
    for j in range(i):       # Inner loop → Controls COLUMNS
        print("*", end="")   # Print element
    print()                  # Move to next line
```

**Execution Flow:**
1. Outer loop starts: i = 1
2. Inner loop runs: j from 0 to 0 (1 time)
3. Print newline
4. Outer loop continues: i = 2
5. Inner loop runs: j from 0 to 1 (2 times)
6. Repeat...

### Common Pattern Formulas

| Pattern Type | Stars/Numbers Formula | Spaces Formula |
|--------------|----------------------|----------------|
| Right Triangle | `i` | 0 |
| Inverted Triangle | `n - i + 1` | 0 |
| Pyramid | `2 * i - 1` | `n - i` |
| Diamond (upper) | `2 * i - 1` | `n - i` |
| Diamond (lower) | `2 * i - 1` | `n - i` |

---

## 💡 Tips for Pattern Programming

1. **Start with Simple Patterns**: Master right triangle before pyramid
2. **Draw on Paper**: Visualize rows, columns, and spaces
3. **Use Tables**: Create calculation tables to understand loops
4. **Test Small Values**: Start with n=3 or n=4 for easier debugging
5. **Break Down Complex Patterns**: Split into spaces + symbols

---

## 🎯 Practice Exercises

Try these patterns on your own:

### 5️⃣ Square Pattern

<table>
<tr>
<td>

**Code:**
```python
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

</td>
<td>

**Output:**
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

</td>
</tr>
</table>

---

### 6️⃣ Hollow Square Pattern

<table>
<tr>
<td>

**Code:**
```python
n = 5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

</td>
<td>

**Output:**
```
* * * * *
*       *
*       *
*       *
* * * * *
```

</td>
</tr>
</table>

---

### 7️⃣ Hollow Triangle Pattern

<table>
<tr>
<td>

**Code:**
```python
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

</td>
<td>

**Output:**
```
    *
   * *
  *   *
 *     *
*********
```

</td>
</tr>
</table>

---

### 8️⃣ Hourglass Pattern

<table>
<tr>
<td>

**Code:**
```python
n = 5
# Upper inverted
for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))
# Lower pyramid  
for i in range(2, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))
```

</td>
<td>

**Output:**
```
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

</td>
</tr>
</table>

---

### 9️⃣ Butterfly Pattern

<table>
<tr>
<td>

**Code:**
```python
n = 5
# Upper
for i in range(1, n+1):
    print("*" * i, end="")
    print(" " * (2*(n-i)), end="")
    print("*" * i)
# Lower
for i in range(n-1, 0, -1):
    print("*" * i, end="")
    print(" " * (2*(n-i)), end="")
    print("*" * i)
```

</td>
<td>

**Output:**
```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

</td>
</tr>
</table>



## 🤝 Contributing

Feel free to contribute more patterns! Fork this repository and create a pull request.

---

## 📝 License

This project is open source and available for educational purposes.

---

<div align="center">

**Made with ❤️ for aspiring programmers**

⭐ Star this repository if you found it helpful!

[🔝 Back to Top](#-pattern-programming-guide)

</div>
