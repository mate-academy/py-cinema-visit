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
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)

    customer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer_item in customer_list:
        cinema_bar.sell_product(customer_item, customer_item.food)

    cinema_hall.movie_session(movie, customer_list, cleaner_staff)
