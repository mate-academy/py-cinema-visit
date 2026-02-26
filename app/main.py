from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [Customer(c.get("name"), c.get("food")) for c in customers]

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    movie_hall = CinemaHall(hall_number)

    movie_hall.movie_session(movie, customer_list, Cleaner(cleaner))
