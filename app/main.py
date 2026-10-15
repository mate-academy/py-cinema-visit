from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, cleaner_instance)
