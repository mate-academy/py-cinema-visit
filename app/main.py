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
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food
        )

    hall_customers = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]
    cleaning_staff = Cleaner(name=cleaner)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=hall_customers,
        cleaning_staff=cleaning_staff
    )
