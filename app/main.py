from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customer_instances.append(new_customer)

        CinemaBar.sell_product(customer=new_customer,
                               product=new_customer.food)

    staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=staff)
