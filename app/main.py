from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    new_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)

    list_of_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)
        CinemaBar().sell_product(new_customer.food, new_customer)

    new_hall.movie_session(movie, list_of_customers, hall_cleaner)
