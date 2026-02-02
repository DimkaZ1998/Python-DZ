class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = None

    def set_rating(self, rating):
        if 1 <= rating <= 10:
            self.rating = rating
        else:
            raise ValueError("Рейтинг должен быть от 1 до 10")

    def is_high_rated(self):
        return self.rating is not None and self.rating >= 8

    def __str__(self):
        rating_str = f"{self.rating}" if self.rating is not None else "Нет оценки"
        return f"{self.title} ({self.year}) - {self.director} [{self.genre}] ★{rating_str}"


class MovieCollection:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        # Проверка на уникальность по названию
        if self.get_movie_by_title(movie.title) is None:
            self.movies.append(movie)
        else:
            print(f"Фильм с названием '{movie.title}' уже есть в коллекции.")

    def remove_movie(self, title):
        movie = self.get_movie_by_title(title)
        if movie:
            self.movies.remove(movie)
        else:
            print(f"Фильм с названием '{title}' не найден.")

    def get_movie_by_title(self, title):
        for movie in self.movies:
            if movie.title == title:
                return movie
        return None

    def rate_movie(self, title, rating):
        movie = self.get_movie_by_title(title)
        if movie:
            try:
                movie.set_rating(rating)
            except ValueError as e:
                print(e)
        else:
            print(f"Фильм с названием '{title}' не найден.")

    def get_top_movies(self, limit=5):
        rated_movies = [m for m in self.movies if m.rating is not None]
        sorted_movies = sorted(rated_movies, key=lambda m: m.rating, reverse=True)
        return sorted_movies[:limit]

    def get_movies_by_genre(self, genre):
        return [m for m in self.movies if m.genre == genre]

    def get_stats(self):
        total_movies = len(self.movies)
        rated_movies = [m for m in self.movies if m.rating is not None]
        rated_count = len(rated_movies)
        average_rating = (sum(m.rating for m in rated_movies) / rated_count) if rated_count > 0 else 0
        genres = [m.genre for m in self.movies]
        most_common_genre = max(set(genres), key=genres.count) if genres else None
        high_rated_count = len([m for m in self.movies if m.rating is not None and m.rating >= 8])
        return {
            'total_movies': total_movies,
            'rated_movies': rated_count,
            'average_rating': round(average_rating, 2),
            'most_common_genre': most_common_genre,
            'high_rated_count': high_rated_count
        }

    def __str__(self):
        return f"Коллекция '{self.name}': {len(self.movies)} фильмов"


# Пример использования:
# Создаем коллекцию
my_collection = MovieCollection("Мои любимые фильмы")

# Создаем фильмы
film1 = Movie("Начало", "Кристофер Нолан", 2010, "фантастика")
film2 = Movie("Крестный отец", "Фрэнсис Форд Коппола", 1972, "драма")

# Добавляем в коллекцию
my_collection.add_movie(film1)
my_collection.add_movie(film2)

# Оцениваем фильмы
my_collection.rate_movie("Начало", 9)
my_collection.rate_movie("Крестный отец", 10)

# Получаем статистику
stats = my_collection.get_stats()
print(f"Всего фильмов: {stats['total_movies']}")
print(f"Средний рейтинг: {stats['average_rating']}")

# Ищем фильмы по жанру
fantasy_movies = my_collection.get_movies_by_genre("фантастика")
for m in fantasy_movies:
    print(Movie)
