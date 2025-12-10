from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: Customer,
    hall_number: int,
    cleaner: Cleaner,
    movie: str
) -> None:
    cus_objects = [Customer(cus["name"], cus["food"]) for cus in customers]

    for cust in cus_objects:
        CinemaBar.sell_product(cust.food, cust)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, cus_objects, cleaner_obj)
