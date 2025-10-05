from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    one_customer = [Customer(i["name"], i["food"]) for i in customers]

    for cust in one_customer:
        CinemaBar.sell_product(cust.food, cust)

    hall = CinemaHall(hall_number)

    one_cleaner = Cleaner(cleaner)

    hall.movie_session(movie, one_customer, one_cleaner)
