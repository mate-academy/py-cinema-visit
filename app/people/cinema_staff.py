class Cleaner:
    """Class describes cinema's cleaner"""
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Method prints cleaner's name and hall number"""
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
