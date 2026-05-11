import os
import shutil
import pickle


# ========================= TASK 0 =========================

def divisible_numbers(x, y):
    result = []

    for i in range(x, y + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))

    print(",".join(result))


divisible_numbers(1000, 2101)


# ========================= TASK 1 =========================

def check_password(password):

    lower = False
    upper = False
    digit = False

    for char in password:

        if char.islower():
            lower = True

        elif char.isupper():
            upper = True

        elif char.isdigit():
            digit = True

    if lower and upper and digit and 4 <= len(password) <= 8:
        result = "Valid password"
    else:
        result = "Invalid password"

    with open("password_result.txt", "w") as f:
        f.write(result)

    return result


print(check_password("Abc1"))


# ========================= TASK 2 =========================

def divisible_numbers_pickle(x, y):

    result = []

    try:

        for i in range(x, y + 1):

            if i % 7 == 0 and i % 5 != 0:
                result.append(i)

        with open("numbers.pkl", "wb") as f:
            pickle.dump(result, f)

        print(result)

    except Exception as e:
        print("Error:", e)


divisible_numbers_pickle(1000, 2101)


# ========================= TASK 3 =========================

def powers(*args):

    if len(args) > 100:
        return "Error: too many arguments"

    result = []

    for x in args:
        result.append(x ** x)

    return result


print(powers(2))
print(powers(2, 3))
print(powers(2, 3, 4))


# ========================= TASK 4 =========================

def dynamic_powers(**kwargs):

    try:

        if len(kwargs) > 100:
            return "Error: too many arguments"

        result = {}

        for key, value in kwargs.items():
            result[key] = value ** value

        return result

    except Exception as e:
        print("Error:", e)


print(dynamic_powers(x1=2, x2=3, x3=4))


# ========================= TASK 5 =========================

folder_name = "DocumentLab5"

os.makedirs(folder_name, exist_ok=True)

tekst = """
Python is a very popular programming language.
Students learn functions and decorators during laboratory classes.
This file contains several example sentences for testing.
Programming requires patience and systematic learning.
Functions may accept variable number of arguments.
"""

files = [
    "Text1ID_ABC.txt",
    "Text2ID_405.txt",
    "Text3ID_607.txt",
    "Text4ID_ABC5.txt",
    "Text5ID_DEF.txt"
]

for file in files:

    with open(os.path.join(folder_name, file), "w", encoding="utf-8") as f:
        f.write(tekst)


def decorator_function(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        folder = args[0]

        zero_counter = 0

        copy_folder = "DocumentLab5copy"

        os.makedirs(copy_folder, exist_ok=True)

        for filename in os.listdir(folder):

            filepath = os.path.join(folder, filename)

            if "0" in filename:

                zero_counter += 1

                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()

                words = text.split()

                print(f"\nPlik z cyfrą 0: {filename}")
                print(f"Liczba słów: {len(words)}")

            if "EF.txt" in filename:

                destination = os.path.join(copy_folder, filename)

                shutil.copy(filepath, destination)

                print(f"\nSkopiowano plik: {filename}")

        print(f"\nLiczba plików zawierających 0: {zero_counter}")

        return result

    return wrapper


@decorator_function
def analyze_files(folder_path, *args):

    for filename in os.listdir(folder_path):

        print(filename)

        filepath = os.path.join(folder_path, filename)

        if "ABC" in filename:

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            words = text.split()

            long_words = [word for word in words if len(word) > 3]

            print(f"\nPlik: {filename}")
            print(f"Liczba słów > 3 litery: {len(long_words)}")


analyze_files(folder_name)
