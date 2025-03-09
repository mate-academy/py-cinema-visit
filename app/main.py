from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(hall_number)
    stall = CinemaBar()
    cleaner = Cleaner(cleaner)
    customers_list = []
    for person in customers:
        customers_list.append(Customer(person["name"], person["food"]))
    for person in customers_list:
        stall.sell_product(person, person.food)
    hall.movie_session(movie, customers_list, cleaner)
