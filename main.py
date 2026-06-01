from typing import Optional

from messy_project.logic import add_numbers
from messy_project.fruit_data import get_fruit


def get_user_name(prompt: str = "Enter your name: ") -> str:
    """Read and return the user's name (wrapper around input for testability)."""
    return input(prompt).strip()


def print_greeting(name: str) -> None:
    """Print a greeting for the provided name."""
    print(f"Hello {name}")


def main(argv: Optional[list] = None) -> None:
    """Main application entry point: orchestrates I/O and business functions."""
    print("starting app")

    name = get_user_name()
    print_greeting(name)

    result = add_numbers(5, 3)
    print("Result:", result)

    data = get_fruit()
    print("Data:", data)


if __name__ == "__main__":
    main()
