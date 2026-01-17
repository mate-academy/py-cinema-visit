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
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"]
        )
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**customer) for customer in customers],
        cleaning_staff=cleaner
    )
