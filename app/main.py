from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str, customers: list, hall_number: int, cleaner: str
) -> None:
    session = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)
    customers_in_the_cinema = []

    for client in customers:
        customer_instance = Customer(name=client["name"], food=client["food"])
        customers_in_the_cinema.append(customer_instance)
        CinemaBar.sell_product(client["food"], customer_instance)

    session.movie_session(movie, customers_in_the_cinema, cinema_cleaner)
