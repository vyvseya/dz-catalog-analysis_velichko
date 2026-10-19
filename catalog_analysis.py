import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# Этап 1 
def average_rating(movies):
    """Возвращает средний рейтинг фильмов с округлением до одного знака"""
    total_rating = 0

    for movie in movies:
        total_rating += movie["rating"]

    average = total_rating / len(movies)
    return round(average, 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает максимальный, минимальный и средний возраст фильмов"""
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average_age)


def duration_in_hours(minutes):
    """Переводит минуты в строку с часами и минутами"""
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"

# Этап 2
def rating_tier(rating): 
    """Определяет категорию фильма по рейтингу"""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Определяет категорию фильма по году выпуска"""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


if __name__ == "__main__":
    # Проверки этапа 1
    print("Средний рейтинг:", average_rating(movies))
    print("Статистика возраста:", catalog_age_stats(movies))
    print("Продолжительность:", duration_in_hours(155))

    # Проверки этапа 2
    print("Рейтинг 9.2:", rating_tier(9.2))
    print("Рейтинг 8.6:", rating_tier(8.6))
    print("Рейтинг 6.4:", rating_tier(6.4))
    print("Рейтинг 4.8:", rating_tier(4.8))
    print("Год 2014:", decade_label(2014))
    print("Год 2015:", decade_label(2015))
    print("Год 2020:", decade_label(2020))
    print("Год 2021:", decade_label(2021))
    print("Год 2024:", decade_label(2024))