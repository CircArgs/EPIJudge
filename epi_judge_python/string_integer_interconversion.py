from test_framework import generic_test
from test_framework.test_failure import TestFailure
from string import digits

def int_to_string(x: int) -> str:
    if not x:
        return '0'
    pos=x>0
    x=abs(x)
    ret = []
    while x>0:
        ret.append(str(x%10))
        x//=10
    return '+'*pos+'-'*(1-pos)+''.join(reversed(ret))

def string_to_int(s: str) -> int:
    s=s.strip()
    ret = 0
    for i, c in enumerate(reversed(s[1:])):
        ret+=digits.index(c)*10**i
    return -ret if s[0]=='-' else ret+digits.index(s[0])*10**(len(s)-1) if s[0]!='+' else ret

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
