from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str):
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(
            name=customer["name"],
            food=customer["food"]
        ))

    cinema_hall = CinemaHall(hall_number)

    cleaner = Cleaner(cleaning_staff)

    for customer in customers_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customers_list,
        cleaning_staff=cleaner
    )
