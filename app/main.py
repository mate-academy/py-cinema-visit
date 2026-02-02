# write your imports here
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
    # write you code here
    customers_info = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        customers_info.append(new_customer)

        CinemaBar.sell_product(
            customer=new_customer,
            product=new_customer.food
        )

    staff = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_info,
        cleaning_staff=staff
    )
