from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances: list[Customer] = []

    for person in customers:
        new_customer: Customer = Customer(person["name"], person["food"])
        customer_instances.append(new_customer)
        CinemaBar.sell_product(product=new_customer.food,
                               customer=new_customer)

    hall: CinemaHall = CinemaHall(hall_number)
    cleaning_staff: Cleaner = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
