from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    cinema_customers = []

    for customer in customers:
        new_customer = Customer(
            name=customer["name"],
            food=customer["food"],
        )
        CinemaBar.sell_product(
            product=new_customer.food,
            customer=new_customer,
        )
        cinema_customers.append(new_customer)

    hall.movie_session(
        movie_name=movie,
        customers=cinema_customers,
        cleaning_staff=cleaning_staff,
    )
