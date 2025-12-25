from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    for i in range(len(customers)):
        customer_instance = [Customer(c["name"], c["food"]) for c in customers]
        cleaner_instance = Cleaner(cleaner)
        hall = CinemaHall(hall_number)
    for customer in customer_instance:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instance,
        cleaner_staff=cleaner_instance)
