x = 11
y = 2

result = x / y

print(int(result))

result = -result

print(result)
print(abs(result))

result = divmod(x, y)
print(result, type(result))

print(y ** 4)
print(pow(y, 4))