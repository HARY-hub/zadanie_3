print("=== ŁADOWARKA PACZEK ===")

# Zabezpieczenie 1: Poprawne wprowadzenie liczby paczek
while True:
    try:
        n = int(input("Ile paczek? "))
        if n <= 0:
            print("Liczba paczek musi być większa od 0!")
            continue
        break
    except ValueError:
        print("To musi być liczba całkowita!")

w = 0
p = []

for i in range(n):
    # Zabezpieczenie 2: Poprawne wprowadzenie wagi
    while True:
        try:
            kg = float(input(f"Waga {i+1}: "))
            
            # Zabezpieczenie 3: Natychmiastowe zakończenie programu dla wagi > 10 kg
            if kg > 10:
                print("BŁĄD: Paczka przekracza 10 kg! Program zostaje zakończony.")
                exit()
            
            # Zabezpieczenie 4: Sprawdzenie minimalnej wagi
            if kg < 1:
                print("Waga musi być w zakresie 1-10 kg! Spróbuj ponownie.")
                continue
            break
        except ValueError:
            print("To musi być liczba!")

    # Logika ładowania paczek
    if w + kg > 20:
        p.append(w)
        w = kg
    else:
        w += kg

# Dodanie ostatniej paczki jeśli istnieje
if w > 0:
    p.append(w)

# Wyświetl wyniki tylko jeśli są paczki
if len(p) > 0:
    print(f"\nWysłano paczek: {len(p)}")
    print(f"Waga całkowita: {sum(p):.2f} kg")
    print(f"Puste kilogramy: {len(p)*20 - sum(p):.2f} kg")
    
    if p:
        pustki = [20 - x for x in p]
        nr = pustki.index(max(pustki)) + 1
        print(f"Najwięcej pustych: paczka #{nr} ({max(pustki):.2f} kg)")
else:
    print("\nNie załadowano żadnych paczek.")