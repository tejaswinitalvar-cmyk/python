# Find the sum of prime numbers in a list using python programming language 

numbers = [10, 7, 13, 20, 17, 25]

total = 0

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            total += num

print("Sum of prime numbers =", total)
