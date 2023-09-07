from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: str,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**customer) for customer in customers],
        cleaning_staff=Cleaner(name=cleaner)
    )
