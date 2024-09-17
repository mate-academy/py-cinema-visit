from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_customers = [Customer(customer["name"], customer["food"])
                        for customer in customers]

    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for cinema_customer in cinema_customers:
        CinemaBar.sell_product(cinema_customer.food, cinema_customer)

    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)
