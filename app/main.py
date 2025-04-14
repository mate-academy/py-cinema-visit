from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_objs = [
        Customer(
            customer_dict["name"],
            customer_dict["food"]
        )
        for customer_dict in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customers_objs:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_objs, cleaning_staff)
