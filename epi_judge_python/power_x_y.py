from test_framework import generic_test


from functools import lru_cache

@lru_cache(100)
def power(x, y):

    if y==0:
        return 1
    elif y==1:
        return x
    elif y==-1:
        return 1/x

    return power(x, y-y//2)*power(x, y//2)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power))
