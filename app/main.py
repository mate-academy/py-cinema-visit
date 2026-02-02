from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []

    for customer in customers:
        customers_list.append(Customer(
            name=customer["name"],
            food=customer["food"]))

    for customer in customers_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)

    hall.movie_session(movie, customers_list, staff)
