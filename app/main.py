from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    new_customers = []
    for customer_data in customers:
        new_customers.append(Customer(customer_data["name"],
                                      customer_data["food"]))

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in new_customers:
        cinema_bar.sell_product(customer, customer.food)
    hall.movie_session(movie, new_customers, cleaner)
