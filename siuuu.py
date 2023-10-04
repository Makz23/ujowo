# 1. Utwórz pustą listę o nazwie "numbers".
numbers = []

# 2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
for i in range(5):
    number = float(input("Podaj liczbę: "))
    numbers.append(number)

# 3. Oblicz sumę liczb znajdujących się w liście "numbers".
suma = sum(numbers)

# 4. Znajdź największą liczbę w liście "numbers".
najwieksza = max(numbers)

# 5. Znajdź najmniejszą liczbę w liście "numbers".
najmniejsza = min(numbers)

# 6. Znajdź średnią arytmetyczną liczb w liście "numbers".
srednia = suma / len(numbers)

# 7. Znajdź ilość liczb parzystych w liście "numbers".
liczby_parzyste = [x for x in numbers if x % 2 == 0]
ilosc_parzystych = len(liczby_parzyste)

# 8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

# 9. Usuń wszystkie powtarzające się elementy z listy "numbers".
numbers = list(set(numbers))

# 10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
squares = [x ** 2 for x in numbers]

# Wyświetl wyniki
print("Suma liczb:", suma)
print("Największa liczba:", najwieksza)
print("Najmniejsza liczba:", najmniejsza)
print("Średnia arytmetyczna:", srednia)
print("Ilość liczb parzystych:", ilosc_parzystych)
print("Powtarzające się elementy:", duplicates)
print("Lista bez powtórzeń:", numbers)
print("Kwadraty liczb:", squares)