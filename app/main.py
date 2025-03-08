from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances_list = []
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(name=cleaner)
    for customer_dict in customers:
        customer_instance = Customer(name=customer_dict["name"],
                                     food=customer_dict["food"])
        customers_instances_list.append(customer_instance)
        cinema_bar.sell_product(product=customer_instance.food,
                                customer=customer_instance)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_instances_list,
                              cleaning_staff=cleaner_instance)
