from app.cinema_bar import CinemaBar
from app.cinema_hall import CinemaHall
from app.cleaner import Cleaner
from app.people.customer import Customer


def cinema_visit(customers, movie, menu, cinema_bar, cinema_hall, cleaner):
    # Сеанс фильма начинается
    cinema_hall.start_session(movie)

    # Покупка продуктов в баре
    for customer in customers:
        cinema_bar.sell_product({"name": customer}, "popcorn", menu)

    # Просмотр фильма
    for customer in customers:
        print(f"{customer} is watching {movie}.")

    # Фильм заканчивается
    cinema_hall.end_session(movie)

    # Уборка после сеанса
    cleaner.clean_hall(cinema_hall.hall_id)