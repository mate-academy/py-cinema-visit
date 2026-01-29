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

    customer_instances = []
    for customer_input in customers:
        customer = Customer(name=customer_input["name"],
                            food=customer_input["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaner_inst = Cleaner(cleaner)

    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=cleaner_inst)
