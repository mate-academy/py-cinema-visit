import pytest
import io

from contextlib import redirect_stdout

from app.people.cinema_staff import Cleaner


def test_cleaner_constructor():
    cleaner = Cleaner(name="James")
    assert hasattr(cleaner, "name"), (
        "Cleaner instance should have 'name' attribute"
    )
    assert cleaner.name == "James", (
        f"Value of attribute 'name' should equal to 'James' when "
        f"instance is created by 'Cleaner(name='James)'"
    )


def test_cleaner_clean_hall():
    name = "Anatoly"
    cleaner = Cleaner(name=name)
    hall_number = 9
    f = io.StringIO()

    with redirect_stdout(f):
        cleaner.clean_hall(hall_number=hall_number)

    out = f.getvalue()
    output = "Cleaner Anatoly is cleaning hall number 9.\n"
    assert out == output, (
        f"'clean_hall' output should equal to {output}, "
        f"when cleaner's 'name' equals to {name} and 'hall_number' equals to {hall_number}"
    )