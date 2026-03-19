from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_list, cleaning_staff)
