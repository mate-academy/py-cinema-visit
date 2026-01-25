from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    instances_customers = []
    for customers_data in customers:
        customer = Customer(name=customers_data["name"],
                            food=customers_data["food"])
        CinemaBar.sell_product(customer=customer,
                               product=customer.food)
        instances_customers.append(customer)
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie, instances_customers, cleaning_staff)
