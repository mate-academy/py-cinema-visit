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
    customer_inst = []
    for customer in customers:
        customer_inst.append(
            Customer(name=customer["name"],
                     food=customer["food"])
        )
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for customer in customer_inst:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_inst, cinema_cleaner)
