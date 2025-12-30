from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_customers = []

    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        new_customers.append(new_customer)
        (CinemaBar
         .sell_product(product=new_customer.food, customer=new_customer))

    cinema = CinemaHall(number=hall_number)

    cinema.movie_session(
        movie_name=movie,
        customers=new_customers,
        cleaning_staff=Cleaner(cleaner)
    )
