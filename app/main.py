# write your imports here
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:
    # create Customer instances
    customer_objs: list[Customer] = [
        Customer(c["name"], c["food"]) for c in customers
    ]

    # sell food via CinemaBar (static method)
    for cust in customer_objs:
        CinemaBar.sell_product(cust.food, cust)

    # create hall and cleaner instances
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # run movie session which will also trigger cleaning
    hall.movie_session(movie, customer_objs, cleaning_staff)
