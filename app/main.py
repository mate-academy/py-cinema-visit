from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(customer_list[-1], customer_list[-1].food)
    cleaner_inst = Cleaner(cleaner)

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_inst
    )
