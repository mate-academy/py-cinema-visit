from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for c in customers:
        customer = Customer(name=c["name"], food=c["food"])
        CinemaBar.sell_product(customer=customer, product=customer.food)
        customer_objects.append(customer)

    cleaning_staff = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)

    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
