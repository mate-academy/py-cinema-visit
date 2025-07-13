from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, number: int, cleaner: str,
    # write you code here
                 movie: str) -> None:
    pass
    customer_objects = []
    for customer_data in customers:
        name = customer_data["name"]
        food = customer_data["food"]
        customer = Customer(name=name, food=food)
        CinemaBar.sell_product(product=food, customer=customer)
        customer_objects.append(customer)

    hall = CinemaHall(number=number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie, customers=customer_objects,
        cleaning_staff=cleaning_staff
    )