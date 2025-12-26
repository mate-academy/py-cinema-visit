from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_in_movie = [Customer(customer["name"], customer["food"])
                          for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer_in_movie in customers_in_movie:
        cinema_bar.sell_product(customer_in_movie.food, customer_in_movie)

    hall.movie_session(movie, customers_in_movie, cleaner_stuff)
