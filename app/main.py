from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    customers_objs = [Customer(name=customer["name"], food=customer["food"])
                      for customer in customers]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customers_objs:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie_name, customers_objs, cleaning_staff)
