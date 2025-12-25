from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    customers_list = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(customer=cust, product=cust.food)
        customers_list.append(cust)
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_staff
    )
