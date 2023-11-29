def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for _ in range(b):
        result *= a
    return result
result = pow(2, 3)
print(result)  
