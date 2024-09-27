# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    clients = [
        Customer(name=customer_inf["name"], food=customer_inf["food"])
        for customer_inf in customers
    ]

    for customer in clients:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, clients, cleaner)
