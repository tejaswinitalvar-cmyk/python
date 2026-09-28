# Find the largest prime number in a list using python programming language

numbers = [10, 7, 23, 15, 31, 20]

largest_prime = None

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            if largest_prime is None or num > largest_prime:
                largest_prime = num

print("Largest prime number =", largest_prime)
