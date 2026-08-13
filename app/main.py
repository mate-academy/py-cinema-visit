
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        customer_list.append(customer)

    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food , customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaning_staff
    )
