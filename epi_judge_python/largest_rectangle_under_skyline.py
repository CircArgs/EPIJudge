from typing import List

from test_framework import generic_test

from functools import lru_cache

# @lru_cache(1000)
def make_r(l):
    r=[]
    m=0
    for i in range(len(l)-1):
        temp=min(l[i], l[i+1])
        if temp>m:
            m=temp
        r.append(temp)
    return r, m

def foo(l):
    if not l:
        return 0
    r0=l
    c=2
    m=max(l)
    search=True
    while (len(r0)>1) and search:
        r, temp_m = make_r(r0)
        if temp_m*c>m:
            m=temp_m*c
        c+=1
        r0=r
    return m

class item:
    def __init__(self, index, data):
        self.index = index
        self.data = data
        
    def __eq__(self, other):
        return self.data==other.data
    
    def __hash__(self):
        return self.data
    
    def __repr__(self):
        return str((self.index, self.data))
    
    def __str__(self):
        return repr(self)

#move right across the list of heights
#for each building we will check our list of previously seen buildings
# if our preexisting list holds buildings taller than the current building then the current building is blocking the old building
# so the largest rectangle the old building can make with its height is up to the current building to we calculate its height and test against and update the max

#when we add a new building, since the buildings iterated through on the previously seen were higher, they support the new building so our new building index can be updated to include the earliest taller building

def foo(l):
    stack = []
    m=0
    for i in range(len(l)):
        e = item(i, l[i])
#         print(e)
#         if ascii_uppercase[e.index]=='L':
#             import pdb; pdb.set_trace()
        if not stack:
#             temp=e.data*e.index
#             m=max(temp, m)
            stack.append(e)
        else:
#             print('e', e)
            deld=False
            j=len(stack)-1
            while (j>=0) and stack:
#                 import pdb; pdb.set_trace()
                es=stack[j]
#                 print(es)
                if es.data==e.data:
                    temp = es.data*(i-es.index)
                    m=max(temp, m)
#                     stack[j]=e
                    break
                elif es.data<e.data:
#                     print('yo')
                    stack.append(e)
                    break
                else:
                    e.index = es.index
                    temp = es.data*(i-es.index)
                    m=max(temp, m)
                    del stack[j]
                    deld=True
                    
#                 print(temp)
                j-=1
            if deld:
                stack.append(e)

#         print([e for e in stack])
    for es in stack:
        temp = es.data*(len(l)-es.index)
#         print(temp)
        m=max(m, temp)
    return m

def calculate_largest_rectangle(heights: List[int]) -> int:
    return foo(heights)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "largest_rectangle_under_skyline.py",
            "largest_rectangle_under_skyline.tsv",
            calculate_largest_rectangle,
        )
    )
