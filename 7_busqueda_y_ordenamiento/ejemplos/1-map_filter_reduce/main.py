# lambda o funciones anonimas
print('--- lambda ---')
add = lambda x, y: x + y
print(add(3, 5))

# Lista dummy
items = [1, 2, 3, 4, 5, 6]

# map
print('--- map ---')
def multiplay_elements_by_two(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

#result = multiplay_elements_by_two(items)
result = list(map(lambda x: x*2, items))
print(result)

# filter
print('--- filter ---')
def get_low_than_three(numbers):
    result = []
    for number in numbers:
        if number < 3:
            result.append(number)
    return result

#result = get_low_than_three(items)
result = list(filter(lambda x: x < 3, items))
print(result)

# reduce
print('--- reduce ---')
def get_average(numbers):
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)
#average = get_average(item)

from functools import reduce
average = reduce((lambda x, y: x * y), items) / len(items)
print(average)
