##### Task 1
### Utwórz 2 listy, pierwsza liczby od 1 do 100, druga 100 losowych liczb
### odejmnij wartości elementów listy pierwszej od drugiej
### Wykorzystaj map() i funkcję sub() z modułu operators
import random
from functools import reduce
# list1 = []
# list2 = []
#
# for i in range(0,100):
#     list1.append(i+1)
#     list2.append(random.randint(1,100))
#
# print(list(map(operator.sub, list1,list2)))


##### Task 2
### Utwórz listę zawierającą 10000 losowych liczb
### wyselekcjonuj liczby mniejsze niż 3 i parzyste
### Wykorzystaj filter() i funkcje z modułu operators

# list1 = []
# for i in range(10000):
#     list1.append(random.randint(1,100))
#
# list2 = list((filter(lambda x: operator.and_(operator.lt(x, 3), operator.eq(x % 2, 0)), list1))
#
# print(list1)
# print(list2)

##### Task 3
### Utwórz pętlę generującą 50 liczb całkowitych z krokiem 5, większych niż 99
### Wykorzystaj count()

# c=1;
# for i in itertools.count(100, 5):
#     if i<350:
#         print(str(c)+". "+ str(i))
#         c = c+1
#     else:
#         break

##### Task 4
### Utwórz funkcję funcycle(n) która z sekwencji 'INFORMATYKA'
### n krotnie (argument funkcji) wypisze w cyklu każdy z jej elementów
### Wykorzystaj cycle()

# def funcycle(n):
#     c = 0
#     for i in itertools.cycle('INFORMATYKA'):
#         if c >= n:
#             break
#         else:
#             print(i)
#             c +=1
#
# funcycle(20)


##### Task 5
### Oblicz iloczyn kartezjański 3D, [1,2,3], ['a','b','c'], [True,False]

# a = [1,2,3]
# b = ['a','b','c']
# c = [True, False]
#
# print(list(product(a, b, c)))


### Task 6
### Posiadasz grupę N-studentów (N-indeksów), podziel w/w grupę na n-podgrup
### Specyfikacja kodu: funkcja, wykorzystanie iteratora kombinatorycznego

# list1 = list(range(1,6))
# print(list1)
# print(list(permutations(list1)))


from itertools import accumulate,chain
from itertools import compress, dropwhile, filterfalse


### Task 7
## początkowa kwota na 3mc lokacie to k = 10000, oprocentowanie lokaty to 0.01%
## oblicz jaką kwotę zgromadzi użytkownik po upływie t = 9mc
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego

# start = 10000
# p = 1.0001
# months = 9
#
# list1 = list(accumulate(range(months), lambda x, _: x*p, initial=start))
# print(list1[9])

### Task 8
### Utwórz własny generator liczb które są kolejnymi wielokrotnosciami liczby cztery tj. 4,16,32,64,... itd
### n - liczbę elementów w generatorze deklaruje użytkownik
### np. dla n=3,  funkcja next w kolejnych wywołaniach zwraca:  4, 16, 32

# def gen4(n):
#     x = 4
#     for i in range(0,n):
#         yield x
#         # x = x + 4
#         x = x*2
#
# g = gen4(5)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


### Task 9
## a) Utwórz własny generator zwracający 1000 losowych liczb parzystych z zakresu 0-100000000

# def even(n):
#     i = 0
#     while i<n:
#         x = random.randint(0,100000000)
#         if x % 2 == 0:
#             yield x
#             i += 1
#
# list1 = list(even(1000))
#
# print(len(list1))

#### Task 9
## Utwórz generator dla ciągu Fibonacciego (pierwszy wyraz ciągu jest równy 0, drugi jest równy 1,
## a każdy kolejny element ciągu jest sumą dwóch poprzednich. Wypisz n-ty element tego ciągu
## Użytkownik deklaruje ilość elementów (n).
## Specyfikacja: użyj accumulate() lub reduce() do wygenerowania ciągu Fibonacciego

# from functools import reduce
# from itertools import accumulate
# from datetime import datetime
#
# def fibo(n):
#     time0 = datetime.now().microsecond
#     if n <= 0:
#         return
#
#     numbers = accumulate (
#         range(n-1),
#         lambda x, _: (x[1], x[0]+x[1]),
#         initial=(0,1)
#     )
#
#     for i in numbers:
#         yield i[0]
#
#     print("Czas: " + str(datetime.now().microsecond - time0))
#
# val = int(input("Podaj liczbe: "))
#
#
# list1 = list(fibo(val))
#
#
# print(list1)
#
# from sys import getsizeof
#
# print(getsizeof(list1))


