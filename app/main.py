from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:

    customers_lst = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_inst = Cleaner(cleaner)

    for customer in customers_lst:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(movie_name=movie, customers=customers_lst, cleaning_staff=cleaner_inst)
