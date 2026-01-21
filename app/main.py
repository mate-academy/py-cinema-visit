from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner_instances = Cleaner(cleaner)
    customer_instances = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"], food=customer_data["food"]
        )
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)
        hall.movie_session(
            movie_name=movie,
            customers=customer_instances,
            cleaning_staff=cleaner_instances
        )
