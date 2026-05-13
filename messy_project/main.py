from messy_project.logic import add
from messy_project.data import get_data


def main():
    """Main application entry point."""
    print("starting app")

    x = input("Enter your name: ")
    print("Hello " + x)

    result = add(5, 3)
    print("Result:", result)

    data = get_data()
    print("Data:", data)
    
if __name__ == "__main__":
    main()
