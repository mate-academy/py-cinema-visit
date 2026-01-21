# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customers = [
        Customer(name=people["name"], food=people["food"])
        for people in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    the_cleaner = Cleaner(cleaner)
    for people in list_customers:
        CinemaBar.sell_product(people, people.food)
    cinema_hall.movie_session(movie, list_customers, the_cleaner)
