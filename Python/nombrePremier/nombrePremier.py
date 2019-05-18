def premier(n):  

    if n <= 1 :
        return False
    for i in range(2, n) :
        if (n % i == 0) :
            return False
    return True

tab = [1, 2, 3, 4, 5]
print(premier(tab))