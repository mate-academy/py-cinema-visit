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
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    list_of_customers = []
    for customer in customers:
        list_of_customers.append(
            Customer(customer.get("name"), customer.get("food"))
        )
    for from_customers in list_of_customers:
        cinema_bar.sell_product(from_customers.food, from_customers)
    cinema_hall.movie_session(movie, list_of_customers, cinema_cleaner)
