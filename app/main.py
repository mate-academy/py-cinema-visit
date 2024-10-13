from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> str:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    cinema_customers = [Customer(name=customer["name"],
                        food=customer["food"]) for customer in customers]

    cleaner = Cleaner(cleaner)
    for customer in cinema_customers:
        cinema_bar.sell_product(customer.food, customer)

    (cinema_hall.movie_session(
        movie_name=movie, customers=cinema_customers,
        cleaner=cleaner))
