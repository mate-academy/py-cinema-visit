from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    clr = Cleaner(cleaner)
    customers_list = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    CinemaHall.movie_session(
        cinema_hall,
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=clr
    )
