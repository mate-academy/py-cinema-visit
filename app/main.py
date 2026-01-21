from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_instances = [Customer(d.get("name"), d.get("food"))
                           for d in customers]

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)

    for customer in customers_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_instances, cinema_cleaner)
