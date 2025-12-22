# Ввод первого числа
num1 = float(input("Введите первое число: "))

# Ввод второго числа
num2 = float(input("Введите второе число: "))

# Ввод операции
operation = input("Введите операцию (+, -, *, /): ")

# Выполнение вычислений с проверкой ошибок
if operation == '+':
    result = num1 + num2
    print("Результат:", result)
elif operation == '-':
    result = num1 - num2
    print("Результат:", result)
elif operation == '*':
    result = num1 * num2
    print("Результат:", result)
elif operation == '/':
    if num2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        result = num1 / num2
        print("Результат:", result)
else:
    print("Ошибка: неизвестная операция")