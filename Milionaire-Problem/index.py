import random
from RSA.key_generator import generate_keys
from mod import Mod


def milionaire_problem(M):
    I = random.randint(0, M)
    print(f"Apolonia ma {I} milionów.")

    J = random.randint(0, M)
    print(f"Bogus ma {J} milionow.\n")

    print("Apolonia generuje klucz prywatny i publiczny...")
    public_key, private_key = generate_keys()
    e = public_key[0]
    n = public_key[1]
    d = private_key[0]
    print(f"Apolonia uzyskała klucz publiczny n = {n}, e = {e}, oraz klucz prywatny d = {d}.")
    print(f"Apolonia przekazuje Bogusiowi klucz publiczny n = {n}, e = {e}.\n")

    x = random.randint(1, M)
    print(f"Bogus wybiera losową wartość x = {x}.\n")

    print("Bogus szyfruje x, przy pomocy klucza prywatnego...")
    C = x ** e % n
    print(f"Bogus otrzymał C = {C}.\n")

    print("Bogus oblicza m...")
    m = C - J + 1
    print(f"Bogus otrzymał m = {m}. Przekazuje je Apolonii.\n")

    print(f"Apolonia oblicza Y(j) dla każdego j z przedziału [1, {M}]...")
    Yj = [((m + j - 1) ** d) % n for j in range(0, M)]
    print(f"Apolonia obliczyła Yj dla każego j z przedziału [1, {M}.\n")
    print(Yj)

    p = random.randint(3, M // int(M ** (1 / 2)))
    print(f"Apolonia wybiera losową wartość p = {p}.")
    print(f"Apolonia oblicza Z(j) dla każdego j z przedziału [1, {M}]...")
    Zj = [yj % p for yj in Yj]
    print(f"Apolonia obliczyła Z(j) dla każdego j z przedziału [1, {M}]...\n")
    print(Zj)

    print(f"Apolonia oblicza W(j), czyli dodaje 1 do każgego Z(j) z indeksem >= I ({I})...")
    Wj = []
    for i in range(0, len(Zj)):
        if i >= I:
            Wj.append(Zj[i] + 1)
        else:
            Wj.append(Zj[i])
    print(f"Apolonia obliczyła W(j), czyli dodała 1 do każgego Z(j) z indeksem >= I ({I}).")
    print(f"Apolonia przekazuje W(j), oraz p = {p} Bogusiowi.\n")

    print(f"Bogus sprawdza, czy W(J) ≡ x % p...")
    if Wj[J] == Mod(x, p):
        print(f"Tak, czyli I >= J ({I} >= {J}).\n")
        if I >= J:
            print("Sukces!")
            return True
        print("Błąd!")
        return False
    else:
        print(f"Nie, czyli I < J ({I} < {J}).\n")
        if I < J:
            print("Sukces!")
            return True
        print("Błąd!")
        return False


def milionaire_problem_no_print(M):
    I = random.randint(0, M - 1)

    J = random.randint(0, M - 1)

    public_key, private_key = generate_keys()
    e = public_key[0]
    n = public_key[1]
    d = private_key[0]

    x = random.randint(1, M)

    C = x ** e % n

    m = C - J + 1

    Yj = [((m + j - 1) ** d) % n for j in range(0, M)]

    p = random.randint(3, M // int(M ** (1 / 2)))
    Zj = [yj % p for yj in Yj]

    Wj = []
    for i in range(0, len(Zj)):
        if i >= I:
            Wj.append(Zj[i] + 1)
        else:
            Wj.append(Zj[i])
    if Wj[J] == Mod(x, p):
        if I >= J:
            return True
        return False
    else:
        if I < J:
            return True
        return False


print(sum([1 for i in range(100) if milionaire_problem_no_print(10000)]))
# M = 100   95%
# M = 1000  80%
# M = 10000 55%
