"""A collection geometry-related functions."""


def square(n):
    """returns (n) squared"""
    return n**2


def triangle(n):
    """returns (n) triangulated"""
    result = 0
    for i in range(n):
        result += i + 1
    return result


def cube(n):
    """returns (n) cubed"""
    return n**3
