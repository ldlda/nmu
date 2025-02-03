"bisection tailored to fit lab 1b"

from typing import Callable
from numbers import Real
from math import isclose, fabs


# this is the already existing bis, see git blame
def bis(
    f: Callable[[Real], Real],
    low: Real,
    high: Real,
    *,
    rel_tol: Real = 1e-9,
    abs_tol: Real = 0.0,
    max_loop: int = 100,
) -> tuple[Real, int]:
    """real

    rel_tol and abs_tol passes to `math.isclose`
    """

    def ldaprx(a, b):
        return isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

    steps = 0
    fl = f(low)
    fh = f(high)
    #     raise ValueError(f"at {low =} f(x) is {fl}, at {high =} f(x) is {fh} which has the same sign")

    if ldaprx(0, fl):
        return (low, 0)
    if ldaprx(0, fh):
        return (high, 0)

    mid = (low + high) / 2

    while (steps := steps + 1) and (max_loop := max_loop - 1) + 1 > 0:
        match f(mid):
            case x if ldaprx(0, x):
                return (mid, steps)
            case x if x < 0:
                low = mid
            case x if x > 0:
                high = mid
        mid = (low + high) / 2
    return (mid, steps)


def bis1b(
    f: Callable[..., Real],
    bounds: tuple[Real, Real],
    rel_tol: Real = 1e-6,
    maxit: int = 50,
    fa: tuple = None,
    fkw: dict = None,
) -> tuple[Real, Real, Real, int]:
    """bisect: root location zeroes

    uses bisection method to find the root of func

    input:
        func: name of function
        bounds: lower and upper guesses
        rel_tol: desired relative error (default = 0.0001%)
        maxit: maximum allowable iterations (default = 50)
        fa, fkw: additional parameters used by func
    output:
        root: real root
        fx: function value at root
        ea: approximate relative error. not in percent because that is bullshit
        iter: number of iterations

    function should take one real variable x (Real) + farg and fkwarg like so:
        `f(x, *fa, **fkw)`
    """
    if fa is None:
        fa = ()
    if fkw is None:
        fkw = {}

    def fi(x):
        return f(x, *fa, **fkw)

    if len(bounds) != 2:
        raise ValueError("bounds should have two values?")
    xl, xu = bounds
    # shit naming competition

    if fi(xl) * fi(xu) > 0:  # maybe incorrect
        raise ValueError("no sign change")

    it = 0
    xr = xl
    ea = 1

    while True:
        xr_old = xr
        xr = (xl + xu) / 2
        it += 1

        if xr != 0:
            ea = fabs((xr - xr_old) / xr)  # approx

        cur_iter = fi(xl) * fi(xu)
        match cur_iter:
            case x if x > 0:
                xu = xr
            case x if x < 0:
                xl = xr
            case 0:
                ea = 0

        if ea <= rel_tol or it >= maxit:
            break
    root = xr
    fx = fi(xr)

    return (root, fx, ea, it)
