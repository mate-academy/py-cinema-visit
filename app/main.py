from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_objects = []
    for person in customers:
        new_customer = Customer(name=person["name"], food=person["food"])
        customer_objects.append(new_customer)

    hall = CinemaHall(number=hall_number)
    cleaner_person = Cleaner(name=cleaner)
    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_person,
    )
