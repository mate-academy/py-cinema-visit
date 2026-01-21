from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    cb = CinemaBar()
    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaning_staff)

    cinema_customers = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        cb.sell_product(product=customer.food, customer=customer)
        cinema_customers.append(customer)
    hall.movie_session(movie_name=movie_name,
                       customers=cinema_customers,
                       cleaning_staff=cleaner)
