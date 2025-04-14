from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

# **Absolute Import**:
#    - Imports a module or object by specifying its full path
#       from the project or package root.
#    - Example:
#      ```
#      import my_project.module.submodule
#      from my_project.module import some_function


def cinema_visit(
        customers: list,
        number: int,
        cleaner: Cleaner,
        movie: str
) -> None:
    cleaner_instance = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number)

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**customer_data) for customer_data in customers],
        cleaning_staff=cleaner_instance)
