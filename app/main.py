from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    clean_staff = Cleaner(name=cleaner)

    customer_objects = [Customer(name=single_customer.get("name"),
                                 food=single_customer.get("food"))
                        for single_customer in customers]

    [cinema_bar.sell_product(customer=customer, product=customer.food)
     for customer in customer_objects]

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_objects,
                              cleaning_staff=clean_staff)
