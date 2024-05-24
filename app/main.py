from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)

    customer_objects = []
    for customer_info in customers:
        customer = (Customer
                    (name=customer_info["name"], food=customer_info["food"]))
        cinema_bar.sell_product(customer, customer.food)
        customer_objects.append(customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_objects,
                              cleaning_staff=cinema_cleaner)
