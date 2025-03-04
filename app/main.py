from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int, cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)

    session_customers = []
    for customer_data in customers:
        session_customers.append(Customer(name=customer_data["name"],
                                          food=customer_data["food"]))

    cinema_hall.movie_session(movie_name=movie,
                              customers=session_customers,
                              cleaning_staff=cleaner_instance)
