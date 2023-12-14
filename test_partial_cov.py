def foo(num):
    num += 5

    if num == 300:
        raise Exception()

    return num - 10


def test_foo():
    assert foo(55) == 50
