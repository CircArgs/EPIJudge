from typing import Set

from test_framework import generic_test

def string_diff(a, b):
    diffs=0
    for i in range(max(len(a), len(b))):
        try:
            diffs+=a[i]!=b[i]
        except IndexError:
            diffs+=1
        if diffs>1:
            return False
    return diffs==1

def filter(f, it, base='_'):
    yielded=False
    for i in it:
        if f(i):
            yielded=True
            yield i
    if not yielded:
        yield base

def transmute(a, b, d, checked=set()):
    if a=='_':
        return float('inf')
    if a==b:
        return 0
    return 1+min(transmute(w, b, d, {*checked, w}) for w in filter(lambda w: w not in checked and string_diff(a, w), d))
            

from string import ascii_letters

ascii_letters=set(ascii_letters.lower())

def generate_changes(s, d):
    for l in ascii_letters:
        for i in range(len(s)):
            temp=s[:i]+l+s[i+1:]
            if temp in d:
                yield temp

def transmute(a, b, d):
    if not (a in d and b in d):
        return -1
    count=0
    level={a}
    while level:
        count+=1
        next_level=set()
        for e in level:
            for w in generate_changes(e, d):
               
                if w==b:
                    return count
                next_level.add(w)
        level=next_level
        d.difference_update(next_level)
    return -1
    
def transform_string(D: Set[str], s: str, t: str) -> int:
    return transmute(s, t, D)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_transformability.py",
            "string_transformability.tsv",
            transform_string,
        )
    )
