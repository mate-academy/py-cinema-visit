from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_customers = []

    for customer in customers:
        new_customers.append(Customer(customer["name"], customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)

    for new_customer in new_customers:
        cinema_bar.sell_product(new_customer.food, new_customer)
    cinema_hall.movie_session(movie, new_customers, cinema_cleaner)
