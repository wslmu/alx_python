def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for _ in range(b):
        result *= a
    return result
print(pow(2, 2))  
