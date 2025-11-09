from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    temp_hall = CinemaHall(hall_number)
    temp_cleaner = Cleaner(cleaner)
    list_customer = []
    for customer in customers:
        temp_customer = Customer(customer["name"], customer["food"])
        list_customer.append(temp_customer)
        CinemaBar.sell_product(temp_customer, temp_customer.food)
    temp_hall.movie_session(movie, list_customer, temp_cleaner)
