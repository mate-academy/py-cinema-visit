from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for customer in customers:
        new_costumer = Customer(customer["name"], customer["food"])
        customers_list.append(new_costumer)
        CinemaBar.sell_product(customer["food"], new_costumer)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_list,
                              cleaning_staff=cleaner)
