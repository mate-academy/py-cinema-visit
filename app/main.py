from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaning_staff)
