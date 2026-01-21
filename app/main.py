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
    customers = list(
        map(lambda customer_record: Customer(
            customer_record["name"],
            customer_record["food"]),
            customers
            )
    )
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customers:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner
    )
