from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_objects = []

    for customer_dict in customers:
        customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
