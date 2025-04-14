from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:

    customer_instances = [Customer(i["name"], i["food"])for i in customers]

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cleaner = Cleaner(cleaner_name)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_instances, cleaning_staff=cleaner)
