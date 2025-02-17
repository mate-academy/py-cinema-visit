from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for element in customers:
        customer = Customer(name=element["name"], food=element["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(product=element["food"], customer=customer)
    cleaners_name = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie_title=movie,
        customers=customers_list,
        cleaning_staff=cleaners_name
    )
