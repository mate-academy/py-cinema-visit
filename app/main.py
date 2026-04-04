from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_list = []

    for cust in customers:
        customer = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customers_list.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_staff)
