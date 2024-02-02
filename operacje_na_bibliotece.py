import uuid



def legenda() -> None:

    print("0 - wyjdz z programu")
    print("1 - inf o asortymencie")
    print("2 - usun ksiazke ")
    print("3 - dodaj ksiazke")
    print("4 - edytuj ksiazke")
    print("5 - zobacz zawartość")
    print("==="*20)




def inf_ksiazka(dc: dict) -> None:
    for k, v in dc.items():
        if k == "zawartość":
            digit_count = liczbas_ilosc(str(v))
            print(f"Ilość znaków w {k} --- {digit_count}")
        else:
            print(f"{k} --- {v}")

def inf_biblioteka(lst:list) -> None:
    print(f"liczba ksiazek --- {len(lst)}")
    for ksizka in lst:
        print("==="*20)
        inf_ksiazka(ksizka)
        print("==="*20)


def czy_ksiazka_istnieje(lst: list, id_user_inp: str) -> bool:
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_user_inp:
            return True
    return False

def inex_instniejacej_kisiazki(lst: list, id_user_inp: str) -> int:
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_user_inp:
            return i
    return -1  

def usun_ksiazke(lst: list) -> None:
    inf_biblioteka(lst)
    print("Enter - zakoncz")
    inp = input("wklej id książki: ")
    if czy_ksiazka_istnieje(lst, inp):
        index = inex_instniejacej_kisiazki(lst, inp)
        if index != -1:
            lst.pop(index)
            print("ksiazka usunieta")
        else:
            print("ksiązka nie istnieje.")
    else:
        print("nie ma książki o takim ID")

        


def dodaj_tytul()-> str:
    print("Text !!!")
    inp = input("podaj tytul: ")
    print("==="*20)
    return inp

def podaj_cene() -> float:
    while True:
        try:
            print("Liczba !!!")
            inp = float(input("Cena: "))
            print("==="*20)
            return inp
        except ValueError:
            print("tylko liczby, try again")


def podaj_liczbe_stron()-> int:
    print("zawartość książki") # numer_stron                                                   tutaj to tam to
    lck = input()
    print("==="*20)
    return lck
    


# -----------------------------------------------------     
def liczbas_ilosc(text):
    znaki = 0
    for char in text:
        if char.isalpha():
            znaki += 1
        elif char.isdigit():
            znaki += 1
    return znaki


znaki = liczbas_ilosc(podaj_liczbe_stron())

def pokaz_zawartosc(lst: list) -> None:
    print(f"Liczba ksiazek --- {len(lst)}")
    print("==="*20)
    inf_biblioteka(lst)
    print("Enter - zakoncz")
    if lst:
        last_book_id = str(lst[-1]["id"])
        print(f"Last book ID: {last_book_id}")
        inp = input(f"Wklej ID książki (ostatnia książka(default): {last_book_id}): ")
        inp = inp.strip() if inp else last_book_id
    else:
        inp = input("Wklej ID książki: ")
    for ksizka in lst:
        if str(ksizka["id"]) == inp:
            print(f"{ksizka['zawartość']}")
            print("==="*20)
            return
    print(f"Nie ma książki o ID {inp}")


# -----------------------------------------------------

def dodaj_ksiazke(lst: list)-> None:
    ksiazka = {
        "id":uuid.uuid4(),
        "tytul":dodaj_tytul(),
        "cena": podaj_cene(),
        "zawartość": podaj_liczbe_stron()
    }
    lst.append(ksiazka)

def edytuj_dane_ksiazki(lst:list) -> None:
    inf_biblioteka(lst)
    print("Enter - zakoncz")
    inp = input("Wklej ID książki: ")
    if czy_ksiazka_istnieje(lst, inp):
        index_ksiazki = inex_instniejacej_kisiazki(lst, inp)
        lst[index_ksiazki]["tytul"] = dodaj_tytul()
        lst[index_ksiazki]["cena"] = podaj_cene()
        lst[index_ksiazki]["ilość słów"] = podaj_liczbe_stron()
    else:
        print("nie ma książki o takim ID")