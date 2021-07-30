from typing import List

from test_framework import generic_test


def plus_one(l):
    carry=1
    for i in reversed(range(len(l))):
        if not carry:
            break
        if l[i]==9:
            l[i]=0
        else:
            l[i]+=1
            carry=0
    if carry:
        l.insert(0, 1)
    return l


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
