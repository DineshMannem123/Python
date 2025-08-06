# Modern Python Code (Python 3.10+)

from datetime import datetime
from typing import Union

def get_greeting(hour: int) -> str:
    match hour:
        case h if 5 <= h < 12:
            return "Good morning!"
        case h if 12 <= h < 17:
            return "Good afternoon!"
        case h if 17 <= h < 21:
            return "Good evening!"
        case _:
            return "Good night!"

def check_age(age: int) -> str:
    match age:
        case a if a >= 18:
            return "You are an adult."
        case a if 13 <= a < 18:
            return "You are a teenager."
        case _:
            return "You are a child."

def main() -> None:
    name: str = input("Enter your name: ")
    age_input: str = input("Enter your age: ")

    if not age_input.isdigit():
        print("Invalid age. Please enter a number.")
        return

    age: int = int(age_input)
    current_hour: int = datetime.now().hour

    print(f"\nHello, {name}!")
    print(get_greeting(current_hour))
    print(check_age(age))

    print("\nCountdown from 5 to 1:")
    for i in reversed(range(1, 6)):
        print(i)

if __name__ == "__main__":
    main()
