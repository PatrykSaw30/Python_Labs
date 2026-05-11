if __name__ == '__main__':
    print "Zadanie 1:"
    print("0 > 1 :", 0 > 1)
    print("0 <= 1 :", 0 <= 1)
    print("0 >= 1 :", 0 >= 1)
    print("1 == 0 :", 1 == 0)
    print("1 == 1 :", 1 == 1)
    print("1 != 0 :", 1 != 0)
    print("1 != 1 :", 1 != 1)
    #
    print "Zadanie 2:"
    var_int_x = int(input("Podaj zmienna x: "))
    var_int_y = int(input("Podaj zmienna y: "))
    print("2x+5y = ", 2*var_int_x+5*var_int_y)

    print "Zadanie 3:"
    var_string_name = input("podaj imie: ")
    var_string_surname = input("podaj nazwisko: ")
    var_int_age = int(input("podaj wiek: "))
    var_string_academy = input("podaj kierunek studiów: ")
    print("Jestem " + var_string_name+ " "+ var_string_surname + " mam " + str(var_int_age) + " lat, studiuje " + var_string_academy + "." )

    print "Zadanie 4:"
    if (1+2+10+20000001+4+347586970885) == 321784560456434534646 :
        print("To działanie równa się liczbie 321784560456434534646")
    else:
        print("To działanie nie równa się liczbie 321784560456434534646, poprawny wynik to ", (1+2+10+20000001+4+347586970885))

    print "Zadanie 5:"
    var_int_x = int(input("Podaj zmienna x: "))
    var_int_y = int(input("Podaj zmienna y: "))
    if (var_int_x+var_int_y) % 2 == 0:
        print("suma twoich liczb jest parzysta")
    else:
        print("suma twoich liczb nie jest parzysta")
    #
    print "Zadanie 6:"
    var_int_x = int(input("Podaj zmienna x: "))
    var_int_y = int(input("Podaj zmienna y: "))
    var_char_sign = input("(+,-,*,/) Podaj znak działania: ")
    match var_char_sign:
        case "+":
            print(var_int_x+var_int_y)
        case "-":
            print(var_int_x-var_int_y)
        case "*":
            print(var_int_x * var_int_y)
        case "/":
            if var_int_y == 0:
                print("Nie dziel przez 0!")
            else:
                print(round((var_int_x / var_int_y), 2))
        case _:
            print("Error")
    #
    print "Zadanie 7:"
    var_int_x = int(input("Podaj zmienna x: "))
    print("(x > 1 and x < 13) : ", (var_int_x > 1 and var_int_x < 13))
    print("(x != 5 or x < 0) : ", (var_int_x != 5 or var_int_x < 0))
    #
    # ---------------------------------------

    print "Zadanie 1a:"
    person = {
        'name' : input("podaj imie: "),
        'surname' : input("podaj nazwisko: "),
        'age' : int(input("podaj wiek: ")),
        'nutrition' : input("Czy zdrowo się odżywiasz? "),
        'sport' : input("Czy lubisz sport? "),
        'academy' : input("podaj kierunek studiów: "),
        'food' : input("Podaj ulubione jedzenie: "),
        'film' : input("Podaj ulubiony film: ")
    }
    for key, value in person.items():
        print(key , ":" , value)

    print "Zadanie 2a:"
    person = {
        'name' : input("podaj imie: "),
        'surname' : input("podaj nazwisko: "),
        'age' : int(input("podaj wiek: ")),
        'job' : input("podaj zawód: "),
        'birth' : input("podaj miejsce urodzenia: "),
        'interests' : input("podaj swoje zainteresowania: ")
    }

    txt = (
        f"Nazywam się {person.get('name')} {person.get('surname')}. \n"
        f"Mam {person.get('age')} lat. \n"
        f"Urodziłem/am się w miejscowości {person.get('birth')}. \n"
        f"Obecnie pracuje jako {person.get('job')}, stale podnosząc swoje kompetencje. \n"
        f"W wolnych chwilach oddaję się mojej pasji, jaką są {person.get('interests')}. \n"
    )

    print(txt)
    #
    print "Zadanie 3a:"


    print "Zadanie 4a:"
    var_string_name = input("Podaj imie: ")
    if var_string_name == "Janusz":
        print("Twoje podane imie to Janusz")
    elif var_string_name == "Grażyna":
        print("Twoje podane imie to Grażyna")
    else:
        print("error")
    #
     print("")
