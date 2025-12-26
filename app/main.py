from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
# write your imports here


def cinema_visit(customers: list, number: int, cleaner: str,
                 movie: str) -> None:
    customer_instances = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]
    cleaner_instance = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number)
    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
