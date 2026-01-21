# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_instances_list = []
    for customer in customers:
        customer_visiter = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], customer_visiter)
        customers_instances_list.append(customer_visiter)
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customers_instances_list, cleaner)
