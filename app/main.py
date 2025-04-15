from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    cinema_customers = []
    cinema_hall = CinemaHall(hall_number)
    cleaner_job = Cleaner(cleaner)

    for customer in customers:
        new_customer = Customer(customer["name"],
                                customer["food"])
        CinemaBar.sell_product(customer["food"], new_customer)

        cinema_customers.append(new_customer)

    cinema_hall.movie_session(movie, cinema_customers, cleaner_job)
