from src.MQV import MQV
from src.common import choose_n_and_g


MQV_first_person = MQV(100, 1000)
MQV_second_person = MQV(100, 1000)

print("Obie osoby wybierają wspólne n i g...")
n, g = choose_n_and_g(max_n=100)
print(f"Wybrano wspólne:\nn = {n}\ng = {g}\n")

print("Pierwsza osoba generuje długoterminowe x i X...")
x = MQV_first_person.get_x()
X = MQV_first_person.get_X(x, n, g)
print(f"Pierwsza osoba otrzymała:\nx = {x}\nX = {X}\n")

print("Druga osoba generuje długoterminowe y i Y...")
y = MQV_second_person.get_x()
Y = MQV_second_person.get_X(y, n, g)
print(f"Druga osoba otrzymała:\ny = {y}\nY = {Y}\n")

print("Pierwsza osoba wysyła X do drugiej osoby.\n")
print("Druga osoba wysyła Y do pierwszej osoby.\n")

print("Pierwsza osoba generuje krótkoterminowe a i A...")
a = MQV_first_person.get_x()
A = MQV_first_person.get_X(a, n, g)
print(f"Pierwsza osoba otrzymała:\ny = {a}\nY = {A}\n")

print("Druga osoba generuje krótkoterminowe b i B...")
b = MQV_second_person.get_x()
B = MQV_second_person.get_X(b, n, g)
print(f"Druga osoba otrzymała:\ny = {b}\nY = {B}\n")

print("Pierwsza osoba wysyła A do drugiej osoby.\n")
print("Druga osoba wysyła B do pierwszej osoby.\n")

print("Pierwsza osoba oblicza k na bazie otrzymanego Y, B, oraz x, a i A...")
k1 = MQV_first_person.get_k_mqv(Y, x, a, A, B, n)
print(f"Pierwsza osoba otrzymała k = {k1}\n")

print("Druga osoba oblicza k na bazie otrzymanego X, A, oraz y, b i B...")
k2 = MQV_second_person.get_k_mqv(X, y, b, B, A, n)
print(f"Pierwsza osoba otrzymała k = {k2}\n")

if k1 == k2:
    print("Sukces!")
else:
    print("Błąd!")
