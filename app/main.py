from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    list_of_customers = [Customer(i["name"], i["food"]) for i in customers]
    for i in list_of_customers:
        CinemaBar.sell_product(i.food, i)
    cinema_hall.movie_session(movie, list_of_customers, cleaner)
