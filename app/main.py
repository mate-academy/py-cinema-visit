from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_instances = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customers_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall_instance.movie_session(movie_name=movie,
                                customers=customers_instances,
                                cleaning_staff=cleaner_instance)
