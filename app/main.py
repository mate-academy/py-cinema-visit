from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(
            Customer(name=customer["name"],
                     food=customer["food"])
        )
    hall = CinemaHall(number=hall_number)
    clean = Cleaner(name=cleaner)
    for one_customer in customer_list:
        CinemaBar.sell_product(one_customer, one_customer.food)
    hall.movie_session(movie, customer_list, clean)
