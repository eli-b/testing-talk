import pytest

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


def test_pi_digits_too_small():
    """Integers smaller than 1 as input should raise an error"""
    # Arrange
    digits = -5

    # Act + Assert
    with pytest.raises(ValueError):
        ret = example2.pi(digits)


def test_pi_digits_too_large():
    """Integers larger than 1000 as input should raise an error"""
    digits = 2_000_000
    with pytest.raises(ValueError):
        ret = example2.pi(digits)


def test_pi_digits_float():
    """Floats as input should raise an error"""
    digits = 3.5
    with pytest.raises(TypeError):
        ret = example2.pi(digits)


def test_pi_digits_round_float():
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    digits = 40.0
    with pytest.raises(TypeError):
        ret = example2.pi(float(int(digits)))


def test_pi_digits_str_input():
    """Strings that represent integers as input should raise an error"""
    digits = "30"
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


def test_pi_digits_bool_input():
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    boolean = True
    with pytest.raises(TypeError):
        ret = example2.pi(boolean)


def test_pi_digits_nominal():
    """Tests with an integer within the accepted range"""
    digits = 50
    ret = example2.pi(digits)
    assert ret == [pi_digits[i : min((i + 40, digits))] for i in range(0, digits, 40)]


# ---------------


def test_is_prime_too_small():
    """Integers smaller than 1 as input should raise an error"""
    digits = -4
    with pytest.raises(ValueError):
        ret = example2.is_prime(digits)


def test_is_prime_float():
    """Floats as input should raise an error"""
    f = 32.87
    with pytest.raises(TypeError):
        ret = example2.is_prime(f)


def test_is_prime_round_float():
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    f = 5.0
    with pytest.raises(TypeError):
        ret = example2.is_prime(float(int(f)))


def test_is_prime_str_input():
    """Strings that represent integers as input should raise an error"""
    n = 31
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


def test_is_prime_bool_input():
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    b = True
    with pytest.raises(TypeError):
        ret = example2.is_prime(b)


def test_is_prime_nominal():
    """Test with an integer within the accepted range"""
    n = 31
    ret = example2.is_prime(n)
    assert ret == (n in primes_set)


# ------


def test_prime_too_small():
    """Integers smaller than 1 as input should raise an error"""
    n = 0
    with pytest.raises(ValueError):
        ret = example2.prime(n)


def test_prime_too_large():
    """Integers larger than 1000 as input should raise an error"""
    n = 2345
    with pytest.raises(ValueError):
        ret = example2.prime(n)


def test_prime_float():
    """Floats as input should raise an error"""
    f = 25.33
    with pytest.raises(TypeError):
        ret = example2.prime(f)


def test_prime_round_float():
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    f = 31.0
    with pytest.raises(TypeError):
        ret = example2.prime(float(int(f)))


def test_prime_str_input():
    """Strings that represent integers as input should raise an error"""
    n = 31
    with pytest.raises(TypeError):
        ret = example2.prime(str(n))


def test_prime_input_none():
    """None as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.prime(None)


def test_prime_bool_input():
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    b = True
    with pytest.raises(TypeError):
        ret = example2.prime(b)


def test_prime_nominal():
    """Tests with an integer within the accepted range"""
    n = 31
    ret = example2.prime(n)
    assert ret == primes[n - 1]  # n=1 requests the first prime


# ------


def test_fib_too_small():
    """Integers smaller than 1 as input should raise an error"""
    n = 0
    with pytest.raises(ValueError):
        ret = example2.fibonacci(n)


def test_fib_too_large():
    """Integers larger than 1000 as input should raise an error"""
    n = 1001
    with pytest.raises(ValueError):
        ret = example2.fibonacci(n)


def test_fib_float():
    """Floats as input should raise an error"""
    f = 30.2
    with pytest.raises(TypeError):
        ret = example2.fibonacci(f)


def test_fib_float_round_float():
    """Round floats within the accepted range as input should still raise an error,
    according to my understanding of the spec"""
    f = 30.0
    with pytest.raises(TypeError):
        ret = example2.fibonacci(float(int(f)))


def test_fib_str_input():
    """Strings that represent integers as input should raise an error"""
    n = 20
    with pytest.raises(TypeError):
        ret = example2.fibonacci(str(n))


def test_fib_input_none():
    """None as input should raise an error"""
    with pytest.raises(TypeError):
        ret = example2.fibonacci(None)


def test_fib_bool_input():
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5
    """
    b = True
    with pytest.raises(TypeError):
        ret = example2.fibonacci(b)


def test_fib_nominal():
    """Tests with an integer within the accepted range"""
    n = 29
    ret = example2.fibonacci(n)
    assert ret == fibs[n - 1]  # n=1 requests the first prime
