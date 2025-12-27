from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall1 = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall1.movie_session(movie, customer_instances, cleaner1)
