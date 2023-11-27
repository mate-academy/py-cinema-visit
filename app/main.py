from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_inst_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers_inst_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name=movie, customers=customers_inst_list,
                              cleaning_staff=cleaner)
