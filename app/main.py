from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers2 = []
    for customer_ in customers:
        customers2.append(Customer(name=customer_["name"],
                                   food=customer_["food"]))
        CinemaBar.sell_product(product=customer_["food"],
                               customer=Customer(name=customer_["name"],
                                                 food=customer_["food"]))
    cinema_hall = CinemaHall(hall_number)
    cleaner2 = Cleaner(name=cleaner)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers2,
                              cleaning_stuff=cleaner2)
