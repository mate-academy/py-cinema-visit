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
    sorted_customers = []

    for cust in customers:
        customer_obj = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(customer=customer_obj,
                               product=customer_obj.food)
        sorted_customers.append(customer_obj)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=sorted_customers,
        cleaning_staff=cleaner_obj
    )
