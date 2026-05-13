import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import add, subtract


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5


def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
