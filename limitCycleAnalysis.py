# import numpy as np
# import math
from sympy import *


def bendixson(f, g):
    """Checks for limit cycle using the Bendixson–Dulac theorem for n=2. Takes the functions x' and y' as well as the
    variable mu """
    summe = f.diff(x) + g.diff(y)
    print("The sum of the partial derivatives is ", summe)
    if (StrictLessThan(summe, 0)).is_Boolean:
        if StrictLessThan(summe, 0):
            print("No possible limit cycle exists in R^2!")
        elif not StrictLessThan(summe, 0):
            print("A limit cycle could exist in R^2!")
    else:
        print("A limit cycle could exist for ", solve(summe > 0, mu))


def main():
    global x
    global y
    global mu
    x, y, mu = symbols('x y mu', real=True)
    f = -1 * x + 2 * y
    g = 4 * x + -(5 + mu ** 2) * y
    bendixson(f, g)


if __name__ == '__main__':
    main()
