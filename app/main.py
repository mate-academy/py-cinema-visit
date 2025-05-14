from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    cinema_hall = CinemaHall(number=hall_number)
    cleaning_person = Cleaner(name=cleaner)

    customer_objects = []
    for person in customers:
        customer_obj = Customer(name=person["name"], food=person["food"])
        customer_objects.append(customer_obj)

        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_person
    )
