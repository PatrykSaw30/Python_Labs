import os
########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.
import os

def change_and_show_catalog(string):
    try:
        os.chdir(string)
        print(f"✅ The directory has been successfully changed to: {os.getcwd()}")

        value = os.listdir()

        print("\nContents of the directory:")
        if not value:
            print("Directory is empty!")
        else:
            for element in value:
                print(f" ├── {element}")

    except FileNotFoundError:
        print(f"❌ Error: Directory '{string}' is not founded.")
    except PermissionError:
        print(f"❌ Error: No access permissions to the directory '{string}'.")
    except NotADirectoryError:
        print(f"❌ Error: '{string}' this is file not directory.")
    except Exception as e:
        print(f"❌ Error: {e}")

change_and_show_catalog("D:\\")

# path = input("Podaj sciezke: ")
# change(path)


########################## Zadanie 2 #########################
## Korzystając z utworzonej funkcji napisz funkcję która będzie zmieniała bieżący katalog
## dyskowy na inny wskazany przez użytkownika oraz będzie wyświetlała zawartość wskazanego przez
## użytkownika katalogu.
## Przetestuj działanie programu dla natepującego przypadku:
## program działa tylko wówczas gdy użytkownik odpowie "yes" na pytanie:
## "Czy mam zmienić katalog?", zastosuj pętle while True(zmuś użytkownika :) do wpisania "yes")
import os


def zmien_i_wyswietl_katalog(sciezka):
    try:
        os.chdir(sciezka)
        print(f"\n✅ Pomyślnie zmieniono katalog na: {os.getcwd()}")

        zawartosc = os.listdir()
        print("Zawartość katalogu:")
        if not zawartosc:
            print(" └── Katalog jest pusty.")
        else:
            for element in zawartosc:
                print(f" ├── {element}")

    except FileNotFoundError:
        print(f"❌ Błąd: Katalog '{sciezka}' nie istnieje.")
    except PermissionError:
        print(f"❌ Błąd: Brak uprawnień dostępu.")
    except NotADirectoryError:
        print(f"❌ Błąd: Ścieżka '{sciezka}' nie jest katalogiem.")
    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")


def uruchom_interfejs():
    print("--- Start programu ---")
    while True:
        odpowiedz = input("Czy mam zmienić katalog? (Wpisz 'yes'): ")

        if odpowiedz.strip().lower() == "yes":
            print("Super! Przechodzimy dalej...\n")
            nowa_sciezka = input("Podaj ścieżkę do nowego katalogu: ")
            zmien_i_wyswietl_katalog(nowa_sciezka)
            break
        else:
            print("Nie przyjmuję odmowy! Musisz wpisać 'yes' :)")

uruchom_interfejs()

# func()

########################## Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się folderze roboczym
## b) korzystając z metod Pythona i (pętli lub funkcji filter) wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym

# os.chdir("Dokument")
# files = os.listdir()
# print(files)
# for file in files:
#     if fnmatch.fnmatch(file, "*.doc"):
#         print(file)


########################## Zadanie 4 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2 katalogi:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe i graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku
import os
DIR_DOC = "StudentDoc"
DIR_PICTURE = "StudentObrazy"

os.makedirs(DIR_DOC, exist_ok=True)
os.makedirs(DIR_PICTURE, exist_ok=True)

with open(os.path.join(DIR_DOC, "note.txt"), "w", encoding="utf-8") as f:
    f.write("Something something.")

with open(os.path.join(DIR_DOC, "report.txt"), "w", encoding="utf-8") as f:
    f.write("This is report. ADNVLSNDLKVNKLSDNVKLSNDLKBVNKSDNBVSNDKLBNS DBKSDMV;ke mpoqweJ OPSKS DNLKVNSJLDvnljsdnvlkS")

with open(os.path.join(DIR_PICTURE, "schemat.png"), "wb") as f:
    f.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + b"\x00" * 44)

with open(os.path.join(DIR_PICTURE, "picture.jpg"), "wb") as f:
    f.write(b"\xff\xd8\xff\xe0\x00\x10JFIF" + b"\x1A" * 140)


def show_directory_and_size_of_files(directory):
    print(f"\n📂 Contents of directory: '{directory}'")

    files = os.listdir(directory)

    if not files:
        print(" └── Directory is empty.")
    else:
        for file in files:
            file_path = os.path.join(directory, file)
            size = os.path.getsize(file_path)

            print(f" ├── {file} | Size: {size} bytes")

show_directory_and_size_of_files(DIR_DOC)
show_directory_and_size_of_files(DIR_PICTURE)



########################## Zadanie 5 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.
import os

def create_directory(dir_name):
    try:
        os.makedirs(DIR_NAME, exist_ok=True)
        print(f"Directory {dir_name} created")
    except FileNotFoundError:
        print(f"❌ Error: Directory '{dir_name}' is not founded.")
    except Exception as e:
        print(f"❌ Error: {e}")


def rename_directory(current_dir, new_dir):
    try:
        os.rename(current_dir, new_dir)
        print(f"Directory {current_dir} renamed to {new_dir}")
    except FileNotFoundError:
        print(f"❌ Error: Directory '{current_dir}' is not founded.")
    except FileExistsError:
        print(f"❌ Error: Directory with name: '{new_dir}' is already exist.")
    except Exception as e:
        print(f"❌ Error: {e}")


