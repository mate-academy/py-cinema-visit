from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cb = CinemaBar()
    list_of_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in list_of_customers:
        cb.sell_product(customer=customer, product=customer.food)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=cleaning_staff
    )
