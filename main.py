from biblioteka import biblioteka # <---
import operacje_na_bibliotece
import os

# co zmieniłem:
# user-proof | inf o asortymencie pokazuje ilość słów w zawartości, a żeby zobaczyć zawartość trzeba użyć 5 | 



def main() -> None:
    while True:
        operacje_na_bibliotece.legenda()
        inp = int(input("--->\t"))
        os.system("cls") 
        if inp == 0:
            os.system("clear")
            z = "program zakonczyl dzialanie"
            print("\n"*5)
            print(f"\t {z.upper()}")
            print("\n"*5)
            break
        elif inp == 1:
            operacje_na_bibliotece.inf_biblioteka(biblioteka)
        elif inp == 2:
            operacje_na_bibliotece.usun_ksiazke(biblioteka)
        elif inp == 3:
            operacje_na_bibliotece.dodaj_ksiazke(biblioteka)
        elif inp == 4:
            operacje_na_bibliotece.edytuj_dane_ksiazki(biblioteka)
        elif inp == 5:
            operacje_na_bibliotece.pokaz_zawartosc(biblioteka)
        else:
            print("Nie ma takiej operacji aaaa") 
            print("==="*20)

# -----------------------------------------------------
if __name__ == "__main__":
    main()
    