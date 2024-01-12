from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_obj = []
    for customer in customers:
        customers_obj.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cbar = CinemaBar()
    cleaner_obj = Cleaner(cleaner)

    for customer in customers_obj:
        cbar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_obj, cleaner_obj)
