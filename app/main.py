from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:

    customer_list = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_person = Cleaner(cleaning_staff)

    for customer in customer_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customer_list,
        cleaning_staff=cleaner_person
    )
