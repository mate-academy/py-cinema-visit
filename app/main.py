from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_instances = []

    for person in customers:
        new_customer = Customer(name=person["name"], food=person["food"])
        customer_instances.append(new_customer)

        CinemaBar.sell_product(
            product=new_customer.food, customer=new_customer
        )

    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie, customers=customer_instances, cleaning_staff=staff
    )
