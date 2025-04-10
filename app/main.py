from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie: str) -> None:
    customers_list = []

    for customer in customers:
        customers_list.append(
            Customer(
                name=customer.get("name"),
                food=customer.get("food")
            )
        )

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(cleaner_name)

    hall.movie_session(movie, customers_list, cleaner)
