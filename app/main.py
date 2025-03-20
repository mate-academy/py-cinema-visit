from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)
    customers_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customers_list.append(new_customer)
        CinemaBar.sell_product(customer["food"], new_customer)

    CinemaHall.movie_session(cinema_hall,
                             movie,
                             customers_list,
                             cleaner_person)
