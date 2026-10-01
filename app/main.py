from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_instances = []
    for cust in customers:
        customer_obj = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(product=cust["food"], customer=customer_obj)
        customer_instances.append(customer_obj)
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
