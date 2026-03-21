from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    for cust in customers:
        human = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(product=human.food, customer=human)
        customer_instances.append(human)
    hall = CinemaHall(hall_number)
    cleaner_inst = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=cleaner_inst)
