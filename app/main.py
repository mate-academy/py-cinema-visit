from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]
    cleaner = Cleaner(cleaner)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, list_of_customers, cleaner)
