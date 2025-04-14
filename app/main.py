from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    for customer in customers:
        customer_instances.append(Customer(customer["name"], customer["food"]))
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instances,
                              cleaning_staff=cleaner)
