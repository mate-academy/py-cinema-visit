from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customer_list = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    for customer in customer_list:
        cinema_bar = CinemaBar()
        cinema_bar.sell_product(customer.food, customer)

    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
