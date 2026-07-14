from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cur_customers = []
    cur_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customers:
        cur_cust = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cur_cust.food, cur_cust)
        cur_customers.append(cur_cust)

    hall.movie_session(movie, cur_customers, cur_cleaner)
