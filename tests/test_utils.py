from messy_project.logic import add_numbers, subtract_numbers


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5


def test_subtract_numbers():
    """Test the subtract_numbers function."""
    assert subtract_numbers(5, 3) == 2
