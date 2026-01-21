from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []
    for customer in customers:
        customer_food = Customer(
            name=customer["name"], food=customer["food"]
        )
        CinemaBar.sell_product(
            customer=customer_food, product=customer_food.food
        )

        customer_list.append(customer_food)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie, customers=customer_list, cleaning_staff=cleaner
    )
