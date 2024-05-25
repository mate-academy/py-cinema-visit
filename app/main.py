from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_instances = [
        Customer(name=client["name"], food=client["food"])
        for client in customers
    ]
    cinema_hall_instance = CinemaHall(number=hall_number)
    cinema_bar_instance = CinemaBar()
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customers_instances:
        cinema_bar_instance.sell_product(product=customer.food,
                                         customer=customer)
    cinema_hall_instance.movie_session(movie_name=movie,
                                       customers=customers_instances,
                                       cleaning_staff=cleaner_instance)
