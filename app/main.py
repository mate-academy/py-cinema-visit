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

    hall = CinemaHall(hall_number)
    cleaner_init = Cleaner(cleaner)
    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]

    for customer in customers_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie, customers_list, cleaner_init)
