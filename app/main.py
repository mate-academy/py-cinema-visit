from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    hall_num = CinemaHall(hall_number)

    cleaner_for_this_hall = Cleaner(cleaner)

    customer_objects = []

    for customer in customers:
        cust, food = customer["name"], customer["food"]
        cust = Customer(cust, food)
        CinemaBar.sell_product(customer=cust, product=food)
        customer_objects.append(cust)

    hall_num.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_for_this_hall
    )
