import math
import random


def Euclid(a, b):
    x = a
    y = b
    if a < b:
        x = b
        y = a

    while 1:
        if x % y == 0:
            return y
        else:
            x, y = y, x % y


a = random.randint(1, 100)
b = random.randint(1, 100)
GCD = Euclid(a, b)
print(a, b)
print(GCD)
print(math.gcd(a, b) == GCD)
