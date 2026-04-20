from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objectrs = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"],
                                food=customer["food"])
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)
        customer_objectrs.append(customer_obj)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objectrs,
        cleaning_staff=Cleaner(name=cleaner)
    )
