class Cleaner:
    def __init__(self: 'Cleaner', name: str = 'Cleaner') -> None:
        self.name: str = name

    def clean(self: 'Cleaner', hall: object) -> str:
        return f'{self.name} cleaned {getattr(hall, "name", "hall")}'

    def clean_hall(self: 'Cleaner', hall_number: int) -> None:
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
