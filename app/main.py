from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_list = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    cinema_bar = CinemaBar()
    for customer_info in customer_list:
        cinema_bar.sell_product(customer_info.food, customer_info)
    staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_list, staff)
