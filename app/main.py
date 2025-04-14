from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, list_of_customers, cleaning_staff)
