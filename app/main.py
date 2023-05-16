from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_instance = [(Customer(customer["name"], customer["food"]))
                          for customer in customers]

    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    [bar_instance.sell_product(customer.food, customer)
     for customer in customers_instance]

    hall_instance.movie_session(movie, customers_instance, cleaner_instance)
