from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_ls = []
    for customer in customers:
        customers_ls.append(Customer(customer["name"], customer["food"]))

    bar = CinemaBar()

    for customer in customers_ls:
        bar.sell_product(customer, customer.food)

    start_end_movie = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    start_end_movie.movie_session(movie, customers_ls, cleaner)
