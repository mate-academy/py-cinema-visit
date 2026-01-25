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

    customers_in = customers
    created_customers = []
    for customer_in in customers_in:
        new_customer = Customer(
            name=customer_in["name"], food=customer_in["food"]
        )
        CinemaBar.sell_product(
            product=customer_in["food"], customer=new_customer
        )
        created_customers.append(new_customer)
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=created_customers,
        cleaning_staff=cleaner_obj
    )
