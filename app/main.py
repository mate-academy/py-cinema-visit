from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers,
    hall_number,
    cleaner,
    movie,
):
    customer_list = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"],
        )

        customer_list.append(customer_instance)

        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance,
        )

    cleaner_instance = Cleaner(
        name=cleaner,
    )

    hall = CinemaHall(
        number=hall_number,
    )

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_instance,
    )
