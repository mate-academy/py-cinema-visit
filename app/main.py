from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_object = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_object.append(customer_obj)

    for cust_obj in customers_object:
        CinemaBar.sell_product(cust_obj, cust_obj.food)

    occupiedCleaner = Cleaner(cleaner)
    ch = CinemaHall(hall_number)

    # ask mentor why "self" here demands object "ch"
    CinemaHall.movie_session(ch, movie, customers_object, occupiedCleaner)
