from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    cinema_customers = []
    for customer in customers:
        cinema_customers.append(Customer(name=customer["name"],
                                         food=customer["food"]))
        cinema_bar.sell_product(customer=cinema_customers[-1],
                                product=cinema_customers[-1].food)
    cinema_hall.movie_session(film_name=movie,
                              customers=cinema_customers,
                              cleaning_staff=cleaner_staff)
