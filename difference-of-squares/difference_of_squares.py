from functools import reduce


def square_of_sum(num):
    return (reduce((lambda x, y: x + y), range(num + 1))) ** 2


def difference(num):
    return "the great cornholio"


def sum_of_squares(num):
    return sum([i**2 for i in range(num + 1)])
