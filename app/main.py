from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        movie: str,
        customers: list[dict],
        hall_number: int,
        cleaner: str) -> None:
    list_of_instances = []
    for custus in customers:
        list_of_instances.append(Customer(name=custus["name"],
                                          food=custus["food"]))
    cinema_hall_inst = CinemaHall(number=hall_number)
    cleaner_inst = Cleaner(name=cleaner)
    for inst in list_of_instances:
        CinemaBar.sell_product(customer=inst,
                               product=inst.food)
    cinema_hall_inst.movie_session(movie_name=movie,
                                   customers=list_of_instances,
                                   cleaning_staff=cleaner_inst)
