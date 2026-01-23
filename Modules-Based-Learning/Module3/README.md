<img src="Bytexl.svg" width="140" align="left"/>

<br clear="left"/>

# Introduction to Data Structures

## Python Learning Journey


<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=2000&color=00D4FF&center=true&width=900&lines=%F0%9F%93%8B+Plan+%F0%9F%8F%97%EF%B8%8F+Build+%F0%9F%9A%80+Deploy+%F0%9F%92%8E+Bytexl" />


## Overview

This module provides a comprehensive introduction to fundamental data structures in Python. Data structures are essential building blocks of programming that allow you to organize, store, and manipulate data efficiently. Understanding different data structures and their properties is crucial for writing optimized and scalable code.

### What You Will Learn:

- **Lists**: Ordered, mutable collections that can store multiple items
- **Tuples**: Immutable sequences ideal for fixed collections and dictionary keys
- **Sets**: Unordered collections of unique elements, perfect for membership testing
- **Dictionaries**: Key-value mappings for fast data retrieval and organization
- **Strings**: Immutable sequences of characters for text data
- **Nested Structures**: Combining data structures for complex data representation

### Key Concepts:

1. **Mutability**: Whether data can be changed after creation
2. **Ordering**: Whether elements maintain insertion order
3. **Uniqueness**: Whether duplicate elements are allowed
4. **Performance**: Time complexity for common operations
5. **Use Cases**: When and where to use each structure

---



## 1. Lists (Ordered & Mutable)



### Code 1: List Operations

```python
#Code1) 
n = input()

num_ = [int(x) for x in n.split()]

largest = max(num_)

print(largest)

#2
n = input().split()
index = int(input())

result = n[index]

print(result)

#3
n = input().split()

start, end = map(int, input().split())

sublist = n[start:end]

print(*(sublist))

#4
n = int(input())

mylist = []

for i in range(n):
  item = input()
  mylist.append(item)
  
removeelement = input()

if removeelement in mylist:
  mylist.remove(removeelement)


mylist.sort()
mylist.reverse()

print(mylist)

#5
n = list(map(int, input().split()))

m = int(input())
newvalue= int(input())

n[m] = newvalue

print(*(n))

#6
temp = list(map(int, input().split()))

anomalies = []

for i in range(1, len(temp)):
  if temp[i - 1] - temp[i] >= 5:
    anomalies.append(temp[i])

print(anomalies)

#7
prices = list(map(int, input().split()))

peaks = []

for i in range(1, len(prices) - 1):
  if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
    peaks.append(i)

print(peaks)

#8 
import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n_orig = int(data[0])
raw = [int(x) for x in data[1:]]

cleaned = []
if raw:
    cleaned.append(raw[0])
    for i in range(1, len(raw)):
        if raw[i] != raw[i-1]:
            cleaned.append(raw[i])

extracted = []
orig_indices = []
for i in range(2, len(cleaned)):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        extracted.append(cleaned[i])
        orig_indices.append(i)

final_list = []
for k in range(len(extracted)):
    val = extracted[k]
    if val < 0:
        pos = orig_indices[k]
        ln = 0
        for l in range(pos - 1, -1, -1):
            if cleaned[l] >= 0:
                ln = cleaned[l]
                break
        rn = 0
        for r in range(pos + 1, len(cleaned)):
            if cleaned[r] >= 0:
                rn = cleaned[r]
                break
        final_list.append((ln + rn) // 2)
    else:
        final_list.append(val)

for m in range(len(final_list)):
    if m % 2 == 0:
        final_list[m] *= n_orig

final_list.reverse()

if len(final_list) > 1 and final_list[0] == final_list[-1]:
    print(final_list)
else:
    print("Corrupted Signal")

```

## 2. Tuples (Ordered & Immutable)



### Code2: Tuple Operations

```python
#Code1)
values = input().split()
result = tuple(values)
print(result)

#Code2) 
t = tuple(input().split())
index = int(input())

print(t[index])



#Code3) 
t1 = tuple(input().split())
t2 = tuple(input().split())

result = t1 + t2
print(result)



#Code4) 
t = tuple(input().split())
start = int(input())
stop = int(input())

print(t[start:stop])


#Code5) 
t = tuple(map(int, input().split()))
x = int(input())

lst = list(t)
lst.append(x)
t = tuple(lst)

print(t)


#Code6) 
times = tuple(map(int, input().split()))

result = []
for t in times:
    if 9 <= t <= 17:
        result.append(t)

print(tuple(result))



#Code7) 
temps = tuple(map(int, input().split()))
result = []

for i in range(len(temps) - 2):
    if temps[i] > 35 and temps[i + 1] > 35 and temps[i + 2] > 35:
        result.append((temps[i], temps[i + 1], temps[i + 2]))

print(tuple(result))



#Code8) 
n = int(input())
t = tuple(map(int, input().split()))

prime_elements = []
for i in range(2, len(t)):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_elements.append(t[i])
prime_tuple = tuple(prime_elements)

unique_elements = []
for x in prime_tuple:
    if x not in unique_elements:
        unique_elements.append(x)
unique_tuple = tuple(unique_elements)

sum_unique = sum(unique_tuple)
sliced_tuple = t[0::3]
sum_sliced = sum(sliced_tuple)

if sum_unique > sum_sliced:
    print("Pattern Matched")
else:
    print("Pattern Mismatch")

```

