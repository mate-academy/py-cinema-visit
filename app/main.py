from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    people = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        people.append(customer)
        CinemaBar.sell_product(customer_data["food"], customer)

    cinema_hall.movie_session(movie, people, cleaner_name)
