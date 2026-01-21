from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int, cleaner: str, movie: str) -> None:
    cb = CinemaBar()
    cleaner_cl = Cleaner(cleaner)
    cust_cl = []
    for i in customers:
        cust_cl.append(Customer(i["name"], i["food"]))

    for i in cust_cl:
        cb.sell_product(i.food, i)

    ch = CinemaHall(hall_number)
    ch.movie_session(movie, cust_cl, cleaner_cl)
