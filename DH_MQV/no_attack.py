from src.DH import DH
from src.common import choose_n_and_g


DH_first_person = DH()
DH_second_person = DH()

print("Obie osoby wybierają wspólne n i g...")
n, g = choose_n_and_g()
print(f"Wybrano wspólne:\nn = {n}\ng = {g}\n")

print("Pierwsza osoba generuje x i X...")
x = DH_first_person.get_x()
X = DH_first_person.get_X(x, n, g)
print(f"Pierwsza osoba otrzymała:\nx = {x}\nX = {X}\n")

print("Druga osoba generuje y i Y...")
y = DH_second_person.get_x()
Y = DH_second_person.get_X(y, n, g)
print(f"Druga osoba otrzymała:\ny = {y}\nY = {Y}\n")

print("Pierwsza osoba wysyła X do drugiej osoby.\n")
print("Druga osoba wysyła Y do pierwszej osoby.\n")

print("Pierwsza osoba oblicza k na bazie otrzymanego Y i x...")
k1 = DH_first_person.get_k(Y, x, n)
print(f"Pierwsza osoba otrzymała k = {k1}\n")

print("Druga osoba oblicza k na bazie otrzymanego X i y...")
k2 = DH_second_person.get_k(X, y, n)
print(f"Pierwsza osoba otrzymała k = {k2}\n")

if k1 == k2:
    print("Sukces!")
else:
    print("Błąd!")
