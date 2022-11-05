from src.DH import DH
from src.common import choose_n_and_g


DH_first_person = DH()
DH_second_person = DH()

DH_impostor = DH()

print("Obie osoby wybierają wspólne n i g...")
n, g = choose_n_and_g()
print(f"Wybrano wspólne:\nn = {n}\ng = {g}\n")

print("!!! Oszust przechwytuje n i g !!!\n")

print("Pierwsza osoba generuje x i X...")
x = DH_first_person.get_x()
X = DH_first_person.get_X(x, n, g)
print(f"Pierwsza osoba otrzymała:\nx = {x}\nX = {X}\n")

print("Druga osoba generuje y i Y...")
y = DH_second_person.get_x()
Y = DH_second_person.get_X(y, n, g)
print(f"Druga osoba otrzymała:\ny = {y}\nY = {Y}\n")

print("!!! Oszust generuje z i Z... !!!")
z = DH_impostor.get_x()
Z = DH_impostor.get_X(z, n, g)
print(f"Oszust otrzymał:\nz = {z}\nZ = {Z}\n")

print("Pierwsza osoba wysyła X do drugiej osoby.")
print(f"!!! Oszust przechwytuje X i zamiast tego wysyła Z do drugiej osoby !!!\n")

print("Druga osoba wysyła Y do pierwszej osoby.")
print(f"!!! Oszust przechwytuje Y i wysyła zmienione Z do pierwszej osoby !!!\n")

print("Pierwsza osoba oblicza k na bazie otrzymanego Y (nieprawidłowego, tak naprawdę otrzymał Z) i x...")
k1 = DH_first_person.get_k(Z, x, n)
print(f"Pierwsza osoba otrzymała k = {k1}\n")

print("Druga osoba oblicza k na bazie otrzymanego X (nieprawidłowego, tak naprawdę otrzymał Z) i y...")
k2 = DH_second_person.get_k(Z, y, n)
print(f"Druga osoba otrzymała k = {k2}\n")


print("!!! Oszust oblicza k do komunikacji z pierwszą osobą na bazie otrzymanego X i z... !!!")
k3 = DH_impostor.get_k(X, z, n)
print(f"!!! Oszust otrzymuje k do komunikacji z pierwszą osobą k = {k3} !!!")

print("!!! Oszust oblicza k do komunikacji z drugą osobą na bazie otrzymanego Y i z... !!!")
k4 = DH_impostor.get_k(Y, z, n)
print(f"!!! Oszust otrzymuje k do komunikacji z drugą osobą k = {k4} !!!")


print(f"\nPierwsza osoba ma k = {k1}\n"
      f"Druga osoba ma k = {k2}\n"
      f"!!! Oszust ma k do komunikakcji z pierszą osobą k = {k3} !!!\n"
      f"!!! Oszust ma k do komunikacji z drugą osobą k = {k4} !!!")
