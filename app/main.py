from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_objs = list()
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_objs.append(customer_obj)

        CinemaBar.sell_product(
            customer=customer_obj,
            product=customer_obj.food
        )

    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_objs, cleaner)
