from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]
    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    correct_hall_number = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    correct_hall_number.movie_session(movie, customers_list, cleaner_name)
