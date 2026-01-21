from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)

    for customer in list_of_customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, list_of_customers, cleaner_staff)
