from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie_name: str,
) -> None:

    work_hall = CinemaHall(hall_number)

    work_cleaner = Cleaner(cleaner)

    work_bar = CinemaBar()

    visitor_name = []
    work_customer = []

    for customer_visit in customers:
        visitor_name.append(customer_visit["name"])
    for name_customer in visitor_name:
        for customer_visit in customers:
            if name_customer == customer_visit["name"]:
                name_customer = Customer(
                    customer_visit["name"],
                    customer_visit["food"]
                )
                work_customer.append(name_customer)
                work_bar.sell_product(name_customer, name_customer.food)

    work_hall.movie_session(movie_name, work_customer, work_cleaner)
