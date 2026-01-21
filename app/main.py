from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    all_customers = []
    bar = CinemaBar()
    for customer in customers:
        new_customers = Customer(customer["name"], customer["food"])
        all_customers.append(new_customers)
        bar.sell_product(new_customers.food, new_customers)

    hall = CinemaHall(hall_number)
    cleaner_worker = Cleaner(cleaner)
    hall.movie_session(movie, all_customers, cleaner_worker)
