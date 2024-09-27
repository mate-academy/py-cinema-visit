from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:

    customers_instance_list = []

    for customer in customers:
        customers_instance_list.append(
            Customer(customer["name"], customer["food"]))

    cinema_bar = CinemaBar()

    cinema_hall = CinemaHall(hall_number)

    cleaning_staff = Cleaner(cleaner)

    for customer_instance in customers_instance_list:
        cinema_bar.sell_product(
            customer_instance.food,
            customer_instance
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instance_list,
        cleaning_staff=cleaning_staff
    )
