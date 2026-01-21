from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_of_customer = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        list_of_customer.append(customer_obj)
    for one_customer in list_of_customer:
        CinemaBar.sell_product(one_customer.food, one_customer)
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    hall.movie_session(movie, list_of_customer, cleaner_staff)
