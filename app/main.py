from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = []
    for customer in customers:
        customer_objects.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner)
