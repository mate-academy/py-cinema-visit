from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cleaner = Cleaner(cleaner)

    hall_number = CinemaHall(hall_number)

    customers_inst = []
    for customer in customers:
        customers_inst.append(Customer(name=customer["name"],
                                       food=customer["food"]))

    for customer in customers_inst:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    CinemaHall.movie_session(self=hall_number,
                             movie_name=movie,
                             customers=customers_inst,
                             cleaning_staff=cleaner)
