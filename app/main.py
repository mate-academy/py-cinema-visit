from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


# write your imports here
def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = [
        Customer(guest["name"], guest["food"]) for guest in customers
    ]

    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_instances, staff)