## 3. Sets (Unordered & Unique)



### Code3: Set Operations

```python
#Code1) 
items = input().split()
unique_items = list(dict.fromkeys(items))
print("{" + ", ".join(unique_items) + "}")


#Code2) 
set1 = set(input().split())
set2 = set(input().split())

union_set = sorted(set1 | set2)
intersection_set = sorted(set1 & set2)
difference_set = sorted(set1 - set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)


#Code3)  
nums = set(map(int, input().split()))
print(min(nums))
print(max(nums))


#Code4) 
words = set(input().split())
vowels = set("aeiouAEIOU")

count = 0
for word in words:
    for ch in word:
        if ch in vowels:
            count += 1

print(count)


#Code5) 
s = list(map(int, input().split()))
x = int(input())

if x in s:
    s.remove(x)

s = sorted(s)
print("{" + ", ".join(map(str, s)) + "}")


#Code6) 
total = set(input().split())
assigned = set(input().split())
new_req = set(input().split())

available = total - assigned
assigned |= (new_req & available)

print(sorted(assigned))


#Code7) 
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    
    lines = [line.strip() for line in input_data if line.strip()]
    
    if not lines:
        return

    emails = lines[0].split()
    
    blocked_domains = set()
    for i in range(1, len(lines)):
        parts = lines[i].split()
        for p in parts:
            blocked_domains.add(p)

    filtered_emails = set()

    for email in emails:
        if '@' in email:
            parts = email.rsplit('@', 1)
            domain = parts[1]
            if domain not in blocked_domains:
                filtered_emails.add(email)

    print(filtered_emails)

if __name__ == "__main__":
    solve()


#Code8) 
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    master_catalog = {} 
    available_books = {} 
    for _ in range(n):
        isbn = input_data[ptr]
        genre = input_data[ptr+1]
        master_catalog[isbn] = genre
        available_books[isbn] = genre
        ptr += 2
        
    borrowed_books = {}  
    borrowed_genres_history = {} 
    m = int(input_data[ptr])
    ptr += 1
    for _ in range(m):
        status = input_data[ptr]
        isbn = input_data[ptr+1]
        ptr += 2
        if status not in borrowed_books:
            borrowed_books[status] = set()
            borrowed_genres_history[status] = set()
            
        if isbn in available_books:
            print(f"Book {isbn} borrowed.")
            genre = available_books[isbn]
            borrowed_books[status].add(isbn)
            borrowed_genres_history[status].add(genre)
            del available_books[isbn]
        else:
            print(f"Book {isbn} not available.")
    k_count = int(input_data[ptr])
    ptr += 1
    for _ in range(k_count):
        op = input_data[ptr].lower()
        ptr += 1
        
        if op == "borrow":
            status = input_data[ptr]
            isbn = input_data[ptr+1]
            ptr += 2
            
            if status not in borrowed_books:
                borrowed_books[status] = set()
                borrowed_genres_history[status] = set()
            
            requested_genre = master_catalog.get(isbn)
            has_genre = any(master_catalog[b_isbn] == requested_genre for b_isbn in borrowed_books[status])
            
            if has_genre:
                print(f"Student already has a book from genre {requested_genre}.")
            elif isbn in available_books:
                print(f"Book {isbn} borrowed.")
                borrowed_books[status].add(isbn)
                borrowed_genres_history[status].add(requested_genre)
                del available_books[isbn]
            else:
                print(f"Book {isbn} not available.")
                
        elif op == "return":
            status = input_data[ptr]
            isbn = input_data[ptr+1]
            ptr += 2
            print(f"Book {isbn} not found in borrowed list.")
                
        elif op == "suggest":
            status = input_data[ptr]
            ptr += 1
            suggested = []
            if status in borrowed_genres_history:
                history = borrowed_genres_history[status]
                for lib_isbn in sorted(available_books.keys()):
                    if available_books[lib_isbn] in history:
                        suggested.append(lib_isbn)
            
            if not suggested:
                print(f"Suggested books for {status}: set()")
            else:
                formatted = "{" + ", ".join(f"'{x}'" for x in sorted(suggested)) + "}"
                print(f"Suggested books for {status}: {formatted}")

if __name__ == "__main__":
    solve()

```

## 4. Dictionaries (Key-Value Pairs)



### Code4: Dictionary Operations

