"""
In the module main.py you have to import all this classes. Classes should be
 imported by absolute path, that starts with 'app.' with keyword 'from'. Write
 a function cinema_visit that takes movie_name, customers - a list of
 customers, elements are dicts with 'name' and desired 'food' of a customer,
 hall_number - number of the hall in cinema, cleaning_staff - name of the
 cleaner, that will clean the hall after movie session.

This function should make Customers instances, instance of CinemaHall
and CinemaBar, instance of Cleaner. First, cinema bar should sell food
to customers, then cinema hall should make a movie session and finally
cleaner cleans cinema hall.

Example:

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(
    customers=customers,
    hall_number=5,
    cleaner="Anna",
    movie="Madagascar"
)

    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.
"""


from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    visitors = [
        Customer(visitor["name"], visitor["food"]) for visitor in customers
    ]
    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)
    cinema_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, visitors, hall_cleaner)
