from typing import List
import sys

sys.setrecursionlimit(999999999)


def listToInt(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value


def lcm(x):
    listToInt(x)
    total = 1
    for i in range(len(x)):
        total *= x[i]
    return total / gcd(x, x[0] % x[1], 1)


def gcd(x, y, start):
    third = x[start]
    x[start] = y
    y = third % y
    if y != 0:
        return gcd(x, y, start)
    return gcd(x, x[start], start + 1)


def factors(original, divisor, start):
    listToInt(original)
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
    if type_factor == "gcf" or type_factor == "g":
        user = input("Enter a list: ")
        list1 = listToInt(user.split())
        if len(list1) > 1:
            listToInt(list1)
            if list1[0] >= list1[1]:
                print("The GCF is: " + gcd(list1, list1[0] % list1[1], 0))
            else:
                print("The GCF is: " + gcd(list1, list1[1] % list1[0], 0))
        else:
            print("The GCF is: %d" % list1[0])
    elif type_factor == "lcm" or type_factor == "l":
        user = input("Enter a list: ")
        print("The LCM is: %d " % lcm(user.split()))
    elif type_factor == "factor" or type_factor == "f":
        user = input("Enter a number: ")
        factors(user.split(), 1, 0)
    else:
        break
