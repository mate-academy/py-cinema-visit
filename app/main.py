from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = \
        [Customer(cus["name"], cus["food"]) for cus in customers]

    new_hall = CinemaHall(hall_number)

    new_cinema_staff = Cleaner(cleaner)

    [
        CinemaBar.sell_product(customer_instance.food, customer_instance)
        for customer_instance in customer_instances
    ]

    new_hall.movie_session(movie, customer_instances, new_cinema_staff)
