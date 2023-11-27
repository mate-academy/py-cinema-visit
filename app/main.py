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
    customers_ob = []
    for customer in customers:
        customers_ob.append(
            Customer(
                name=customer.get("name"),
                food=customer.get("food")
            )
        )
    hall: CinemaHall = CinemaHall(hall_number)
    bar_instance: CinemaBar = CinemaBar()

    for customer_instance in customers_ob:
        bar_instance.sell_product(customer_instance, customer_instance.food)

    cleaner_instance = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customers_ob,
        cleaning_staff=cleaner_instance
    )
