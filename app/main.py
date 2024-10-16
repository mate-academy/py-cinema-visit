from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    """
    Function that corresponds to cinema visit, creates all the instances and
    triggers its functions to show step by step how cinema is working.
    :param customers: list of customers
    :param hall_number: hall number when movie is played
    :param cleaner: cleaner staff name
    :param movie: movie name to be played
    :return: None
    """
    movie_customers = [
        Customer(
            name=customer["name"], food=customer["food"]
        ) for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(name=cleaner)

    for customer in movie_customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie, movie_customers, cleaner_staff)
