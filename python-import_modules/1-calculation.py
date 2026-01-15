#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import calculation

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculation(a, b)))
    print("{} - {} = {}".format(a, b, calculation(a, b)))
    print("{} * {} = {}".format(a, b, calculation(a, b)))
    print("{} / {} = {}".format(a, b, calculation(a, b)))
