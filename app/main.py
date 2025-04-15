from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    customer_list = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    for person_instance in customer_list:
        cinema_bar.sell_product(person_instance.food, person_instance)
    hall.movie_session(
        movie, customer_list, cleaner
    )
