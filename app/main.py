from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_objs = []

    for customer in customers:
        cust = Customer(name=customer["name"], food=customer["food"])
        customers_objs.append(cust)

    for cust in customers_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(
        movie=movie, customers=customers_objs, cleaning_staff=cleaner_obj)
