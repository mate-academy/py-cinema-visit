from app.people.cinema_staff import Cleaner
from typing import List


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def start_movie(
        self,
        movie_name: str,
        customers: List[str],
        cleaning_staff: List[Cleaner]
    ) -> str:
        customer_list = ", ".join(customers)
        staff_list = ", ".join([staff.name for staff in cleaning_staff])
        return (
            f"Starting '{movie_name}' in hall {self.hall_number}.\n"
            f"Customers: {customer_list}\n"
            f"Cleaning staff: {staff_list}"
        )
