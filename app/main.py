from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(cuss: list, h_number: int, clea: str, mov: str) -> None:

    cus = [Customer(name=cus["name"], food=cus["food"]) for cus in cuss]

    # Продаж їжі клієнтам
    for customer in cus:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Створення об'єкта CinemaHall
    hall = CinemaHall(number=h_number)

    # Створення об'єкта Cleaner
    cleaning_staff = Cleaner(name=clea)

    # Проведення кіносеансу
    hall.movie_session(nm=mov, css=cus, cl=cleaning_staff)
