from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objs = []
    for customer in customers:
        cust = Customer(name=customer.get("name"),
                 food=customer.get("food"),)
        customer_objs.append(cust)

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_objs,
                       cleaning_staff=Cleaner(name=cleaner))
