import doctest


def plus1(n):
    """In a doc

    >>> plus1(1)
    2

    >>> plus1(n)
    Traceback (most recent call last):
      ...
    NameError: name 'n' is not defined
    """
    return n + 1


if __name__ == "__main__":
    doctest.testmod()
