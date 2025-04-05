from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str
                 ) -> None:
    customers_instances = []
    for customer in customers:
        customers_instances.append(Customer(customer["name"],
                                            customer["food"]))

    cinema_bar_instances = CinemaBar()

    for person in customers_instances:
        cinema_bar_instances.sell_product(product=person.food,
                                          customer=person)

    cinemahall_instances = CinemaHall(number=hall_number)

    cleaner_instances = Cleaner(name=cleaner)

    cinemahall_instances.movie_session(movie_name=movie,
                                       customers=customers_instances,
                                       cleaning_staff=cleaner_instances)
