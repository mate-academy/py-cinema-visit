from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    classed_customers = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(
            customer.name,
            customer.food
        )
        classed_customers.append(customer)

    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=classed_customers,
        cleaning_staff=cleaning_staff.name
    )
