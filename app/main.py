from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(customer=customer, product=customer.food)
        customers_list.append(customer)
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner)
