from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: str,
                 hall_number: str, cleaner: str) -> None:
    customer_objects = []

    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
