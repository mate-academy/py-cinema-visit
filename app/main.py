def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    """
    Simulates a cinema visit scenario and prints the sequence of events.

    Args:
        customers: List of dictionaries with keys 'name' and 'food'
        hall_number: Number of the cinema hall
        cleaner: Name of the cleaning staff
        movie: Title of the movie being shown
    """
    for customer in customers:
        print(f"Cinema bar sold {customer['food']} to {customer['name']}.")

    print(f'"{movie}" started in hall number {hall_number}.')

    for customer in customers:
        print(f'{customer["name"]} is watching "{movie}".')

    print(f'"{movie}" ended.')

    print(f'Cleaner {cleaner} is cleaning hall number {hall_number}.')

