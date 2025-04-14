from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_lst = [Customer(el["name"], el["food"]) for el in customers]

    for customer in customers_lst:
        CinemaBar.sell_product(customer, customer.food)

    cleaner_inst = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_lst, cleaner_inst)
