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

    list_of_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]

    hall = CinemaHall(number=hall_number)
    the_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)

    for customer in list_of_customers:
        the_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=cleaner
    )
