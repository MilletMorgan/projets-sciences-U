#
# result3 = 0
# s = 0
#
# for n in range(10):
#     result = 2 ** (n - 1)
#     result2 = 2 ** n - 1
#     if result == result2:
#         result3 = (2 ** (n - 1)) * (2 ** n - 1)
#         print(result3)
#
#         for i in range(1, result3):
#             if result3 % i == 0:
#                 s = s + i
#
#         if s == result3:
#             print(result3, " est parfait.")
#         else:
#             print(result3, "n'est pas parfait.")
#


def sommediviseur(n):
    s = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            s = s + i
    return s


# Test si le nombre est premier
def premier(n):
    res = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True


borne = int(input("Borne : "))

for n in range(1, borne + 1):
    if premier(2 ** n - 1):
        nombre = (2 ** (n - 1)) * (2 ** n - 1)
        if nombre == sommediviseur(nombre):
            print("n = ", n, " 2^n-1 = ", 2 ** n - 1)
            print(nombre, " est un nombre parfait")
        else:
            print("n = ", n, "2^", n, "-1 = ", 2 ** n - 1, " n'est pas premier")
            print()
