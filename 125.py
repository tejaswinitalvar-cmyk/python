# Find the smallest prime number in a list using python programming language

numbers = [10, 17, 5, 23, 11, 8]

smallest_prime = None

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            if smallest_prime is None or num < smallest_prime:
                smallest_prime = num

print("Smallest prime number =", smallest_prime)
