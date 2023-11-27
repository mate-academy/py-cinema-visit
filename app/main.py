from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_customers = []
    for customer in customers:
        cinema_customers.append(Customer(customer["name"], customer["food"]))
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in cinema_customers:
        bar.sell_product(customer.food, customer)
    hall.movie_session(movie, cinema_customers, cleaner)
