from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_objects = [Customer(customer_dict["name"], customer_dict["food"])
                        for customer_dict in customers]

    cinema_bar = CinemaBar()
    for customer in customer_objects:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)

    cleaner_name = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_name)
