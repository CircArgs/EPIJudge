from test_framework import generic_test

from string import hexdigits

def to_decimal(s, b):
    neg=False
    if s[0]=='-':
        neg=True
        s=s[1:]
    tot=0
    for i, c in enumerate(reversed(s)):
        d = hexdigits.index(c)
        tot+=d*(b**i)
    return tot if not neg else -tot

def div_parts(dividend, divisor):
    quotient= dividend//divisor
    return quotient, dividend-quotient*divisor

def from_decimal(n, b):
    neg=False
    if n<0:
        neg=True
        n=-n
    qd, r = div_parts(n, b)
    ret=hexdigits[r]
    while qd>0:
        qd, r = div_parts(qd, b)
        ret+=hexdigits[r].upper()
    ret=ret[::-1]
    return ret if not neg else "-"+ret

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    temp = to_decimal(num_as_string, b1)
    return from_decimal(temp, b2)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
