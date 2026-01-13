from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str,
) -> None:
    cleaner_current = Cleaner(cleaner)
    hall_current = CinemaHall(hall_number)
    customer_list = [Customer(customer_current["name"],
                              customer_current["food"])
                     for customer_current in customers]

    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)

    hall_current.movie_session(
        movie,
        customer_list,
        cleaner_current
    )
