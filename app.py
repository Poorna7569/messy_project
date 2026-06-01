from messy_project.logic import add_numbers
from messy_project.fruit_data import get_fruit  

def main():
    """Main application entry point."""
    print("starting app")

    x = input("Enter your name: ")
    print("Hello " + x)

    result = add_numbers(5, 3)
    print("Result:", result)

    data = get_fruit()
    print("Data:", data)
    
if __name__ == "__main__":
    main()
