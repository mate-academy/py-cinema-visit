from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customer_instances = []
    for customer_info in customers:
        customer = Customer(name=customer_info["name"],
                            food=customer_info["food"])
        cinema_bar.sell_product(product=customer.food, customer=customer)
        customer_instances.append(customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
