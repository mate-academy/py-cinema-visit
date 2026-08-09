from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_list = []
    for person in customers:
        customer_obj = Customer(person["name"], person["food"])
        CinemaBar.sell_product(customer=customer_obj, product=person["food"])
        customers_list.append(customer_obj)
    cleaner_obj = Cleaner(cleaner)
    c_hall = CinemaHall(hall_number)
    c_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_obj)
