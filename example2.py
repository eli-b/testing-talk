import itertools
import functools
import math
import numbers


def pi(digits):
    """Return `digits digits of pi`, in clumps of 40"""
    if (
        not isinstance(digits, numbers.Integral)
        or type(digits) == bool  # bool is required to be interpreted as a bad type
    ):
        raise TypeError()
    if digits < 1 or digits > 1000:
        raise ValueError()
    pi_digits = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
    ret = []
    for i in range(0, digits, 40):
        ret.append(pi_digits[i : min((i + 40, digits))])
    return ret


def is_prime(n):
    if (
        not isinstance(n, numbers.Integral)
        or type(n) == bool  # bool is required to be interpreted as a bad type
    ):
        raise TypeError()
    if n < 1:
        raise ValueError()
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Include the root of n
        if n % i == 0:
            return False
    return True


def prime(n):
    """Return the n'th prime"""
    if (
        not isinstance(n, numbers.Integral)
        or type(n) == bool  # bool is required to be interpreted as a bad type
    ):
        raise TypeError()
    if n < 1 or n > 1000:
        raise ValueError()
    potentials = itertools.count(2)
    primes = filter(is_prime, potentials)
    first_n_primes = itertools.islice(primes, n - 1 + 1)
    # -1 because n=1 requests the first prime, + 1 because the end of a slice is exclusive
    return list(first_n_primes)[-1]


def fibonacci(n):
    # import time  # For testing the timeout requirement of the tests
    # time.sleep(3)
    if (
        not isinstance(n, numbers.Integral)
        or type(n) == bool  # bool is required to be interpreted as a bad type
    ):
        raise TypeError()
    if n < 1 or n > 1000:
        raise ValueError()
    # Cache required values:
    for i in range(1, n):
        fibonacci_inner(i)
    # Compute the result:
    return fibonacci_inner(n)


@functools.lru_cache(maxsize=None, typed=True)
def fibonacci_inner(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci_inner(n - 1) + fibonacci_inner(n - 2)