#### Task 10
## Porównaj czas obliczeń i ilość zajmowanej pamięci przez dane w przypadku gdy programujesz
## a) imperatywnie/sturkturalnie,
## b) funkcyjnie stosując funkcje ale nie wyższego rzędu,
## c) funkcyjnie stosując funkcje wyższego rzędu, do zrównoleglenia obliczeń
## d) funkcyjnie stosując generator/iterator,
## Jak wariant realizuje zadanie najszybciej, a jakie zajmuje najmniej pamięci?

## Utwórz 3 listy po 1000000 losowych liczb
## zapisz liczby z 3 list do 2-ch list: pierwsza zawiera liczby parzyste, druga liczby nieparzyste

# from datetime import datetime
# from sys import getsizeof
#
# list1 = [random.randint(0, 100) for _ in range(1000000)]
# list2 = [random.randint(0, 100) for _ in range(1000000)]
# list3 = [random.randint(0, 100) for _ in range(1000000)]
# list4 = list1 + list2 + list3
#
# #a:
# print("A: \n")
# time0 = datetime.now().microsecond
# even = []
# odd = []
# for i in list4:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Czas: " + str(datetime.now().microsecond - time0))
# print("parzyste: " + str(getsizeof(even)))
# print("nieparzyste: " + str(getsizeof(odd)))
#
# #b:
# print("\n B: \n")
# time0 = datetime.now().microsecond
# even = [i for i in list4 if i % 2 ==0]
# odd = [i for i in list4 if i % 2 != 0]
# print("Czas: " + str(datetime.now().microsecond - time0))
# print("parzyste: " + str(getsizeof(even)))
# print("nieparzyste: " + str(getsizeof(odd)))
#
# #c:
# print("\n C: \n")
# time0 = datetime.now().microsecond
# even = list(filter(lambda x: x % 2 == 0, list4))
# odd = list(filter(lambda x: x % 2 != 0, list4))
# print("Czas: " + str(datetime.now().microsecond - time0))
# print("parzyste: " + str(getsizeof(even)))
# print("nieparzyste: " + str(getsizeof(odd)))
#
# #d:
# print("\n D: \n")
# def gen():
#     even = (i for i in list4 if i % 2 == 0)
#     odd = (i for i in list4 if i % 2 != 0)
#     return list(even), list(odd)
#
# time0 = datetime.now().microsecond
# gener = gen()
# print("Czas: " + str(datetime.now().microsecond - time0))
# print(getsizeof(gener))

#### Task 11
### W przypadku dużych danych stosujemy algorytm dziel i rządź, który polega na odpowiednim
### 1. dzieleniu danych na części,
### 2. mapowaniu (operacja którą można przeprowadzić niezależnie w pewnym zakresie np. tworzymy pary klucz-wartość),
### 3. przesuwaniu (np.grupowanie podobnych kluczy, jesli są one blisko siebie agregujemy ich wartości)
### 4. redukowaniu danych (agregowanie danych poprzez ich redukcję)

## Utwórz listę zawierającą 10000 losowych nazw 6 języków programowania
## np. list_prog = ['python','java','C++','C++','python',....,'java']
# oblicz ile razy wybrany język programowania wystąpił w liście
## a) programuj imperatywnie
## b) programuj funkcyjnie
## c) wykorzystaj algorytm dziel i rządź który stosujemy aby zobtymalizować obliczenia gdy dane są duże
## np. wariant1: podziel zadania na podzadania wykonaj operację na zliczania na podzbiorach i agreguj wyniki
## wykorzystaj funkcje wbudowane lub metody dedykowane dla list
## np. wariant2: dzielisz listę na n-list, każda lista zawiera m-krotek [('python',1),...,('java',1),('C++',1)]
## przesuwasz identyczne krotki do 6-ciu list i zliczasz ilości, wynik końcowy to np. ('python',101),('java',23)

# languages = ['Python', 'PHP', 'C#', 'C++', 'JavaScript', 'Kotlin']
#
# list1 = [random.choice(languages) for _ in range(10000)]
#
# target = 'PHP'
# counter = 0
# # a:
# for i in list1:
#     if i == target:
#         counter += 1
#
# print(target + " wystapil w liscie tyle razy: " + str(counter))
#
# # b:
# result = list(filter(lambda x: x == target, list1))
#
# print(target + " wystapil w liscie tyle razy: " + str(len(result)))
#
# # c:
# size = int(len(list1) / 4)
#
# x = []
#
# for i in range(4):
#     start = i*size
#     end = (i+1)*size
#
#     mini_list = list1[start:end]
#     x.append(mini_list)
#
# mapped = list(map(lambda new_list: new_list.count(target), x))
#
# new_result = reduce(lambda a, b: a + b, mapped)
#
# print(target + " wystapil w liscie tyle razy: " + str(new_result))
