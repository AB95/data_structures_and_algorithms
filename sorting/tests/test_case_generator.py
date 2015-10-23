import random


def integer_array_generator(length):
    return [random.randint(-100, 100) for i in xrange(length)]


def float_array_generator(length):
    return [random.random()*100 for i in xrange(length)]


def number_array_generator(length):
    return integer_array_generator(length/2) + float_array_generator(length/2)


def char_array_generator(length):
    return [chr(random.randint(97, 122)) for i in xrange(length)]


def string_array_generator(length):
    return [''.join(char_array_generator(5)) for i in xrange(length)]
