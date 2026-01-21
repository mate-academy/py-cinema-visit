from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_inst = [Customer(
        customer["name"],
        customer["food"]) for customer in customers]

    CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)

    for person in customer_inst:
        CinemaBar.sell_product(person, person.food)

    print(f'"{movie}" started in hall number {hall_number}.')
    for customer in customer_inst:
        customer.watch_movie(movie)

    print(f'"{movie}" ended.')
    cleaner_name.clean_hall(hall_number)
