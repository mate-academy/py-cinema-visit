from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # створюємо об'єкти Customer
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    # продаємо їжу (static method)
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # створюємо зал і прибиральника
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # запускаємо сеанс
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )