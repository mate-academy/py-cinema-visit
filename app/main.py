# write your imports here
from typing import List, Dict


def cinema_visit(
    customers: List[str],
    hall_number: int,
    cleaner: str,
    movie: str
) -> Dict:
    visit_info = {
        "hall": hall_number,
        "movie": movie,
        "customers": customers,
        "cleaner": cleaner
    }

    print("Cinema Visit Report")
    print("-------------------")
    print(f"Hall Number: {hall_number}")
    print(f"Movie: {movie}")
    print(f'Customers: {", ".join(customers)}')
    print(f"Cleaner: {cleaner}")

    return visit_info
