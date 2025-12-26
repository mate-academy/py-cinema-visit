from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_list_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in new_list_customers:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, new_list_customers, cleaning_staff)
