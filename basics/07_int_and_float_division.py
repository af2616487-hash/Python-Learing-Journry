data = input().split()

a = int(data[0])
b = int(data[1])

result1 = a // b
result2 = float(a) / float(b)

print(result1)
print(f"{result2:.2f}")
