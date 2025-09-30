from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_obj = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_obj.append(customer)

        CinemaBar.sell_product(customer, customer.food)

    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customers_obj, cleaner)