DIR_NAME = str(input("Write name of directory: "))
create_directory(DIR_NAME)
new_directory_name = str(input("Write name of new directory: "))
rename_directory(DIR_NAME, new_directory_name)

########################## Zadanie 6 ########################
# # Utwórz trzy listy, zapisz, usuń a następnie odczytaj z pliku listy, użyj pickle
import pickle
import os

first_list = ["apple", "banana", "cherry"]
second_list = [10, 20, 30, 40]
third_list = ["Python", 3.13, True]

all_lists = [first_list, second_list, third_list]
file_name = "text.pkl"

try:
    with open(file_name, "wb") as file:
        pickle.dump(all_lists, file)
    print(f"Data has been saved in {file_name}")
except PermissionError:
    print(f"You cannot save data in this directory")
except Exception as e:
    print(f"Something went wrong: {e}")

del first_list, second_list, third_list, all_lists
print("Lists has been deleted from the memory!")


try:
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            loaded_lists = pickle.load(file)
        print("Data has been loaded!")

    for i, list in enumerate(loaded_lists, 1):
        print(f"{i}: {list}")
except FileNotFoundError:
    print(f"File {file_name} not found!")
except pickle.UnpicklingError:
    print("Unpickling failed!")
except EOFError:
    print("File is empty!")
except Exception as e:
    print(f"Something went wrong: {e}.")
########################## Zadanie 7 ########################
## Zapisz do pliku liczbę 123456789, spakuj, rozpakuj dane
## Sprawdź w dokumentacji pakietu struct typ danej
## https://docs.python.org/3/library/struct.html
import struct
import pickle
import os

file_name = "binary.pkl"
number = 123456789

try:
    binary_data = struct.pack('i', number)
    print(f"Data in binary code: {binary_data}")
    with open(file_name, "wb") as file:
        pickle.dump(binary_data, file)
    print("Data has been saved in file!")

    del binary_data

    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            binary_data = pickle.load(file)
        print("Data has been loaded from file!")

    data = struct.unpack('i', binary_data)[0]
    print(f"Data: {data}")

except Exception as e:
    print(f"Something went wrong! {e}")
  
########################## Zadanie 9 #########################
## Utwórz i zapisz do folderu 5 dowolnych plików tekstowych z dowolnym tekstem
##(więcej niż 5 zdań), możesz tez skopiować dowolny tekst.
## Nazwy plików: Tekst1ID_ABC, Tekst2ID_405.txt, Tekst3ID_607.txt, Tekst4ID_ABC.txt, Tekst5ID_DEF.txt
## Uwaga: pisząc program przyjmij założenie, że masz takich nazw plików w folderze tysiące,
## program ma działać niezależnie od liczby plików w folderze
## Utwórz funkcję która:
## a) odczyta z folderu nazwy wszystkich plików
## b) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.
## Utwórz dodatkowową funkcję która wykorzystując poprzednią funkcję sprawdzi:
## a) ile plików zawiera w identyfikatorze ID liczbę 0
## b) dla wszystkich plików które w nazwie nie mają liczby 0
##    wyznaczy liczbę słów
## c) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.

# def createFiles(files):
#     text = (
#             "To jest pierwsze zdanie w pliku. \n"
#             "To jest drugie zdanie w pliku. \n"
#             "To jest trzecie zdanie w pliku. \n"
#             "To jest czwarte zdanie w pliku. \n"
#             "To jest piąte zdanie w pliku. \n"
#             "To jest szóste zdanie w pliku. \n"
#     )
#
#     for file in files:
#         path = os.path.join("task9", file)
#         with open(path, "w", encoding="utf-8") as f:
#             f.write(text)
#             f.close()
#
# def func():
#     files = os.listdir("task9")
#     wordsList = []
#     for file in files:
#         print(file)
#         name = file.split('.')[0]
#         if name.endswith("ABC"):
#             path = os.path.join("task9", file)
#             with open(path, "r", encoding="utf-8") as f:
#                 text = f.read()
#                 words = text.split()
#                 counter = 0
#                 for word in words:
#                     if len(word.strip(".,!?")) > 3:
#                         counter += 1
#                         wordsList.append(word)
#                 print(counter)
#                 f.close()
#     return wordsList
#
# def func2():
#     wordsList = func()
#     files = os.listdir("task9")
#     counter = 0
#     for file in files:
#         if "0" in file:
#             counter += 1
#         else:
#             path = os.path.join("task9", file)
#             with open(path, "r", encoding="utf-8") as f:
#                 text = f.read()
#                 words = text.split()
#                 print(f"Tyle słow w pliku {file}: ",len(words))
#                 f.close()
#     print("tyle plików z 0 w nazwie: ", counter)
#     print("tyle słow >3 w plikach z koncówką abc: ", len(wordsList))
#
#
#
# os.makedirs("task9",exist_ok=True)
# files = ["Tekst1ID_ABC.txt", "Tekst2ID_405.txt", "Tekst3ID_607.txt", "Tekst4ID_ABC.txt", "Tekst5ID_DEF.txt"]
# createFiles(files)
# func()
# func2()
--------------------------------------------------------------------------------------------------------------------------




