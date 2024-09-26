from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = [
        Customer(costumer["name"], costumer["food"]) for costumer in customers
    ]
    cleaner_staff = Cleaner(cleaner)
    for costumer in customer_list:
        CinemaBar.sell_product(costumer.food, costumer)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_list, cleaner_staff)
