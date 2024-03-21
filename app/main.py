from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers_list: list, hall_number: int, cleaner_name: str, movie_name: str
) -> None:
    for customer_data in customers_list:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # Create Cleaner instance
    cleaning_staff = Cleaner(name=cleaner_name)

    # Create CinemaHall instance
    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=[
            Customer(name=customer_data["name"], food=customer_data["food"])
            for customer_data in customers_list
        ],
        cleaning_staff=cleaning_staff
    )
