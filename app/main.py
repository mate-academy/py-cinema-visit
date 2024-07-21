from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list, hall_number: int,
    cleaner: str, movie: str
) -> None:
    cinema_customers = []
    for customer in customers:
        cinema_customers.append(Customer(customer["name"], customer["food"]))

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for cinema_customer in cinema_customers:
        CinemaBar.sell_product(cinema_customer.food, cinema_customer)

    cinema_hall.movie_session(movie, cinema_customers, cleaner)
