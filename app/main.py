from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    for person in customers:
        one_customer = Customer(
            name=person["name"],
            food=person["food"]
        )
        list_of_customers.append(one_customer)
        CinemaBar.sell_product(one_customer, one_customer.food)

    staff_cleaner = Cleaner(cleaner)

    current_hall = CinemaHall(hall_number)

    CinemaHall.movie_session(
        current_hall,
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=staff_cleaner
    )
