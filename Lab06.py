TASK01
import math

def calculator():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        assert second_number != 0, "Second number must be entered"
        result = first_number + second_number
        print(f"Result of {first_number} / {second_number}: {result}")

        assert first_number > 0, "first_number must be greater than 0"
        result = math.sqrt(first_number)
        print(f"Result of sqrt({first_number}) : {result}")

    except ValueError:
        print("Please enter a number!")
    except ZeroDivisionError:
        print("Second number must be entered!")
    except TypeError:
        print("Please enter a number!")
    except AssertionError as e:
        print(f"Logical error: {e}")
    except Exception as e:
        print(f"Something went wrong! {e}")

calculator()
task02
import pandas as pd
import pickle

file_name = "richest_movie"
folder_path = "D:\\python-labs\\6-python-lab\\task2\\movies.csv"

def find_and_save_richest_bw_movie(csv_path, pickle_path):
    try:
        data = pd.read_csv(csv_path, encoding='utf-8')
        dfs = pd.DataFrame(data)
        baw_movies = dfs[dfs['color'] == " Black and White"]
        richest_movies = baw_movies.loc[baw_movies['budget'].idxmax()]
        movie_title = richest_movies["movie_title"]
        print(f'Black and white film with biggest budget: {movie_title}')

        with open(pickle_path, "wb") as file:
            pickle.dump(data, file)
        print("Data has been saved in file!")

    except FileNotFoundError:
        print("File not found!")
    except KeyError:
        print("Something went wrong!")
    except Exception as e:
        print(e)
task03
import re
import math

def licz(fun):
    fun = fun.replace(' ', '')
    pattern = r'([+-]?\d*\.?\d*)x\^2|([+-]?\d*\.?\d*)x|([+-]?\d+\.?\d*)'
    matches = re.findall(pattern, fun)

    a, b, c = 0.0, 0.0, 0.0

    for m_a, m_b, m_c in matches:
        if m_a:
            if m_a in ('', '+'):
                a = 1.0
            elif m_a == '-':
                a = -1.0
            else:
                a = float(m_a)
        elif m_b:
            if m_b in ('', '+'):
                b = 1.0
            elif m_b == '-':
                b = -1.0
            else:
                b = float(m_b)
        elif m_c:  # Wyraz wolny
            c = float(m_c)

    if a == 0:
        raise ValueError("To nie jest równanie kwadratowe (a = 0).")

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return round(x, 2)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return sorted([round(x1, 2), round(x2, 2)], reverse=True)

wynik = licz('x^2+4x-21')
try:
    assert wynik == [3.0, -7.0], f"Błąd! Oczekiwano [3.0, -7.0], otrzymano {wynik}"
    print(f"Test zaliczony! Pierwiastki równania x^2+4x-21 to: {wynik}")
except AssertionError as e:
    print(e)
find_and_save_richest_bw_movie(folder_path, file_name)
