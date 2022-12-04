#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, product, quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    
    aa = add(a, b)
    bb = sub(a, b)
    cc = mul(a, b)
    dd = div(a, b)

    print("{} + {} = {}".format(a, b, aa))
    print("{} - {} = {}".format(a, b, bb))
    print("{} * {} = {}".format(a, b, cc))
    print("{} / {} = {}".format(a, b, dd))
