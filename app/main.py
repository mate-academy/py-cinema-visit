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
    customer_instances = []
    for customer_data in customers:
        new_customer = Customer(
            customer_data["name"],
            customer_data["food"]
        )
        customer_instances.append(new_customer)
        CinemaBar.sell_product(new_customer.food, new_customer)

    staff_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customer_instances, staff_cleaner)
