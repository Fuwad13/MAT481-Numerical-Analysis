# Bisection Method to find a root of f(x) in interval [a, b]
# sign of f(a) and f(b) must be different, that is, f(a)*f(b) must be negative
# that implies there is at least one c suct that f(c) = 0, which is a root

EPSILON = 1e-9
MAX_ITER = 100

def f(x : float) -> float :
    # define f(x) here
    return x**3 + 4*(x**2) - 10


def find_root(f , a : float, b : float) -> float :
    #  check if [a, b] is a valid interval for this method
    if f(a)*f(b) >= 0 :
        raise ValueError("f(a) and f(b) must have opposite signs")
    FA = f(a)
    c = (a+b)/2
    for i in range(MAX_ITER) :
        c = (a+b)/2
        FC = f(c)
        if FC == 0 or (b-a)/2 < EPSILON :
            return c
        if FA*FC < 0 :
            b = c
        else :
            a = c
            FA = FC
    return c

print(find_root(f, 1, 2))
