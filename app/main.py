from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    hall = CinemaHall(number=hall_number)

    customer_objects = []
    for this_one in customers:
        next_customer = Customer(
            name=this_one["name"],
            food=this_one["food"]
        )
        customer_objects.append(next_customer)
        CinemaBar.sell_product(
            product=next_customer.food,
            customer=next_customer
        )

    hall_cleaner = Cleaner(name=cleaner)

    hall.movie_session(movie, customer_objects, hall_cleaner)
