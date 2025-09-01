from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_list = []

    for customer in customers:
        current_customer = Customer(
            name=customer["name"], food=customer["food"])
        customers_list.append(current_customer)

        CinemaBar.sell_product(
            product=current_customer.food, customer=current_customer)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_staff)
