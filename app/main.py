from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, number: int, cleaner: str,
                 movie: str) -> None:
    customer_objects = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        customer_objects.append(customer)

    cleaning_staff = Cleaner(cleaner)

    hall = CinemaHall(number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
