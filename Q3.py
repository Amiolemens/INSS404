import random
from array import array

numbers = array('i',[random.randint(1, 100) for _ in range(100)])

odd_numbers=array('i',[num for num in numbers if num % 2 !=0])

print(odd_numbers)