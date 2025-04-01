from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [Customer(customer["name"],
                 customer["food"]) for customer in customers]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie,
                       customers=customers,
                       cleaning_staff=cleaner)
