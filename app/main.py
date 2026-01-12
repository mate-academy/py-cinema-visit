from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_intances = []
    for customer_data in customers:
        customer_item = Customer(name=customer_data["name"],
                                 food=customer_data["food"])
        customer_intances.append(customer_item)
    hall_intance = CinemaHall(number=hall_number)
    cleaner_intance = Cleaner(name=cleaner)

    for customer in customer_intances:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall_intance.movie_session(
        movie_name=movie,
        customers=customer_intances,
        cleaning_staff=cleaner_intance)
