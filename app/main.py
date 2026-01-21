from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cust_instances = [Customer(cus["name"], cus["food"]) for cus in customers]
    for cus in cust_instances:
        CinemaBar.sell_product(cus.food, cus)
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_hall.movie_session(movie, cust_instances, cleaner_instance)
