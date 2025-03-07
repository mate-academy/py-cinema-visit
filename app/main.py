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
    cleaner_instance = Cleaner(cleaner)
    cinema_bar_instances = CinemaBar()
    hall = CinemaHall(hall_number)

    customers_instances_list = [
        Customer(name=person["name"],
                 food=person["food"])
        for person in customers
    ]

    for person in customers_instances_list:
        cinema_bar_instances.sell_product(customer=person,
                                          product=person.food)

    hall.movie_session(
        movie_name=movie,
        customers=customers_instances_list,
        cleaning_staff=cleaner_instance
    )
