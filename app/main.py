from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [Customer(name=customer["name"],
                              food=customer["food"]) for customer in customers]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    for customer in customer_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_list,
                              cleaner=cleaning_staff)
