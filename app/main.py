from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_ins = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall_ins = CinemaHall(hall_number)
    bar_ins = CinemaBar()
    cleaner_ins = Cleaner(cleaner)

    for customer in customer_ins:
        bar_ins.sell_product(product=customer.food, customer=customer)

    hall_ins.movie_session(
        movie_name=movie, customers=customer_ins, cleaning_staff=cleaner_ins
    )
