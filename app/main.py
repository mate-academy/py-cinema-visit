from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    movie_customers = []
    for custom in customers:
        movie_customers.append(Customer(custom["name"], custom["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_ = Cleaner(cleaner)
    for customer in movie_customers:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, movie_customers, cleaner_)
