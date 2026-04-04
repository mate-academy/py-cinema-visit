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
    customer_objects = []

    for cust_dict in customers:
        customer_obj = Customer(
            name=cust_dict["name"],
            food=cust_dict["food"]
        )
        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj
        )
        customer_objects.append(customer_obj)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
