from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(new_customer.food, new_customer)
        customer_instances.append(new_customer)
    hall = CinemaHall(number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, customer_instances, clean)
