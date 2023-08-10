from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner_name: str,
                 movie_name: str) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(cleaner_name)

    customers_list = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data.get("food"))
        customers_list.append(customer)
        if customer.food is not None:
            CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customers_list,
                              cleaning_staff=cleaner)
