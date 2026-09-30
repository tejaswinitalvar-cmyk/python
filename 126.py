# Find the sum of numbers at prime positions using python programming language

numbers = [10, 20, 30, 40, 50, 60, 70]

total = 0

for i in range(len(numbers)):
    position = i + 1

    if position > 1:
        is_prime = True

        for j in range(2, position):
            if position % j == 0:
                is_prime = False
                break

        if is_prime:
            total += numbers[i]

print("Sum of numbers at prime positions =", total)
