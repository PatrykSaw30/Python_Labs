import sys
import functools

try:
    import stars
    import sil
except ModuleNotFoundError:
    print("Uwaga: Brak modułów stars.py lub sil.py w katalogu roboczym.")

def zad_1():
    print("\n[Zadanie 1]")
    znaki = list("Python")
    sklej_tekst = lambda x: "".join(x)
    print("Wynik:", sklej_tekst(znaki))

def zad_2():
    print("\n[Zadanie 2]")
    osoba = "Jan Kowalski"
    podzial = lambda s: list(map(list, s.split()))
    print("Lista liter:", podzial(osoba))

def zad_3():
    print("\n[Zadanie 3]")
    zawiera_znak = lambda slowo, znak: znak in slowo
    print("Czy 'Kowalski' ma literę 'a'?", zawiera_znak("Kowalski", "a"))
    print("Czy 'Kowalski' ma literę 'x'?", zawiera_znak("Kowalski", "x"))

def zad_4():
    print("\n[Zadanie 4]")
    dane_logowania = {}
    
    while True:
        uzytkownik = input("Wpisz nazwe uzytkownika (lub STOP): ")
        if uzytkownik.upper() == "STOP":
            break
            
        haslo = input("Wpisz haslo: ")
        if len(haslo) == 0:
            print("Haslo jest wymagane. Ponow probę.")
            continue
            
        dane_logowania[uzytkownik] = haslo

    print("Utworzony słownik:", dane_logowania)

def zad_5():
    print("\n[Zadanie 5]")
    try:
        print("Kształt E:")
        stars.poziom(5)
        stars.pion(1)
        stars.poziom(4)
        stars.pion(1)
        stars.poziom(5)

        print("\nKształt L:")
        stars.pion(4)
        stars.poziom(5)
    except NameError:
        print("Błąd: import 'stars' nie powiódł się.")

def zad_6():
    print("\n[Zadanie 6]")
    try:
        n = int(input("Podaj n: "))
        k = int(input("Podaj k (nie większe niż n): "))

        if k > n or n < 0 or k < 0:
            print("Błąd: k nie może być większe od n, a liczby muszą być dodatnie.")
            return

        wynik = sil.silnia(n) // (sil.silnia(k) * sil.silnia(n - k))
        print(f"Obliczony symbol Newtona: {wynik}")

    except ValueError:
        print("Oczekiwano liczb całkowitych.")
    except NameError:
        print("Błąd: import 'sil' nie powiódł się.")

def zad_7():
    print("\n[Zadanie 7]")
    parzyste = list(filter(lambda wartosc: wartosc % 2 == 0, range(1, 100)))
    print(", ".join(map(str, parzyste)))

def zad_8():
    print("\n[Zadanie 8]")
    iloczyn = functools.reduce(lambda a, b: a * b, range(1, 100))
    print(f"Iloczyn liczb 1-99 (fragment): {str(iloczyn)[:20]}...")

def zad_9_10():
    print("\n[Zadanie 9 i 10]")
    liczby = filter(lambda cyfra: cyfra % 7 == 0 and cyfra % 5 != 0, range(2000, 3201))
    print(", ".join([str(x) for x in liczby]))

def zad_11():
    print("\n[Zadanie 11]")
    try:
        wybor = input("Wprowadź literę (E lub L): ").strip().upper()
        szablon = lambda znak: print("*****\n*\n****\n*\n*****" if znak == 'E' else ("*\n*\n*\n*\n*****" if znak == 'L' else "Nieobsługiwana litera!"))
        szablon(wybor)
    except Exception as err:
        print("Wystąpił wyjątek:", err)

if __name__ == '__main__':
    zad_1()
    zad_2()
    zad_3()
    zad_4()
    zad_5()
    zad_6()
    zad_7()
    zad_8()
    zad_9_10()
    zad_11()
