from typing import List

from test_framework import generic_test
def foo(l):
    m=0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            temp = (j-i)*min(l[i],l[j])
            if temp>m:
                m=temp
    return m
    
def foo(l):
    i,j=0, len(l)-1
    a, b=l[i], l[j]
    m=min(a, b)*(j-i)
    while i<j:
        
        if a<=b:
            i+=1
        else:
            j-=1
        a, b=l[i], l[j]
        temp=min(a, b)*(j-i)
        if temp>m:
            m=temp
    return m
        
        
def get_max_trapped_water(heights: List[int]) -> int:
    return foo(heights)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_trapped_water.py", "max_trapped_water.tsv", get_max_trapped_water
        )
    )
