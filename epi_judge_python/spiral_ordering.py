from typing import List

from test_framework import generic_test

def matrix_in_spiral_order(l):
    if not l:
        return l
    r = len(l)
    c=len(l[0])
    rmax=r
    rmin=0
    cmin=0
    cmax=c
    dr=False
    dc=False
    turn=True
    i=0
    j=0
    ret=[]
    while len(ret)<(c*r):
        if turn:
            turn=not turn
#             print("C", list(reversed(range(cmin, cmax)) if dc else range(cmin, cmax)))
            for j in (reversed(range(cmin, cmax)) if dc else range(cmin, cmax)):
                ret.append(l[i][j])
            
            if not dc:
                rmin+=1
            else:
                rmax-=1
            dc=not dc
        else:
            turn= not turn
#             print("R", list(reversed(range(rmin, rmax)) if dr else range(rmin, rmax)))
            for i in (reversed(range(rmin, rmax)) if dr else range(rmin, rmax)):
               
                ret.append(l[i][j])
            
            if dr:
                cmin+=1
            else:
                cmax-=1
            dr= not dr
    return ret



if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
