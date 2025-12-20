from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, number: int, cleaner: str, movie: str) \
        -> None:
    # 1. Create instances of Customer
    customer_instances = []
    for customer_data in customers:
        customer_instances.append(
            Customer(name=customer_data["name"], food=customer_data["food"])
        )

    # 2. Create instance of CinemaHall
    hall = CinemaHall(number=number)

    # 3. Create instance of Cleaner
    cleaner_instance = Cleaner(name=cleaner)

    # 4. Cinema Bar sells food (using static method without instance)
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # 5. Run the movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
