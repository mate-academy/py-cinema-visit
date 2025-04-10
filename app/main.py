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
    hall = CinemaHall(hall_number)
    hall_bar = CinemaBar()
    hall_cleaner = Cleaner(cleaner)

    hall_customers = []

    for person in customers:
        hall_customers.append(Customer(person["name"], person["food"]))
        hall_bar.sell_product(
            Customer(person["name"], person["food"]),
            person["food"]
        )

    hall.movie_session(movie, hall_customers, hall_cleaner)
