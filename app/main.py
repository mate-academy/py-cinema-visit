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
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    instances_of_customers = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    for person in instances_of_customers:
        cinema_bar.sell_product(person, person.food)
    cinema_hall.movie_session(movie, instances_of_customers, cinema_cleaner)
