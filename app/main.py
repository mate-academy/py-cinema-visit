from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str,
                 ) -> None:
    list_customers = [Customer(customer["name"], customer["food"])
                      for customer in customers]
    current_cleaner = Cleaner(cleaning_staff)
    hall_cinema = CinemaHall(hall_number)

    for customer in list_customers:
        CinemaBar.sell_product(customer, customer.food)

    hall_cinema.movie_session(movie_name, list_customers, current_cleaner)
