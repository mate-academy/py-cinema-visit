from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    clr = Cleaner(cleaner)
    for customer in customers:
        customer_res = Customer(name=customer["name"],
                                food=customer["food"])
        cinema_bar.sell_product(customer=customer_res,
                                product=customer_res.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=[Customer(**kwargs)
                                         for kwargs in customers],
                              cleaning_staff=clr)
