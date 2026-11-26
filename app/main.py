from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    instances_customers = []
    for customer in customers:
        customer = Customer(name=customer["name"],
                            food=customer["food"])
        CinemaBar.sell_product(customer=customer,
                               product=customer.food)
        instances_customers.append(customer)
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie, instances_customers, cleaning_staff)
