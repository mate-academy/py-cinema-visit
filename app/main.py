from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_obj = [Customer(customer["name"],
                              customer["name"]) for customer in customers]

    for customer in customers:
        CinemaBar.sell_product(Customer(customer["name"],
                                        customer["food"]), customer["food"])

    cinema_hall.movie_session(movie, customers_obj, cleaner)
