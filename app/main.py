from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[Customer],
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_list = [Customer(customer["name"],
                              customer["food"]) for customer in customers]
    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_list, cleaner)
