print("=== ŁADOWARKA PACZEK ===")

# Pobranie liczby elementów
while True:
    try:
        n = int(input("Ilość elementów: "))
        if n <= 0:
            print("Liczba musi być większa od 0!")
            continue
        break
    except ValueError:
        print("To musi być liczba całkowita!")

aktualna_paczka = []
paczki = []
suma_wszystkich_kg = 0

# Pobieranie wag elementów
for i in range(n):
    try:
        kg = float(input(f"Waga elementu {i+1}: "))

        # Sprawdzenie zakresu 1–10 kg
        if kg < 1 or kg > 10:
            print("Podano wagę spoza zakresu 1–10 kg. Zakończenie dodawania.")
            break

        # Jeśli przekroczy 20 kg → zamknij paczkę
        if sum(aktualna_paczka) + kg > 20:
            paczki.append(aktualna_paczka)
            aktualna_paczka = [kg]
        else:
            aktualna_paczka.append(kg)

        suma_wszystkich_kg += kg

    except ValueError:
        print("To musi być liczba!")
        break

# Dodanie ostatniej paczki
if aktualna_paczka:
    paczki.append(aktualna_paczka)

# PODSUMOWANIE
if paczki:
    liczba_paczek = len(paczki)
    suma_pustych = liczba_paczek * 20 - suma_wszystkich_kg

    # Obliczanie pustych kg dla każdej paczki
    puste_w_paczkach = [20 - sum(p) for p in paczki]
    max_pustych = max(puste_w_paczkach)
    nr_max = puste_w_paczkach.index(max_pustych) + 1

    print("\n=== PODSUMOWANIE ===")
    print(f"Wysłano {liczba_paczek} paczkę/paczki:", end=" ")

    opis = []
    for p in paczki:
        opis.append("(" + "+".join(str(int(x)) for x in p) + ")")

    print(", ".join(opis))
    print(f"Wysłano {int(suma_wszystkich_kg)} kg")
    print(f"Suma pustych kilogramów: {int(suma_pustych)}kg")
    print(f"Najwięcej pustych kilogramów ma paczka {nr_max} ({int(max_pustych)}kg)")
else:
    print("\nNie załadowano żadnych paczek.")