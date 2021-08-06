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

def generate_power_set(items):
    if len(items)==0:
        return [set()]
    rem=next(iter(items))
    temp=generate_power_set(items-{rem})
    return temp+[{*s, rem} for s in temp]

#loop arbitrary items
def generate_power_set(items):
    ret=[set()]
    for i in items:
        ret+=[{*s, i} for s in ret]
    return [list(s) for s in ret]

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
