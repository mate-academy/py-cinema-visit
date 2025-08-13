from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str):
    customer_objects = []
    for c in customers:
        customer_instance = Customer(name=c["name"], food=c["food"])
        CinemaBar.sell_product(product=customer_instance.food, customer=customer_instance)
        customer_objects.append(customer_instance)

    hall = CinemaHall(number=hall_number)

    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
