from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.bar import CinemaBar
from app.hall import CinemaHall


def cinema_visit(
  movie: str, customers: list, hall_number: int, cleaner: str
) -> None:
    customer_objs = [
      Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cleaner_obj = Cleaner(name=cleaner)

    for cust in customer_objs:
        CinemaBar.sell_product(customer=cust, product=cust.food)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
      movie_name=movie, customers=customer_objs, cleaning_staff=cleaner_obj
    )
