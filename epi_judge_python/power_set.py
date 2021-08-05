from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(l: List[int]) -> List[List[int]]:
    ret = []
    for i in range(1<<len(l)):
        temp=[]
        for j in range(i.bit_length()):
            if (1<<j)&i:
                temp.append(l[j])
        ret.append(temp)
    return ret


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
