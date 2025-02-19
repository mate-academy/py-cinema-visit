from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    # Створення об'єктів
    customer_objects = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    # Продаж їжі
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Кінопоказ
    cinema_hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_obj)


# Приклад виклику
customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"

cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
