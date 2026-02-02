# Анализатор данных

def filter_even(numbers):
    """
    Возвращает только четные числа
    
    Аргументы:
        numbers - список чисел(список)
    
    Возвращает:
        list()
    """
    
    result = [num for num in numbers if num % 2 == 0]
    return result

def filter_odd(numbers):
    """
    Возвращает только нечетные числа
    
    Аргументы:
        numbers - список чисел(список)
    
    Возвращает:
        list()
    """
    
    result = [num for num in numbers if num % 2 != 0]
    return result

def is_even(num): # True - если число простое, False - если составное
    i = 2
    if num == 1:
        return False
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def filter_prime(numbers):
    """
    Возвращает только простые числа. 
    
    Аргументы:
        numbers - список чисел(список)
    
    Возвращаент:
        list()
    """
    
    result = []
    for num in numbers:
        if is_even(num):
            result.append(num)
    return result

def filter_by_range(numbers, start, end):
    result = []
    
    for num in numbers:
        if start <= num <= end:
            result.append(num)
    
    return result

def filter_by_condition(numbers, condition_func):
    result = []
    
    for num in numbers:
        if condition_func(num):
            result.append(num)
    
    return result

def calculate_statistics(numbers):
    sum_numbers = sum(numbers)
    avg = sum_numbers / len(numbers)
    unique_count = 0
    
    for num in numbers:
        if numbers.count(num) == 1:
            unique_count = num
    
    print('max: ', max(numbers))
    print('min: ', min(numbers))
    print('average: ', avg)
    print('sum: ', sum_numbers)
    print('unique count: ', unique_count)

    
numbers = [12, 7, 23, 4, 19, 8, 11, 15]

print("Четные:", filter_even(numbers))
print("Простые:", filter_prime(numbers))
print("В диапазоне 10-20:", filter_by_range(numbers, 10, 20))
print('Больше 16: ', filter_by_condition(numbers, lambda x: x > 16))