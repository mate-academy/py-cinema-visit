from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances = [
        Customer(cus["name"], cus["food"])
        for cus in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    for customer in customers_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie, customers_instances, new_cleaner)
