from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customers_instances = []
    for i in customers:
        customers_instances.append(Customer(i.get("name"), i.get("food")))

    for cust in customers_instances:
        CinemaBar.sell_product(cust.food, cust)

    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    hall_instance.movie_session(movie, customers_instances, cleaner_instance)
