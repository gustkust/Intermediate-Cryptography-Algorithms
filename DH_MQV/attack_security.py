from src.DH import DH
from src.MQV import MQV
from src.common import choose_n_and_g

MQV_first_person = MQV(500, 1000)
MQV_second_person = MQV(500, 1000)

DH_impostor = DH(500, 1000)

print("Obie osoby wybierają wspólne n i g...")
n, g = choose_n_and_g(max_n=500)
print(f"Wybrano wspólne:\nn = {n}\ng = {g}\n")
print("!!! Oszust przechwytuje n i g !!!\n")

print("Pierwsza osoba generuje długoterminowe x i X...")
x = MQV_first_person.get_x()
X = MQV_first_person.get_X(x, n, g)
print(f"Pierwsza osoba otrzymała:\nx = {x}\nX = {X}\n")

print("Druga osoba generuje długoterminowe y i Y...")
y = MQV_second_person.get_x()
Y = MQV_second_person.get_X(y, n, g)
print(f"Druga osoba otrzymała:\ny = {y}\nY = {Y}\n")

print("!!! Oszust generuje z i Z... !!!")
z = DH_impostor.get_x()
Z = DH_impostor.get_X(z, n, g)
print(f"Oszust otrzymał:\nz = {z}\nZ = {Z}\n")

print(
    "Pierwsza osoba wysyła X do drugiej osoby (wysyła je dużo wcześnej od samej komunikacji, by oszust się nie zoriętował).\n")
print(
    "Druga osoba wysyła Y do pierwszej osoby (wysyła je dużo wcześnej od samej komunikacji, by oszust się nie zoriętował.\n")

print("Pierwsza osoba generuje krótkoterminowe a i A...")
a = MQV_first_person.get_x()
A = MQV_first_person.get_X(a, n, g)
print(f"Pierwsza osoba otrzymała:\ny = {a}\nY = {A}\n")

print("Druga osoba generuje krótkoterminowe b i B...")
b = MQV_second_person.get_x()
B = MQV_second_person.get_X(b, n, g)
print(f"Druga osoba otrzymała:\ny = {b}\nY = {B}\n")

print("Pierwsza osoba wysyła A do drugiej osoby.")
print(f"!!! Oszust przechwytuje A i zamiast tego wysyła Z do drugiej osoby !!!\n")

print("Druga osoba wysyła B do pierwszej osoby.")
print(f"!!! Oszust przechwytuje B i zamiast tego wysyła Z do drugiej osoby !!!\n")

print("Pierwsza osoba oblicza k na bazie otrzymanego Y, B (nieprawidłowego, tak naprawdę otrzymał Z), oraz x, a i A...")
k1 = MQV_first_person.get_k_mqv(Y, x, a, A, Z, n)
print(f"Pierwsza osoba otrzymała k = {k1}\n")

print("Druga osoba oblicza k na bazie otrzymanego X, A (nieprawidłowego, tak naprawdę otrzymał Z), oraz y, b i B...")
k2 = MQV_second_person.get_k_mqv(X, y, b, B, Z, n)
print(f"Pierwsza osoba otrzymała k = {k2}\n")

print("!!! Oszust oblicza k do komunikacji z pierwszą osobą na bazie otrzymanego X i z... !!!")
k3 = DH_impostor.get_k(X, z, n)
print(f"!!! Oszust otrzymuje k do komunikacji z pierwszą osobą k = {k3} !!!")

print("!!! Oszust oblicza k do komunikacji z drugą osobą na bazie otrzymanego Y i z... !!!")
k4 = DH_impostor.get_k(Y, z, n)
print(f"!!! Oszust otrzymuje k do komunikacji z drugą osobą k = {k4} !!!")

print(f"\nPierwsza osoba ma k = {k1}\n"
      f"Druga osoba ma k = {k2}\n"
      f"!!! Oszust ma k do komunikakcji z pierszą osobą k = {k3} !!!\n"
      f"!!! Oszust ma k do komunikacji z drugą osobą k = {k4} !!!\n")

if k1 != k2 != k3 != k4:
    print("Nie udało się ustalić wspólnego klucza, atak udaremniony!")

