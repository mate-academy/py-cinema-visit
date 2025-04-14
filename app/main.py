# write your imports here
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
    customers_list = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in customers_list:
        CinemaBar.sell_product(
            product=customer.food, customer=customer
        )

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_staff
    )
