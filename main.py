# Структура данных для хранения игроков
players = {
    1: {"name": "Алексей", "rating": 1000, "matches": 0},
    2: {"name": "Мария", "rating": 1000, "matches": 0},
    3: {"name": "Дмитрий", "rating": 1000, "matches": 0}
}

# Коэффициент скорости изменения рейтинга
K = 32

# Задача 1: Функция для расчета изменения рейтинга для игрока A
def get_rating_delta(rating_a, rating_b, result):
    """
    Расчет изменения рейтинга по формуле ELO.
    
    :param rating_a: текущий рейтинг игрока A
    :param rating_b: текущий рейтинг игрока B
    :param result: результат матча для игрока A
    1 — победа, 0.5 — ничья, 0 — поражение
    :return: целое число — изменение рейтинга для игрока A
    """
    # Шаг 1: Вычисляем вероятность победы игрока A
    E = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    # Шаг 2: Вычисляем изменение рейтинга
    change = K * (result - E)
    # Шаг 3: Округляем до целого
    return round(change)

# Задача 2: Функция регистрации матча между двумя игроками
def register_match(p1_id, p2_id, winner):
    """
    Обновление рейтингов игроков после матча.
    
    :param p1_id: ID первого игрока
    :param p2_id: ID второго игрока
    :param winner: кто победил:
    1 — победил первый игрок,
    2 — победил второй,
    0 — ничья
    """
    # Проверка существования игроков
    if p1_id not in players or p2_id not in players:
        print("Один из игроков не найден.")
        return
    
    # Получение данных игроков
    player1 = players[p1_id]
    player2 = players[p2_id]
    
    rating1 = player1['rating']
    rating2 = player2['rating']
    
    # Определяем результат для каждого игрока
    if winner == 1:
        result1, result2 = 1, 0
    elif winner == 2:
        result1, result2 = 0, 1
    elif winner == 0:
        result1, result2 = 0.5, 0.5
    else:
        print("Некорректный результат.")
        return
    
    # Расчет изменения рейтинга для каждого игрока
    delta1 = get_rating_delta(rating1, rating2, result1)
    delta2 = get_rating_delta(rating2, rating1, result2)
    
    # Обновляем рейтинги
    players[p1_id]['rating'] += delta1
    players[p2_id]['rating'] += delta2
    
    # Увеличиваем счетчик матчей
    players[p1_id]['matches'] += 1
    players[p2_id]['matches'] += 1
    
    # Выводим результат
    print(f"Рейтинг игрока {player1['name']} изменился на {delta1:+}")
    print(f"Рейтинг игрока {player2['name']} изменился на {delta2:+}")

# Задача 3: Вывод таблицы лидеров
def show_leaderboard():
    """
    Выводит список игроков, отсортированный по рейтингу по убыванию.
    Формат: 1. Имя - рейтинг очков (кол-во матчей)
    """
    # Сортируем игроков по рейтингу
    sorted_players = sorted(players.items(), key=lambda item: item[1]['rating'], reverse=True)
    
    print("Таблица лидеров:")
    # Перебираем отсортированный список и выводим каждого игрока
    for rank, (player_id, data) in enumerate(sorted_players, start=1):
        print(f"{rank}. {data['name']} - {data['rating']} очков ({data['matches']} матчей)")

# Пример использования:
if __name__ == "__main__":
    # Регистрация нескольких матчей
    register_match(1, 2, 1)  # Алексей побеждает Марию
    register_match(3, 1, 2)  # Дмитрий побеждает Алексея
    register_match(2, 3, 0)  # Мария и Дмитрий сыграли ничью
    
    print()
    # Вывод таблицы лидеров
    show_leaderboard()
