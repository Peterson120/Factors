from typing import List
from sys import setrecursionlimit

setrecursionlimit(999999999)


def listToInt(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def lcm(x):
    x = list(dict.fromkeys(x))
    total = 1
    for i in range(len(x)):
        total *= x[i]
    return total // gcd(x, 0)


def gcd(x, time):
    third = x[0]
    x[0] = x[1]
    x[1] = third % x[1]
    if len(x) > time + 1:
        if x[1] != 0:
            gcd(x, time)
        else:
            x.sort(reverse=True)
            time += 1
            if time + 1 < len(x):
                gcd(x, time)
    return x[0]


def factors(original, divisor, start):
    if len(original) != start:
        if original[start] % divisor == 0:
            print(divisor)
            if original[start] == divisor:
                return factors(original, 1, start + 1)
        return factors(original, divisor + 1, start)
    return


type_factor = ""
while type_factor != "stop":
    type_factor = input("GCF(G), LCM(L), or Factor(F): ").lower()
    user = input("Enter a list: ")
    list1 = listToInt(user.split())
    list1.sort(reverse=True)
    if type_factor == "gcf" or type_factor == "g":
        if len(list1) > 1:
            print("The GCF is: ", gcd(list1, 0))
        else:
            print("The GCF is: %d" % list1[0])
    elif type_factor == "lcm" or type_factor == "l":
        if len(list1) > 1:
            print("The LCM is: ", lcm(list1))
        else:
            print("The LCM is: ", list1[0])
    elif type_factor == "factor" or type_factor == "f":
        factors(list1, 1, 0)
    else:
        break
