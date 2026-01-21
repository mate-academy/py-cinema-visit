# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    # write you code here
    humans = [Customer(human["name"], human["food"]) for human in customers]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleanning_staff = Cleaner(cleaner)
    for human in humans:
        cinema_bar.sell_product(human.food, human)
    hall.movie_session(movie, humans, cleanning_staff)
