import pytest
from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import integers, floats, booleans

from primes import primes
from fibs import fibs

import example2

pi_digits = (
    "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982"
    "14808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881"
    "09756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066"
    "06315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759"
    "59195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664"
    "3086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827"
    "7857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640"
    "3441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230"
    "8253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863"
    "8823537875937519577818577805321712268066130019278766111959092164201989"
)  # Obtained from the Internet
primes_set = set(primes)


def test_imports_without_an_error():
    """Tests that the module is imported without raise an exception"""
    pass


@given(digits=integers(max_value=0))
def test_pi_digits_too_small(digits):
    """Integers smaller than 1 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.pi(digits)


@given(digits=integers(min_value=1001))
def test_pi_digits_too_large(digits):
    """Integers larger than 1000 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.pi(digits)


@given(digits=floats())
def test_pi_digits_float(digits):
    """Floats as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.pi(digits)


@given(digits=floats(min_value=3, max_value=990))
def test_pi_digits_round_float(digits):
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    with pytest.raises(TypeError):
        ret = example2.pi(float(int(digits)))


@given(digits=integers())
def test_pi_digits_str_input(digits):
    """Strings that represent integers as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.pi(
            str(digits)
            # Calling int() on this input would result in an integer,
            # which should either work or give a different exception if given directly
        )


def test_pi_digits_none():
    """None as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.pi(None)


@given(boolean=booleans())
def test_pi_digits_bool_input(boolean):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    with pytest.raises(TypeError):
        ret = example2.pi(boolean)


@pytest.mark.timeout(60)  # We're calling pi 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(digits=integers(min_value=3, max_value=990))
def test_pi_digits_nominal(digits):
    """Tests integers within the accepted range"""
    ret = example2.pi(digits)
    assert ret == [pi_digits[i : min((i + 40, digits))] for i in range(0, digits, 40)]


# ---------------


@given(digits=integers(max_value=0))
def test_is_prime_too_small(digits):
    """Integers smaller than 1 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.is_prime(digits)


@given(f=floats())
def test_is_prime_float(f):
    """Floats as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.is_prime(f)


@given(f=floats(min_value=3, max_value=990))
def test_is_prime_round_float(f):
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    with pytest.raises(TypeError):
        ret = example2.is_prime(float(int(f)))


@given(n=integers())
def test_is_prime_str_input(n):
    """Strings that represent integers as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.is_prime(
            str(n)
            # Calling int() on this input would result in an integer,
            # which would either work or give a different exception
        )


def test_is_prime_input_none():
    """None as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.is_prime(None)


@given(b=booleans())
def test_is_prime_bool_input(b):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    with pytest.raises(TypeError):
        ret = example2.is_prime(b)


@pytest.mark.timeout(60)  # We're calling is_prime 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(n=integers(min_value=2, max_value=1000000))
def test_is_prime_nominal(n):
    """Tests integers within the accepted range"""
    ret = example2.is_prime(n)
    assert ret == (n in primes_set)


# ------


@given(n=integers(max_value=0))
def test_prime_too_small(n):
    """Integers smaller than 1 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.prime(n)


@given(n=integers(min_value=1001))
def test_prime_too_large(n):
    """Integers larger than 1000 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.prime(n)


@given(f=floats())
def test_prime_float(f):
    """Floats as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.prime(f)


@given(f=floats(min_value=3, max_value=990))
def test_prime_round_float(f):
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    with pytest.raises(TypeError):
        ret = example2.prime(float(int(f)))


@given(n=integers())
def test_prime_str_input(n):
    """Strings that represent integers as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.prime(str(n))


def test_prime_input_none():
    """None as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.prime(None)


@given(b=booleans())
def test_prime_bool_input(b):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    with pytest.raises(TypeError):
        ret = example2.prime(b)


@pytest.mark.timeout(60)  # We're calling prime 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(n=integers(min_value=1, max_value=1000))
def test_prime_nominal(n):
    """Tests integers within the accepted range"""
    ret = example2.prime(n)
    assert ret == primes[n - 1]  # n=1 requests the first prime


# ------


@given(n=integers(max_value=0))
def test_fib_too_small(n):
    """Integers smaller than 1 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.fibonacci(n)


@given(n=integers(min_value=1001))
def test_fib_too_large(n):
    """Integers larger than 1000 as input should raise an error"""
    with pytest.raises(ValueError):
        ret = example2.fibonacci(n)


@given(f=floats())
def test_fib_float(f):
    """Floats as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.fibonacci(f)


@given(f=floats(min_value=3, max_value=990))
def test_fib_float_round_float(f):
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    with pytest.raises(TypeError):
        ret = example2.fibonacci(float(int(f)))


@given(n=integers())
def test_fib_str_input(n):
    """Strings that represent integers as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.fibonacci(str(n))


def test_fib_input_none():
    """None as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.fibonacci(None)


@given(b=booleans())
def test_fib_bool_input(b):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    with pytest.raises(TypeError):
        ret = example2.fibonacci(b)


@pytest.mark.timeout(60)  # We're calling fibonacci 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(n=integers(min_value=1, max_value=1000))
def test_fib_nominal(n):
    """Tests integers within the accepted range"""
    ret = example2.fibonacci(n)
    assert ret == fibs[n - 1]  # n=1 requests the first prime
