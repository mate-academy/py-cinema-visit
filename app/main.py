from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    bar = CinemaBar()
    customer_objects = []

    for c in customers:
        customer = Customer(name=c["name"], food=c["food"])
        bar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)

