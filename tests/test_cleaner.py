from app.cleaner import Cleaner

def test_cleaner_clean_hall():
    cleaner = Cleaner("Anatoly")
    cleaner.clean_hall(9)