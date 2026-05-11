# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
print('----ZADANIE 1----')
lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
gene1 = "FGFR4"
gene2 = "FGERA4"

if gene1 in lista_gene1:
    print("FGFR4 index:", lista_gene1.index(gene1))
else:
    print("FGFR4 nie istnieje")

if gene2 in lista_gene1:
    print("FGERA4 index:", lista_gene1.index(gene2))
else:
    print("FGERA4 nie istnieje")
 #####Zadanie 3
    ## Przekopiuj dowolny ale długi fragment tekstu ze strony:
    ## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
    ## sprawdź:
    ## a) ile razy w tekście występuje słowo Emma
    ## b) zamień całość tekstu na duże litery
    ## c) wstaw poszczególne wyrazy jako elementy listy
    ## d) ile zdań jest w analizowanym tekście?
    print('----ZADANIE 2----')

    tekst = """A co z Emmą? Kryje się na nią jakiś człowiek? Shaunak Khire, współtwórca Stealth, twierdzi, że choć Emma posiada zespół ludzkich trenerów, efekty jej pracy są wyłącznie jej zasługą. Zawsze ciężko będzie laikom korzystającym z tych usług wiedzieć na pewno, czy chodzi o maszynę czy o człowieka."""

    print('----A----')
    print(tekst.count("Emma"))
    print('----B----')
    print(tekst.upper())
    print('/n----C----/n')
    lista_slow = tekst.split(" ")
    print(lista_slow)
    print('----D----')
    print(tekst.count("."))


########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta
print('----ZADANIE 4----')
liczba = int(input("Podaj liczbę: "))

if liczba % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

    ########Zadanie 5
    ## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
    ## student uzyskuje określoną ocenę końcową z laboratorium
    ## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 - if
    ## np 50% to 3.0, 61% to 3.5, ...., 91% to 5.0 - match
    ## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktó
print('----ZADANIE 5----')
punkty = int(input("Podaj liczbę punktów (0-15): "))

match punkty:
    case 8 | 9:
        print("3.0")
    case 10:
        print("3.5")
    case 11:
        print("4.0")
    case 12:
        print("4.5")
    case 13 | 14 | 15:
        print("5.0")
    case _:
        print("Niezaliczone")
print('----ZADANIE 6----')
# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
n = int(input("Podaj n: "))

suma = 0

for i in range(1, n+1):
    suma += 1/i
    print('----ZADANIE 7----')
    ###### Zadanie 7
    ###### Calculate the root of the numbers from 1 to 10 using the while loop
    ###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while

print("Suma =", suma)
print('----ZADANIE 7----')
###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while
import math

i = 1

while i <= 10:
    print("Pierwiastek z", i, "=", math.sqrt(i))
    i += 1
print('----ZADANIE 8----')
###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)

elif delta == 0:
    x = -b/(2*a)
    print("x =", x)

else:
    print("Brak rozwiązań") 3 digits: a, b, c as input and

print('----ZADANIE 9----')
###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed
### in a comma-separated sequence on a single line.
wynik = []

for i in range(1,1001):

    liczba = str(i)

    if all(int(c)%2==0 for c in liczba):
        wynik.append(liczba)

print(",".join(wynik))
print('----ZADANIE 10----')
while True:

    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))

    if x == 0 or y == 0:
        print("Program zakończony")
        break

    if isinstance(x,int) and isinstance(y,int):
        print("Wynik:", x*y)



