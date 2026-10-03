from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(name=customer["name"],
                                      food=customer["food"]))
    cinema_hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer_instance in customer_list:
        CinemaBar.sell_product(customer=customer_instance,
                               product=customer_instance.food)
    cinema_hall_instance.movie_session(movie_name=movie,
                                       customers=customer_list,
                                       cleaning_staff=cleaner_instance)
