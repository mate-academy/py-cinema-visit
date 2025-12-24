from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)

    for customer in cinema_customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, cinema_customers, cleaner_stuff)
