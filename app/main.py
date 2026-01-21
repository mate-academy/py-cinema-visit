from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = []

    for person in customers:
        one_customer = Customer(person["name"], person["food"])
        visitors.append(one_customer)
        CinemaBar.sell_product(one_customer.food, one_customer)

    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    CinemaHall.movie_session(hall, movie, visitors, cleaner)
