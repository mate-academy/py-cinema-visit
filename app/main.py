from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str,
                 ) -> None:
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(hall_number)

    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
