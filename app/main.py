from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_1 = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        customers_1.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    CinemaHall(hall_number).movie_session(movie_name=movie,
                                          customers=customers_1,
                                          cleaner_stuff=Cleaner(cleaner))
