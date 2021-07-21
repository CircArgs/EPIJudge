from typing import List

from test_framework import generic_test

def duplicate_pairs(l):
    dist=float('inf')
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            a, b = l[i], l[j]
            if a==b and (j-i)<dist:
                dist=j-i
    return dist if dist<float('inf') else -1

def find_nearest_repetition(l: List[str]) -> int:
    d, dist= {}, float('inf')
    for i, w in enumerate(l):
        if w in d:
            temp=i-d[w]
            if temp<dist:
                dist=temp
        d[w]=i
    return dist if dist<float('inf') else -1

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nearest_repeated_entries.py",
            "nearest_repeated_entries.tsv",
            find_nearest_repetition,
        )
    )
