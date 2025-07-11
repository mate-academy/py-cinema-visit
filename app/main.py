from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str,
                 ) -> None:
    customers_ = []
    for customer_ in customers:
        customer = Customer(
            name=customer_["name"],
            food=customer_["food"],
        )
        customers_.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall = CinemaHall(hall_number)
    CinemaHall.movie_session(
        cinema_hall,
        movie,
        customers_,
        Cleaner(name=cleaner)
    )
