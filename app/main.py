from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = [Customer(name=cust["name"],
                                  food=cust["food"])
                         for cust in customers]
    hall_num = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for visitor_1 in list_of_customers:
        cinema_bar = CinemaBar()
        cinema_bar.sell_product(visitor_1.food, visitor_1)
    CinemaHall.movie_session(hall_num, movie, list_of_customers, staff)
