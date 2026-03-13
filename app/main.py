from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cutomer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in cutomer_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=cutomer_list,
        cleaning_staff=cleaning_staff
    )
