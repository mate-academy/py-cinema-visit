from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    list_of_customers = []
    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(list_of_customers[-1], customer["food"])

    cleaner_of_the_hall = Cleaner(cleaner)

    CinemaHall(hall_number).movie_session(movie,
                                          list_of_customers,
                                          cleaner_of_the_hall)
