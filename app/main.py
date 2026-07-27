from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:

    customer_list = []

    for customer in customers:
        current_customer = Customer(
            customer["name"],
            customer["food"],
        )

        customer_list.append(current_customer)

        CinemaBar.sell_product(
            product=current_customer.food,
            customer=current_customer,
        )

    hall = CinemaHall(hall_number)

    hall.movie_session(
        movie,
        customer_list,
        Cleaner(cleaner),
    )
