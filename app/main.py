from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
# write your imports here


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customer_objects = []
    for cus in customers:
        customer = Customer(name=cus["name"], food=cus["food"])
        customer_objects.append(customer)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaning_staff)
