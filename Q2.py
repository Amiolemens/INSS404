import random

def sort_numbers(number):
    numbers.sort()
    return numbers

numbers = [random.randint(1, 100) for _ in range(100)]
sorted_numbers = sorted(numbers)
print(sorted_numbers)