while True : # Бесконечный цикл, продолжается, пока не будет прерван по логике программы
    number_list = input('Введите несколько чисел через пробел: ')
    try:
        number_list = number_list.split()
        number_list = [int(i) for i in number_list]
    except ValueError:
        print('Ваш ввод должен содержать только числа и пробелы!')
    else:
        print(f'Сумма чисел : {sum(number_list)}')
        print(f'Среднее значение : {sum(number_list) / len(number_list)}')
        print(f'Максимальное значение : {max(number_list)}')
        print(f'Минимальное значение : {min(number_list)}')
        print(f'Количество чётных чисел : {len([i for i in number_list if i % 2 == 0])}') # Внутри скобок создается массив четных чисел из number_list
        print(f'Количество положительных чисел : {len([i for i in number_list if i > 0])}') # Внутри скобок создается массив положительных чисел из number_list
        print(f'Сортированный список по возрастанию : {sorted(number_list)}')
        break
