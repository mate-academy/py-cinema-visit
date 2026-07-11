from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
):

    customer_instances = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )

        customer_instances.append(customer_instance)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
