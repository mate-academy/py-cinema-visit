from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects = []
    for customer in customers:
        new_customer = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customer_objects.append(new_customer)

    for new_customer in customer_objects:
        CinemaBar.sell_product(
            product=new_customer.food,
            customer=new_customer
        )

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
