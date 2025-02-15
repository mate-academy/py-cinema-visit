from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int, cleaner:
        str, movie: str
) -> None:
    cleaner = Cleaner(cleaner)
    movie_hall = CinemaHall(hall_number)

    list_customers = [Customer(c["name"], c["food"]) for c in customers]

    for customer in list_customers:
        CinemaBar.sell_product(customer, customer.food)

    movie_hall.movie_session(movie, list_customers, cleaner)
