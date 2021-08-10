from typing import List

from test_framework import generic_test


class Pos:
    def __init__(self, row, col, n):
        self.__dict__.update(locals())
        self.diagp=col-row
        self.diagn=row-(n-col)
            
    def __eq__(self, other):
        return self.row==other.row and self.col==other.col
    
    def __hash__(self):
        return hash(self.to_tuple())
    
    def __repr__(self):
        return f'Pos(row={self.row}, col={self.col}, diag=({self.diagp}, {self.diagn}))'
    
    def __str__(self):
        return repr(self)
    def to_tuple(self):
        return (self.row, self.col)

def n_queens(n):
    ret=[]
    def foo(row, c, dp, dn, sret):
        if row==n:
            ret.append(sret)
            return
        for col in range(n):
            p=Pos(row, col, n-1)
            if col not in c and p.diagp not in dp and p.diagn not in dn:
                foo(row+1, {*c, col}, {*dp, p.diagp}, {*dn, p.diagn}, [*sret, p])
    foo(0, {}, {}, {}, [])
    return [[i.col for i in j] for j in ret]


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("n_queens.py", "n_queens.tsv", n_queens, comp))
