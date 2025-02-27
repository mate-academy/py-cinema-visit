from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    all_customer = []
    for customer in customers:
        buyer = Customer(customer["name"], customer["food"])
        all_customer.append(buyer)
        CinemaBar.sell_product(buyer, buyer.food)

    cinema = CinemaHall(hall_number)
    cinema.movie_session(movie, all_customer, Cleaner(cleaner))
