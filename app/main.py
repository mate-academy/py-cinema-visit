from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_obj = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_obj.append(customer)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers_obj:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie_name=movie, customers=customers_obj, cleaning_staff=cleaner)
