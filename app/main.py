from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    """
    Function that corresponds to cinema visit,
    creates all the instances and triggers
    it functions to show step by step how cinema works.

    :param customers: list of customers
    :param hall_number: hall number where movie is played
    :param cleaner: cleaning staff name
    :param movie: movie name to be played
    :return: None
    """
    movie_customers = [
        Customer(
            name=customer["name"], food=customer["food"]
        ) for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    cinemabar = CinemaBar()

    for customer in movie_customers:
        cinemabar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie, movie_customers, cleaning_staff)
