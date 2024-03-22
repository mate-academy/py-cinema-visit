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
    cinema_hall = CinemaHall(hall_number)
    customers_list = []
    for data in customers:
        customer = Customer(data["name"], data["food"])
        CinemaBar.sell_product(customer.food, customer)
        customers_list.append(customer)

    cinema_hall.movie_session(movie, customers_list, cleaner_instance)
