from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # Create Customer instances
    customer_instances = [
        Customer(
            name=customer["name"],
            food=customer["food"]) for customer in customers]

    # Create Cleaner instance
    cleaner_instance = Cleaner(name=cleaner)

    # Sell food to customers
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create CinemaHall instance and start the movie session
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance)


# Example usage (you can test with this code snippet)
if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name,
        movie=movie)
