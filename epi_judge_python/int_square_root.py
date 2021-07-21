from test_framework import generic_test


def square_root(k: int) -> int:
    i=k//2
    change=i
    while 0<=i<=k:

        s=i**2
        change=max(1, change//2)
        if s>k:
            i-=change
        elif s==k or (i+1)**2>k:
            return i
        else:
            i+=change
    return i
    


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )
