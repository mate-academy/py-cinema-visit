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
        new_customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(product=customer["food"], customer=new_customer)
        customer_list.append(new_customer)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaner)
