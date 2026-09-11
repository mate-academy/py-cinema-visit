from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customer_list = []

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_list.append(customer)

    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie_name=movie,
                       customers=customer_list,
                       cleaning_staff=cleaner)