```python
#Code1) 
keys = input().split()
values = input().split()

d = dict(zip(keys, values))
print(d)


#Code2) 
n = int(input())
d = {}
for _ in range(n):
    key = input()
    value = input()
    d[key] = value

print(d.get('computers', "Key 'computers' not found"))


#Code3) 
n = int(input())
original = {}
for _ in range(n):
    key = input()
    value = input()
    original[key] = value

extract_keys = input().split()
new_dict = {k: original[k] for k in extract_keys if k in original}

print(new_dict)


#Code4) 
n = int(input())
d = {}
for _ in range(n):
    key = input()
    value = input()
    d[key] = value

get_key = input()
print(d.get(get_key, "Key not found"))

update_key = input()
update_value = input()
d.update({update_key: update_value})

pop_key = input()
d.pop(pop_key, None)

d_copy = d.copy()
print(d_copy)

d.clear()
print(d)


#Code5) 
n = int(input())
d = {}

for _ in range(n):
    key = input()
    value = input()
    d[key] = value

for k, v in d.items():
    print(f"The value for {k} is {v}")


#Code6) 
records = input().split()
sales = {}

for record in records:
    title, count = record.split(":")
    count = int(count)
    sales[title] = sales.get(title, 0) + count

print(sales)


#Code7) 
names = input().split()
scores = list(map(int, input().split()))

result = {}
for name, score in zip(names, scores):
    if score >= 50:
        result[name] = score

print(result)


#Code8) 
n = int(input())
D = {}

for _ in range(n):
    k, v = input().split()
    D[k] = int(v)

for k, v in list(D.items()):
    if len(k) % 2 != 0 or v <= 0:
        D.pop(k)

vowels = "aeiou"
for k, v in list(D.items()):
    rev = k[::-1]
    new_key = ""
    for ch in rev:
        if ch in vowels:
            new_key += ch.upper()
        else:
            new_key += ch
    if v % 2 == 0:
        new_val = bin(v)[2:]
    else:
        new_val = oct(v)[2:]
    D.pop(k)
    D[new_key] = new_val

keys = sorted(D.keys())
print(keys[0] + keys[-1])

```

## 5. List Comprehensions



### Code5: Comprehensions
```python
#Code1)  
nums = list(map(int, input().split()))
evens = [x for x in nums if x % 2 == 0]
print(evens)


#Code2) 
n = int(input())
print(sum(i*i for i in range(1, n + 1)))


#Code3) 
d = eval(input())
inverted = {v: k for k, v in d.items()}
print(inverted)


#Code4) 
nested = eval(input())
flat = [item for sublist in nested for item in sublist]
print(flat)


#Code5) 
n = int(input())
result = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1)]
print(result)


#Code6) 
names = input().split()
prices = list(map(float, input().split()))
discounted = {names[i]: round(prices[i] * 0.9, 2) for i in range(len(names)) if prices[i] > 1000}
print(discounted)


#Code7) 
nums = list(map(int, input().split()))
result = [n*n for n in nums if n % 2 == 0 and str(n*n) == str(n*n)[::-1]]
print(result)


#Code8) 
n = int(input())
nums = list(map(int, input().split()))

def digit_sum_even(x):
    return sum(map(int, str(abs(x)))) % 2 == 0

result = []
mapping = {}

for x in nums:
    if x % 3 == 0 or digit_sum_even(x):
        if x % 2 == 0:
            t = x * x
        else:
            t = x * x * x
        mapping[x] = t

for v in mapping.values():
    if v >= 0 and int(v ** 0.5) ** 2 == v:
        result.append(v)

print(*result)

```

## 6. Strings



### Code Block 6: Working with Strings

```python
#Code1) 
s = input()
print(len(s))


#Code2) 
s1 = input()
s2 = input()
s = s1 + s2
print(s)
print(s[:5])


#Code3) 
s = input()
print(s[::-1])


#Code4) 
s = input()
w = int(input())
try:
    fill = input()
    if fill == "":
        fill = "#"
except:
    fill = "#"

print(s.center(w, fill))


#Code5) 
a = input()
b = input()
s = input()
table = str.maketrans(a, b)
print(s.translate(table))



#Code6) 
emails = input().split()
cleaned = [e.strip().lower() for e in emails]
sorted_emails = sorted(cleaned, key=lambda x: x.split('@')[1])
print(sorted_emails)


#Code7) 
s = input().lower()
for ch in ".,!?;:":
    s = s.replace(ch, "")
words = s.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

for w, c in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
    print(f"{w}:{c}")


#Code8) 
s = input()

letters = []
digits = []

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            letters.append(ch.upper())
        else:
            letters.append(ch.lower())
    else:
        digits.append(ch)

digits = [str(9 - int(d)) for d in digits[::-1]]

i = j = 0
res = []

while i < len(letters) and j < len(digits):
    res.append(letters[i])
    res.append(digits[j])
    i += 1
    j += 1

res.extend(letters[i:])
res.extend(digits[j:])

print("".join(res))

```

---

## Summary

| Data Structure | Ordered | Mutable | Unique | Use Case |
|---|---|---|---|---|
| List | Yes | Yes | No | Variable-length sequences |
| Tuple | Yes | No | No | Fixed collections, dict keys |
| Set | No | Yes | Yes | Unique elements, membership testing |
| Dictionary | No (Python 3.7+: Yes) | Yes | Keys only | Key-value mappings |
| String | Yes | No | No | Text data |

## Learning Resources

- Official Python Docs: https://docs.python.org/3/tutorial/datastructures.html
- - Write and test practical examples for each data structure
- Experiment with different operations and methods
- Implement nested structures for real-world scenarios
