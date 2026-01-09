from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    customers_objects = []
    for customer_dict in customers:
        customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        customers_objects.append(customer)

    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for customer in customers_objects:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_objects, cinema_cleaner)
