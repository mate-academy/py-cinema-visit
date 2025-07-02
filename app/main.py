from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_objs = []
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        customer_objs.append(customer)

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj)
