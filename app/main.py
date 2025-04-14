# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str, movie: str) -> None:

    people_lst = []
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        people_lst.append(customer_obj)
        cinema_bar.sell_product(customer_obj, customer_obj.food)

    hall.movie_session(movie, people_lst, cleaner)
