from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = []
    for customer in customers:
        cust1 = Customer(customer.get("name"), customer.get("food"))
        customer_instances.append(cust1)

    cinemahall = CinemaHall(hall_number)
    cinemabar = CinemaBar
    cleaner = Cleaner(cleaner)

    for customer in customer_instances:
        cinemabar.sell_product(customer.food, customer)

    cinemahall.movie_session(movie, customer_instances, cleaner)
