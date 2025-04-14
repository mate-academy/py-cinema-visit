from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = [Customer(movie_visitor["name"],
                              movie_visitor["food"])
                     for movie_visitor in customers]
    for movie_visitor in customer_list:
        CinemaBar.sell_product(
            movie_visitor.food, movie_visitor)
    CinemaHall(hall_number).movie_session(movie,
                                          customer_list, Cleaner(cleaner))
