from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_objs = [Customer(
        name=customer["name"],
        food=customer["food"])
        for customer in customers]

    cleaner_obj = Cleaner(cleaner)

    for customer in customers_objs:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food)

    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(
        movie_name=movie,
        customers_list=customers_objs,
        cleaning_staff=cleaner_obj)
