numbers = []

for i in range(5):
    number = float(input("Podaj liczbę: "))
    numbers.append(number)
suma = sum(numbers)
najwieksza = max(numbers)
najmniejsza = min(numbers)
srednia = suma / len(numbers)
liczby_parzyste = [x for x in numbers if x % 2 == 0]
ilosc_parzystych = len(liczby_parzyste)
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
numbers = list(set(numbers))
squares = [x ** 2 for x in numbers]
print("Suma liczb:", suma)
print("Największa liczba:", najwieksza)
print("Najmniejsza liczba:", najmniejsza)
print("Średnia arytmetyczna:", srednia)
print("Ilość liczb parzystych:", ilosc_parzystych)
print("Powtarzające się elementy:", duplicates)
print("Lista bez powtórzeń:", numbers)
print("Kwadraty liczb:", squares)
