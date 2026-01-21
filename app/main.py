from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))
    for i in customer_list:
        CinemaBar.sell_product(i.food, i)
    new_hall_number = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    new_hall_number.movie_session(movie, customer_list, new_cleaner)
