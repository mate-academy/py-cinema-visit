from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cust_objects = [Customer(name=person["name"],
                    food=person["food"]) for person in customers]

    hall = CinemaHall(hall_number)

    cleaner_obj = Cleaner(cleaner)

    for customer in cust_objects:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall.movie_session(movie_name=movie, customers=cust_objects,
                       cleaning_staff=cleaner_obj)
