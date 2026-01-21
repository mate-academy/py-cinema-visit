from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    customers_list: list[Customer] = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cleaner: Cleaner = Cleaner(cleaner_name)
    [CinemaBar.sell_product(custom, custom.food) for custom in customers_list]
    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
