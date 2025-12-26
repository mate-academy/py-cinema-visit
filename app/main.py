from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    new_customers = []
    for customer in customers:
        new_customers.append(Customer(customer["name"], customer["food"]))
    new_hall = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    new_bar = CinemaBar
    for customer in new_customers:
        new_bar.sell_product(customer, customer.food)
    new_hall.movie_session(movie, new_customers, new_cleaner)
