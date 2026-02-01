from cinema.app.bar import CinemaBar
from cinema.app.hall import CinemaHall
from cinema.people.customer import Customer
from cinema.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list[dict],
    hall_number: int,
    cleaner: str,
) -> None:
    # NÃO crie instância de CinemaBar - use o método estático diretamente
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    customer_instances: list[Customer] = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        customer_instances.append(customer)
        # Chame o método estático diretamente da classe CinemaBar
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )