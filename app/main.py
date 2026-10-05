from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int, cleaner: str, movie: str) -> None:
    film_customers = []
    for customer in customers:
        film_customer = Customer(customer["name"], customer["food"])
        film_customers.append(film_customer)
        CinemaBar.sell_product(film_customer.food, film_customer)
    cinema = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    cinema.movie_session(movie, film_customers, hall_cleaner)
