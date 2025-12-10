from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # створюємо список об'єктів Customer
    customer_objects = [Customer(name=c["name"], food=c["food"]) for c in customers]

    # продаємо їжу кожному клієнту через CinemaBar (статичний метод)
    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # створюємо об'єкт Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # створюємо об'єкт CinemaHall
    hall = CinemaHall(hall_number=hall_number)

    # запускаємо кіносесію
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
