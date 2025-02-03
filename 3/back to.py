# im actually done with jupyter notebook i dont like jupyter notebooks.

"""
ass
"""

import numpy
import scipy
import sympy
import numpy.linalg
import scipy.linalg
import numpy.polynomial
import scipy.optimize


scipy.linalg.eig
scipy.linalg.companion

ce = tuple(reversed((1, 0, -7, 6)))
p = numpy.polynomial.Polynomial(ce).roots()

x_sym = sympy.Symbol("x")

f = x_sym**3 -7 * x_sym + 6
c = sympy.solve(f, x_sym)

print(p)
print(c)

def system(x_y):  # trait Index<usize> for ndarray
    x, y = x_y
    u = x**2 + x * y - 10
    v = y + 3 * x * y**2 - 57
    return u, v


r = scipy.optimize.fsolve(system, (0, 0)) 
# look this is way better than matlab where you have a separate options function? stinky?

# pass this big boi a **options and you are set for life
print(r)