from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    list_of_customers = []
    for cus in customers:
        customer = Customer(cus["name"], cus["food"])
        list_of_customers.append(customer)
        CinemaBar.sell_product(cus["food"], customer)

    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, list_of_customers, cleaner_obj)
