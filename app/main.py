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
    list_of_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner_person = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in list_of_customers:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(
        movie_name=movie,
        cleaning_staff=cleaner_person,
        customers=list_of_customers
    )
