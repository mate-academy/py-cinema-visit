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
    customers_inst = []
    cleaner_inst = Cleaner(cleaner)
    for customer in customers:
        customer_inst = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        CinemaBar.sell_product(
            customer=customer_inst,
            product=customer_inst.food
        )
        customers_inst.append(customer_inst)
    cinema_hall_inst = CinemaHall(number=hall_number)
    cinema_hall_inst.movie_session(
        movie_name=movie,
        customers=customers_inst,
        cleaning_staff=cleaner_inst
    )
