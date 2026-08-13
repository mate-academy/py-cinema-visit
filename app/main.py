from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    class_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )

        for customer in customers
    ]

    for customer in class_customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, class_customers, Cleaner(cleaner))
