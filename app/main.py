from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_customers = []
    for customer in customers:
        cinema_customer = Customer(customer.get("name"), customer.get("food"))
        CinemaBar.sell_product(customer.get("food"), cinema_customer)
        cinema_customers.append(cinema_customer)

    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)
