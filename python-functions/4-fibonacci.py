def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence
n = 8
fibonacci_numbers = fibonacci_sequence(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")