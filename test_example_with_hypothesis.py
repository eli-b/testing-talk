"""Must be run with -n1 (or more), --timeout=1, and --hypothesis-profile=suppress (which I define in the conftest).
Using xdist is required! This way a single test fails on timeout with the thread timeout method instead crashing the whole pytest run.
The downside is that the report says that the worker crashed without giving a usable traceback.
"""

import pytest
from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import integers, floats, booleans

from primes import primes  # Obtained from the Internet
from fibs import fibs  # Obtained from my implementation, sadly I couldn't find a long enough external source.

import example

pi_digits = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982' \
            '14808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881' \
            '09756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066' \
            '06315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759' \
            '59195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664' \
            '3086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827' \
            '7857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640' \
            '3441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230' \
            '8253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863' \
            '8823537875937519577818577805321712268066130019278766111959092164201989'  # Obtained from the Internet
primes_set = set(primes)


def test_imports_without_an_error():
    """Tests that the module is imported without raise an exception"""
    pass


@given(digits=integers(max_value=0))
def test_pi_digits_too_small(digits, capsys):
    """Integers smaller than 1 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(digits)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(digits=integers(min_value=1001))
def test_pi_digits_too_large(digits, capsys):
    """Integers larger than 1000 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(digits)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(digits=floats())
def test_pi_digits_float(digits, capsys):
    """Floats as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(digits)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(digits=floats(min_value=3, max_value=990))
def test_pi_digits_round_float(digits, capsys):
    """Round floats within the accepted range as input should still print an error,
    according to my understanding of the spec"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(float(int(digits)))
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(digits=integers())
def test_pi_digits_str_input(digits, capsys):
    """Strings that represent integers as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(str(digits))  # Calling int() on this input would result in an integer,
                                   # which should either work or give a different exception if given directly
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


def test_pi_digits_none(capsys):
    """None as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(None)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(boolean=booleans())
def test_pi_digits_bool_input(boolean, capsys):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(boolean)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@pytest.mark.timeout(60)  # We're calling pi 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(digits=integers(min_value=3, max_value=990))
def test_pi_digits_nominal(digits, capsys):
    """Tests integers within the accepted range"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.pi(digits)
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    assert lines == [pi_digits[i: min((i + 40, digits))] for i in range(0, digits, 40)]
    assert ret is None


# ---------------

@given(digits=integers(max_value=0))
def test_is_prime_too_small(digits, capsys):
    """Integers smaller than 1 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(digits)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(f=floats())
def test_is_prime_float(f, capsys):
    """Floats as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(f)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(f=floats(min_value=3, max_value=990))
def test_is_prime_round_float(f, capsys):
    """Round floats within the accepted range as input should still print an error,
    according to my understanding of the spec"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(float(int(f)))
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(n=integers())
def test_is_prime_str_input(n, capsys):
    """Strings that represent integers as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(str(n))  # Calling int() on this input would result in an integer,
                                    # which would either work or give a different exception
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


def test_is_prime_input_none(capsys):
    """None as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(None)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(b=booleans())
def test_is_prime_bool_input(b, capsys):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(b)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@pytest.mark.timeout(60)  # We're calling is_prime 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(n=integers(min_value=2, max_value=1000000))
def test_is_prime_nominal(n, capsys):
    """Tests integers within the accepted range"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.is_prime(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == ''
    assert ret == (n in primes_set)


# ------


@given(n=integers(max_value=0))
def test_prime_too_small(n, capsys):
    """Integers smaller than 1 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(n=integers(min_value=1001))
def test_prime_too_large(n, capsys):
    """Integers larger than 1000 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(f=floats())
def test_prime_float(f, capsys):
    """Floats as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(f)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(f=floats(min_value=3, max_value=990))
def test_prime_round_float(f, capsys):
    """Round floats within the accepted range as input should still print an error,
    according to my understanding of the spec"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(float(int(f)))
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(n=integers())
def test_prime_str_input(n, capsys):
    """Strings that represent integers as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(str(n))
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


def test_prime_input_none(capsys):
    """None as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(None)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(b=booleans())
def test_prime_bool_input(b, capsys):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(b)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@pytest.mark.timeout(60)  # We're calling prime 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(n=integers(min_value=1, max_value=1000))
def test_prime_nominal(n, capsys):
    """Tests integers within the accepted range"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.prime(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == ''
    assert ret == primes[n - 1]  # n=1 requests the first prime

# ------


@given(n=integers(max_value=0))
def test_fib_too_small(n, capsys):
    """Integers smaller than 1 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(n=integers(min_value=1001))
def test_fib_too_large(n, capsys):
    """Integers larger than 1000 as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Input out of range'
    assert ret is None


@given(f=floats())
def test_fib_float(f, capsys):
    """Floats as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(f)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(f=floats(min_value=3, max_value=990))
def test_fib_float_round_float(f, capsys):
    """Round floats within the accepted range as input should still print an error,
    according to my understanding of the spec"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(float(int(f)))
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(n=integers())
def test_fib_str_input(n, capsys):
    """Strings that represent integers as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(str(n))
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


def test_fib_input_none(capsys):
    """None as input should print an error"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(None)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@given(b=booleans())
def test_fib_bool_input(b, capsys):
    """True and False are explicitly required to be a wrong input type,
    even though in Python True and False have a numeric value: sum([True for i in range(5)]) == 5"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(b)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Wrong input type'
    assert ret is None


@pytest.mark.timeout(60)  # We're calling fibonacci 50 times
@settings(max_examples=50)  # Each example's deadline is 1s (see above)
@given(n=integers(min_value=1, max_value=1000))
def test_fib_nominal(n, capsys):
    """Tests integers within the accepted range"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    ret = example.fibonacci(n)
    captured = capsys.readouterr()
    assert captured.out.strip() == ''
    assert ret == fibs[n - 1]  # n=1 requests the first prime

# ------


def test_from_example(capsys):
    """Tests with the example from the exercise, adapted to not test is_prime with numbers over a million"""
    _ = capsys.readouterr()  # To get around capsys not being reset between examples
    example.pi(3.5)
    example.pi(1001)
    example.pi(56)
    example.pi(3)
    print('***********************************************')
    print(example.is_prime('Yoyoyo'))
    print(example.is_prime(2.3))
    print(example.is_prime(0))
    print(example.is_prime(1000000))
    print(example.is_prime(2))
    print('***********************************************')
    print(example.prime(True))
    print(example.prime(-1))
    print(example.prime(1))
    print(example.prime(6))
    print('***********************************************')
    print(example.fibonacci('-1'))
    print(example.fibonacci(0))
    print(example.fibonacci(1))
    print(example.fibonacci(13))
    captured = capsys.readouterr()
    assert captured.out.strip() == \
        '''Wrong input type
Input out of range
3.14159265358979323846264338327950288419
7169399375105820
3.1
***********************************************
Wrong input type
None
Wrong input type
None
Input out of range
None
False
True
***********************************************
Wrong input type
None
Input out of range
None
2
13
***********************************************
Wrong input type
None
Input out of range
None
1
233'''
