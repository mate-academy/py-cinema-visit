from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    """
    Simulates a cinema visit, involving customers, the cinema
    hall, and the cleaning staff.

    The function initializes customer instances and a cleaner
    instance, assigns a cinema hall, and processes the movie session.
    Each customer's food is sold using the CinemaBar, and
    the movie session is started with given details.
    This simulates a complete cinema visit experience.

    :param customers: List of dictionaries containing customer details,
        where each dictionary has keys 'name' (str) and 'food' (str)
    :type customers: list
    :param hall_number: The number of the cinema hall being used
    :type hall_number: int
    :param cleaner: Name of the cleaning staff responsible for the cinema hall
    :type cleaner: str
    :param movie: The name of the movie being played during the visit
    :type movie: str
    :return: None
    :rtype: None
    """
    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_instances.append(customer_instance)

    cleaner_instance = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie, customers=customer_instances,
                       cleaning_staff=cleaner_instance)
