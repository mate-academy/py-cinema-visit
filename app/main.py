from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    linked_hall = CinemaHall(hall_number)
    linked_customers = []
    linked_cleaner = Cleaner(cleaner)
    for customer in customers:
        tmp = Customer(customer.get("name"), customer.get("food"))
        linked_customers.append(tmp)
        CinemaBar.sell_product(tmp, tmp.food)

    CinemaHall.movie_session(
        linked_hall,
        movie,
        linked_customers,
        linked_cleaner
    )
