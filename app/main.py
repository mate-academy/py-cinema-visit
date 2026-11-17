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
    customer_objects = []
    for customer_dict in customers:
        customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        customer_objects.append(customer)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
