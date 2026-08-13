from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj,
        )

    hall = CinemaHall(hall_number)
    updated_cust = []
    cleaner = Cleaner(cleaner)
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        updated_cust.append(new_customer)
    hall.movie_session(
        movie_name=movie,
        customers=updated_cust,
        cleaning_staff=cleaner
    )
