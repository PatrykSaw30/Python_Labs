TASK01
def sing_up(**kwargs):
    if check_is_password_correct(kwargs[userName]):
        print("You create new account!")

def check_is_password_correct(pas):
    if len(pas) > 8 or len(pas) < 4:
        print("Password must be at least 8 characters long!")
        return False
    else:
        for letter in password:
            if letter.isalpha() or letter.isupper() or letter.isdigit():
                return True
            else:
                print("Password is not correct.")
                return False


userName = str(input("Enter your username: "))
password = str(input("Enter your password: "))

data = {userName: password}
sing_up(**data)

-------------------------------------------------------
TASK02
import pickle

def find_numbers(x=1, y=1):

    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('x must be an integer')

    if x > y:
        x, y = y, x

    result = [num for num in range(x, y + 1) if num % 7 == 0 and num % 5 != 0]
    return result

def save_to_pickle(data, filename = "result.pkl"):
    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    try:
        x = int(input("Enter x number: "))
        y = int(input("Enter y number: "))

        numbers = find_numbers(x, y)

        print(", ".join(map(str, numbers)))

        save_to_pickle(numbers)

    except ValueError as ve:
        print(f"Input error {ve}")
    except Exception as e:
        print(f"Type error {e}")

if __name__ == "__main__":
    main()
----------------------------------------
TASK03
from math import *


def multiple_arguments(*args):
    if len(args) > 100:
        raise ValueError("Too many arguments")

    for x in args:
        if not isinstance(x, int):
            raise TypeError("Argument must be an integer")


    result = [pow(x,2) for x in args]
    return result

userInput = str(input("Enter comma-separated numbers: "))

try:
    numbers = [int(x.strip()) for x in userInput.split(",") if x.strip()]
    output = multiple_arguments(*numbers)
    print(*output)
except ValueError:
    print("Error: Please enter valid numbers.")



