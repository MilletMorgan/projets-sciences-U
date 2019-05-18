def deciConvers(decimal):
    if decimal > 1:
        deciConvers(decimal//2)

    return decimal % 2


def binConvers():
    binary_list = []
    decimal = []
    binary = int(input("Enter your binary number : "))

    for i in str(binary):
        binary_list.append(int(i))

    binary_list.reverse()

    for i in range(len(binary_list)):
        if binary_list[i] == 1:
            decimal.append(2 ** i)

    return decimal


def operation_binary(binary_list):
    calcul = str(input("Calcul ? [addition/soustraction/multiplication] : "))

    if calcul == "addition":
        binary2 = binConvers()
        result = sum(binary_list) + sum(binary2)
        return print(sum(binary_list), " + ", sum(binary2), " = ", result)
    elif calcul == "multiplication":
        binary2 = binConvers()
        result = sum(binary_list) * sum(binary2)
        return print(sum(binary_list), " * ", sum(binary2), " = ", result)
    elif calcul == "soustraction":
        binary2 = binConvers()
        result = sum(binary_list) - sum(binary2)
        return print(sum(binary_list), " - ", sum(binary2), " = ", result)
    else:
        sum(binary_list)


def convert():
    signed = 0
    binary_list = binConvers()

    if (len(binary_list)) == 8 and binary_list[-1] == 1:
        signed = int(input("Signed binary ? [1/0] "))

        if signed == 1:
            signed_binary(binary_list)

    affichage(sum(binary_list), binary_list, signed)


def signed_binary(binary_list):
    binary_list[-1] = binary_list[-1] * -1

    # for i in range(len(binary_list)):
    #     if binary_list[i] == 1:
    #         binary_list[i] = 0
    #     else:
    #         binary_list[i] = 1

    return binary_list


def affichage(decimal, binary_list, signed):
    if signed == 1:
        print("-", decimal)
    else:
        print(decimal)

    operation = str(input("Operation ? [oui/non] "))
    if operation == "oui":
        operation_binary(binary_list)
    else:
        print(sum(binary_list))


def main():
    convert()


main()
