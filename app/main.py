from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(name=customer_data["name"],
                                     food=customer_data["food"])
        CinemaBar.sell_product(product=customer_instance.food,
                               customer=customer_instance)
        customer_instances.append(customer_instance)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instances,
                              cleaning_staff=cleaner_staff)
