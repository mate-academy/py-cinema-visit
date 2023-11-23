from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cust_inst = []
    for customer in customers:
        cust_inst.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in cust_inst:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(
        movie_name=movie,
        customers=cust_inst,
        cleaning_stuff=cleaner
    )
