from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str) -> None:
    custom_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        custom_list.append(new_customer)
        cin_bar = CinemaBar
        cin_bar.sell_product(new_customer, new_customer.food)

    clear = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie, customers=custom_list, cleaning_staff=clear
    )
