from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    new_customers = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(
            product=new_customer.food,
            customer=new_customer,
        )
        new_customers.append(new_customer)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=new_customers,
        cleaning_staff=cleaning_staff,
    )
