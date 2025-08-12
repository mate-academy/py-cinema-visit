from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner)
