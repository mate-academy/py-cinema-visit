from app.cinema.bar import CinemaBar  # noqa: F401
from app.cinema.hall import CinemaHall  # noqa: F401
from app.people.customer import Customer  # noqa: F401
from app.people.cinema_staff import Cleaner  # noqa: F401
from app.cinema_visit import cinema_visit

if __name__ == "__main__":
    cinema_visit(
        customers=[{"name": "Bob", "food": "popcorn"}],
        hall_number=1,
        cleaner_name="Anna",
        movie="Tenet",
    )
