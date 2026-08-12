from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    served_customers = []
    for customer in customers:
        cust = Customer(name=customer["name"], food=customer["food"])
        served_customers.append(cust)
        CinemaBar.sell_product(product=customer["food"], customer=cust)
    ch = CinemaHall(hall_number)
    clear = Cleaner(cleaner)
    ch.movie_session(movie, served_customers, clear)
