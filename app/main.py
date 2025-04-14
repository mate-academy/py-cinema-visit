# main.py

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: dict
                 , hall_number: int
                 , cleaner: str
                 , movie: str) -> None:

    # Створення екземплярів клієнтів
    customer_instances = [Customer(name=c["name"]
                                   , food=c["food"])
                          for c in customers]

    # Продаж їжі клієнтам
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Створення екземпляра залу
    cinema_hall = CinemaHall(number=hall_number)

    # Створення екземпляра прибиральника
    cleaning_staff = Cleaner(name=cleaner)

    # Початок кінопоказу
    cinema_hall.movie_session(movie_name=movie
                              , customers=customer_instances
                              , cleaning_staff=cleaning_staff
                              )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"

cinema_visit(customers=customers
             , hall_number=hall_number
             , cleaner=cleaner_name
             , movie=movie
             )
