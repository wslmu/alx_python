for i in range(10):
    for j in range(i + 1, 10):
        if i != j and i * 10 + j < 89:
            print("{:02d}, ".format(i * 10 + j), end="")
print("89")