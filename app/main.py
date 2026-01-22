from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie_name: str
) -> None:
    customer_objects = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie_name,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
