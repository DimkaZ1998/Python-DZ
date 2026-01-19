import random
import  time

# ШАГ 1. Создадим фукнцию-генератор подсказок
def generate_hint(secret, guess):
    """
    Генерирует подсказку в зависимости от модуля разности 
    между секректным числом и числом, которое ввел пользователь
    """
    if abs(secret - guess) <= 5:
        return 'Горячо!'
    elif abs(secret - guess) <= 15:
        return 'Тепло!'
    else:
        return 'Холодно'

# ШАГ 2. Создадим подсчёт очков, бонус за быструю победу
def calculate_score(score, isWon, time=0):
    """
    1. Снимает очки за каждую попытку
    2. Проверяет, чтобы максимум было 100 очков
    3. Начисляет доп. очки за быструю победу
    """
    score -= 10 # Снимаем очки за попытку
    
    bonus_score = 20
    if isWon and time < 41: # Если пользователь победил меньше чем за 40 секунд - начисляем дополнительные очки
        if score + bonus_score > 100: # Не должно быть больше 100 очков
            score = 100
            print(f'Бонус за быструю победу - {bonus_score} очков! Время победы: {time} сек.')
        else:
            score += bonus_score
            print(f'Бонус за быструю победу - {bonus_score} очков! Время победы: {time} сек.')
    
    
    return score # Вернем очки

# ШАГ 3. Основная логика игры
def play_game(score):
    """
    Описывает основную логику игры, цикл while, в котором это все происходит.
    Аргумет score нужен, чтобы изменить существующие очки а потом вернуть их
    """
    
    SECRET = 60 # Секретное число от 1 до 100
    start_time = time.time() # Время, когда пользователь начал игру
    attempts = {} # Словарь попыток, где ключ - уникальный id попытки(ее порядковый номер), ключ - содержание попытки(угадал/не угадал)
    quantity_attempts = 0 # Количество попыток
    attempts['secret number'] = SECRET # Добавим секретное число в описание игры
    
    while True:  
        if score <= 0:
            end_time = time.time() # Время, когда у пользователя закончились очки
            attempt_time = round(abs(start_time - end_time), 3) # Время в секундах, за которое у пользователя закончились очки
            print('Кажется, ваши очки закончились (\nДо встречи!')
            
            # Добавим время поражения
            attempts['Time of lose'] = attempt_time
            
            return (attempts, 0)
        try: 
            guess = int(input('Введите число: ')) 
        except ValueError: # Если пользователь ввёл не число
            print()
            print('Ввод должен быть числом!')
            print()
            continue
        
        if guess <= 0: # Если ввод неположительный
            print('Число должно быть положительным!')
            print()
            continue
        
        quantity_attempts += 1 # Увеличим кол-во попыток
        
        if guess == SECRET:
            end_time = time.time() # Время, когда пользователь отгадал число
            attempt_time = round(abs(start_time - end_time), 3) # Время в секундах, за которое пользователь угадал число
            
            score = calculate_score(score, True, attempt_time)
            print()
            
            # Добавим попытку в список
            attempts[f'Попытка {quantity_attempts}'] = {
                'id' : quantity_attempts,
                'result' : True,
                'input number' : guess,
            }
            
            # Добавим время победы
            attempts['Time of victory'] = attempt_time
            
            break
        else:
            hint = generate_hint(SECRET, guess)
            print(hint)
            score = calculate_score(score, False)
            print()
            # Добавим попытку в список
            attempts[f'Попытка {quantity_attempts}'] = {
                'id' : quantity_attempts,
                'result' : False,
                'input number' : guess
            }
    
    return (attempts, score) # Возвращаем список попыток (Результат игры), Очки просле игры

# ШАГ 4. Покажем статистику игр
def show_statistics(plays_dict):
    print()
    if not plays_dict: # Если игр еще не было
        print('Вы еще ни разу не сыграли(')
        print()
        return
    for play_id, attempts_dict in plays_dict.items():
        if play_id == 'Quantity of games': # Выведем количество игр
            print(f'{play_id} : {attempts_dict}')
            continue
        if play_id == 'Best result': # Выведем лучший результат, если он есть
            print(f'{play_id} : {attempts_dict}')
            continue
        print(play_id, ':')
        for attempt_id, attempt_info in attempts_dict.items():
            if attempt_id == 'Time of victory' or attempt_id == 'Time of lose': # Последний элемент списка попыток
                print(f'    {attempt_id} : {attempt_info}')
                print()
                continue
            elif attempt_id == 'secret number': # Секретное число:
                print(f'    {attempt_id} : {attempt_info}')
                print()
                continue
            print(f'    {attempt_id}: ')
            print()
            for key, info in attempt_info.items():
                print(f'\t{key}: {info}')
            
            print()
        print()

# Меню пользователя
menu = f"""
{'=' * 40}
Меню :
1. Начать новую игру
2. Показать статистику игр
3. Завершить сеанс
{'=' * 40}
"""
score = 100

plays_dict = {} # Список игр, где ключ - уникальный id игры, значение - словарь с попытками, полученный из game_play()
best_result = False # Лучший результат по времени, при первой инициализации его нету
plays_dict['Quantity of games'] = 0 # Количество игр
plays_quantity = 0

# TODO:
# 1. Добавить в статистику игр самый быстрый результат
print()
print()
while True:
    print(menu)
    
    try:
        change = int(input('Ваш выбор (1-4): '))
    except ValueError: # Если пользователь ввёл не число
        print('Ввод должен быть числом!')
        continue
    
    if change <= 0: # Если число неположительное
        print('Ввод должен быть положительным!')
        continue
    elif change not in range(1, 5): # Если вариант выбран неверно
        print('Вводите правильный вариант!')
        continue
    
    if change == 1:
        game, score = play_game(score) # Распакуем кортеж, который вернул play_game и получим информацию об игре и обновленные очки
        if game.get('Time of victory'): # Если игрок выиграл
            if game['Time of victory'] < best_result or not best_result: # Сравним время его победы с имеющимся лучшим результатом. Если лучшего результата еще нет - присвоим время первой победы
                best_result = game['Time of victory']
                plays_dict['Best result'] = best_result
        plays_quantity += 1
        plays_dict['Quantity of games'] = plays_quantity # Увеличим количество игр
        
        plays_dict[f'Игра {plays_quantity}'] = game 
    elif change == 2:
        show_statistics(plays_dict)
    elif change == 3:
        print()
        print('=' * 40)
        print('Сеанс завершен')
        print('=' * 40)
        print('СТАТИСТИКА ИГР')
        show_statistics(plays_dict)
        break