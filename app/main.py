from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cleaner_obj = Cleaner(name=cleaner)

    customer_objects = []
    for cst_data in customers:
        customer_obj = Customer(
            name=cst_data["name"],
            food=cst_data["food"]
        )
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
