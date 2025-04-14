from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str):
    # Створення об'єктів клієнтів
    customer_objects = [Customer(name=c["name"], food=c["food"]) for c in customers]

    # Продаж продуктів у барі
    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)

    # Створення кінозалу та прибиральника
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # Запуск кінопоказу
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
