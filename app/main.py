from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner_name: str,
    movie_name: str
) -> None:
    customer_instances = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
        customer_instances.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner_name)

    hall.movie_session(
        movie_name=movie_name,
        customers=customer_instances,
        cleaning_staff=cleaner
    )
