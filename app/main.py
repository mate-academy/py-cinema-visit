from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_list = []

    for customer_dict in customers:
        new_customer = Customer(
            name=customer_dict["name"],
            food=customer_dict["food"]
        )
        customer_list.append(new_customer)

    for customer in customer_list:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food
        )

    hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_staff
    )