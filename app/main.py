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
    customers_obj = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    cinema_hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    for customer in customers_obj:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall_obj.movie_session(movie, customers_obj, cleaner_obj)
