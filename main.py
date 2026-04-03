from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str) -> None:
    customer_instances = []

    for c_data in customers:
        new_customer = Customer(name=c_data["name"], food=c_data["food"])
        customer_instances.append(new_customer)
        CinemaBar.sell_product(
            product=new_customer.food,
            customer=new_customer
        )

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
