from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_object = []
    for i in customers:
        customer_object.append(Customer(name=i["name"], food=i["food"]))
    cleaning_staff = Cleaner(name=cleaner)
    for customer in customer_object:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_object,
        cleaning_staff=cleaning_staff
    )
