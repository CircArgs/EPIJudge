from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    x, y = sorted((x, y))
    if not x:
        return y
    temp=y%x
    if temp==0:
        return x
    return gcd(x, temp)

def gcd(x: int, y: int) -> int:
    x, y = sorted((x, y))
    while x:
        x, y = y%x, x

    return y


if __name__ == "__main__":
    exit(generic_test.generic_test_main("gcd.py", "gcd.tsv", gcd))
