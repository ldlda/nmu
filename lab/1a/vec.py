# quit this shit rn

import sympy
from sympy.abc import k, n, i
import sympy.algebras
import sympy.vector

# 5

f = 1 / k + 1 / (1 - k)

pinf = sympy.oo

f_s = sympy.summation(f, (i, 0, n))

print(f_s)


f_2 = 1 / (n**2)

f_inf = sympy.summation(f_2, (n, 1, pinf))

print(f_inf)
