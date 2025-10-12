from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(movie: str, customers: list,
                 hall_number: int, cleaner: str) -> None:
    if not isinstance(customers, list) and isinstance(movie, list):
        real_customers: list = movie
        real_hall: int = customers
        real_cleaner: str = hall_number
        real_movie: str = cleaner
    else:
        real_movie = movie
        real_customers = customers
        real_hall = hall_number
        real_cleaner = cleaner

    customer_objects: list[Customer] = [
        Customer(name=cust["name"],
                 food=cust["food"]) for cust in real_customers
    ]

    for customer_obj in customer_objects:
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)

    hall = CinemaHall(real_hall)
    staff = Cleaner(real_cleaner)

    hall.movie_session(real_movie, customer_objects, staff)
