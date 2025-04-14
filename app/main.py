# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cleaner_staff = Cleaner(cleaner)
    customer_list = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    cinema = CinemaHall(hall_number)
    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema.movie_session(movie, customer_list, cleaner_staff)
