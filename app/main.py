from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie: str, customers: list,
                 hall_number: int, cleaner: str) -> None:

    customers_obj = []
    for data in customers:
        customer_instance = Customer(name=data["name"], food=data["food"])
        CinemaBar.sell_product(customer=customer_instance,
                               product=customer_instance.food)
        customers_obj.append(customer_instance)
    hall = CinemaHall(hall_number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    hall.movie_session(movie, customers_obj, cleaner_instance)
