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
    customers_list = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"], food=customer_data["food"]
        )
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customers_list.append(customer)

    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_list,
                              cleaning_staff=Cleaner(name=cleaner))
