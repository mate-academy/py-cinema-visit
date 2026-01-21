from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = []
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()

    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        customers_list.append(customer)

        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
