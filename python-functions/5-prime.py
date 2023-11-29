def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
test_number = 17
result = is_prime(test_number)
print(f"{test_number} is prime: {result}")
