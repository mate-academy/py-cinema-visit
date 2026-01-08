from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    """
    It handles all actions performed in the cinema, creating instances and
    calling imported functions and shows it in chronological order.
            1.  The customers buy their food.
            2.  The cinema hall show the movie.
            3.  The cinema staff go to clean the hall.
    Args:
        customers (list[dict]): A list with the customers and
                                        their choosen food.
        hall_number (int): The place where the movie is shown.
        cleaner (str): the cinema staff name that clean the given hall
                        when the show is over.
        movie (str): The name of the film that consumers choose to watch
    """
    visitors = [Customer(customer["name"], customer["food"])
                for customer in customers]
    hall_cleaner = Cleaner(cleaner)

    for customer in visitors:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)

    hall.movie_session(movie, visitors, hall_cleaner)
