# Find the average of prime numbers in a list using python programming language 

numbers = [10, 7, 13, 20, 17, 25, 19]

prime_numbers = []

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

average = sum(prime_numbers) / len(prime_numbers)

print("Prime numbers:", prime_numbers)
print("Average of prime numbers =", average)
