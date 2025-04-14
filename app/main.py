from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: Cleaner | str,
                 movie: str) -> None:
    customer_instances = [
        Customer(name=cust["name"], food=cust["food"]) for cust in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()

    for customer in customer_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instances,
                              cleaning_staff=cleaner_instance)
