from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_instances = []
    for customer_dict in customers:
        created_customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        CinemaBar.sell_product(
            product=created_customer.food,
            customer=created_customer
        )
        customer_instances.append(created_customer)

    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
