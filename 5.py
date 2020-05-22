from functools import reduce

def custom(first, second):
    return first * second

numbers = [el for el in list(range(100, 1001)) if el % 2 == 0]

result = reduce(custom, numbers)
print(result)
