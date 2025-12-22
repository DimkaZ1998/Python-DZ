# Выбор направления конвертации
print("Выберите направление конвертации:")
print("1. Цельсий → Фаренгейт")
print("2. Фаренгейт → Цельсий")
choice = input("Введите 1 или 2: ")

# Обработка выбора
if choice == '1':
    temp_input = input("Введите температуру в градусах Цельсия: ")
    try:
        celsius = float(temp_input)
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}°C равно {fahrenheit}°F")
    except ValueError:
        print("Ошибка: введено не число.")
elif choice == '2':
    temp_input = input("Введите температуру в градусах Фаренгейта: ")
    try:
        fahrenheit = float(temp_input)
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F равно {celsius}°C")
    except ValueError:
        print("Ошибка: введено не число.")
else:
    print("Ошибка: неверный выбор. Пожалуйста, введите 1 или 2.")