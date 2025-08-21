import pytest
import io

from contextlib import redirect_stdout

from app.main import cinema_visit

@pytest.mark.parametrize(
    "customers,hall_number,cleaner,movie,output",
    [
        (
            [
                {"name": "Bob", "food": "popcorn"}
            ],
            1,
            "Anna",
            "Tenet",
            'Cinema bar sold popcorn to Bob.\n'
            '"Tenet" started in hall number 1.\n'
            'Bob is watching "Tenet".\n'
            '"Tenet" ended.\n'
            'Cleaner Anna is cleaning hall number 1.\n'

        ),
        (
            [
                {"name": "Bob", "food": "Coca-cola"},
                {"name": "Alex", "food": "popcorn"}
            ],
            5,
            "Anna",
            "Madagascar",
            'Cinema bar sold Coca-cola to Bob.\n'
            'Cinema bar sold popcorn to Alex.\n'
            '"Madagascar" started in hall number 5.\n'
            'Bob is watching "Madagascar".\n'
            'Alex is watching "Madagascar".\n'
            '"Madagascar" ended.\n'
            'Cleaner Anna is cleaning hall number 5.\n'
        ),
        (
            [
                {"name": "Susan", "food": "Pepsi"},
                {"name": "Michael", "food": "Coca-cola"},
                {"name": "Monica", "food": "popcorn"}
            ],
            3,
            "Vasiliy",
            "Interstellar",
            'Cinema bar sold Pepsi to Susan.\n'
            'Cinema bar sold Coca-cola to Michael.\n'
            'Cinema bar sold popcorn to Monica.\n'
            '"Interstellar" started in hall number 3.\n'
            'Susan is watching "Interstellar".\n'
            'Michael is watching "Interstellar".\n'
            'Monica is watching "Interstellar".\n'
            '"Interstellar" ended.\n'
            'Cleaner Vasiliy is cleaning hall number 3.\n'
        )
    ]
)
def test_cinema_visit(customers, hall_number, cleaner, movie, output):
    f = io.StringIO()

    with redirect_stdout(f):
        cinema_visit(customers, hall_number, cleaner, movie)

    out = f.getvalue()

    assert out == output, (
        f"When 'customers' equals to {customers}, "
        f"'hall_number' equals to {hall_number}. "
        f"'cleaner' equals to {cleaner}, "
        f"and 'movie' equals to {movie}, "
        f"'cinema_visit' output should equal to {output}"
    )
