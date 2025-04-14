from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)
    for customer in list_of_customers:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, list_of_customers, cleaner_staff)
