from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> callable:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    # Створення екземплярів клієнтів зі списку словників customers_info
    customer_instances = [Customer(info["name"], info["food"])
                          for info in customers]

    # Продаж продуктів клієнтам у кінобарі
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    # Проведення кіносеансу в кінозалі
    cinema_hall.movie_session(movie, customer_instances, cleaner)
