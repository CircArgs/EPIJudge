import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def flagsort_helper(A, start, end, pivot):
    if (end-start)<1:
        return
    if (end-start)==1:
        A[start], A[end] = min(A[start], A[end]), max(A[start], A[end])
        return
    pv = A[pivot]
    ps, pe = pivot, pivot
    s, e = pivot-1, pivot+1
    
    while s>=start and e<=end:
        sv, ev = A[s], A[e]
        if sv<pv and ev<pv:#1
            A[ps], A[e], A[pe+1] = A[e], A[pe+1], A[ps]
            pe+=1
            ps+=1
        elif sv>pv and ev>pv:#2
            A[pe], A[s], A[ps-1] = A[s], A[ps-1], A[pe]
            ps-=1
            pe-=1
        elif sv>pv and ev<pv:#3
            A[e], A[s] = A[s], A[e]
        elif sv<pv and ev>pv:#4
            pass
        elif sv==pv and ev>pv:#5
            A[ps-1], A[s] = A[s], A[ps-1]
            ps-=1
        elif sv==pv and ev<pv:#6
            if pe+1<e:
                A[pe+1], A[s], A[e] = A[s], A[e], A[pe+1]
            else:
                A[pe+1], A[s] = A[s], A[pe+1]
            pe+=1
        elif sv<pv and ev==pv:#7
            A[pe+1], A[e] = A[e], A[pe+1]
            pe+=1
        elif sv>pv and ev==pv:#8
            if ps-1>s:
                A[ps-1], A[e], A[s] = A[e], A[s], A[ps-1]
            else:
                A[ps-1], A[e] = A[e], A[ps-1]
            ps-=1
        else: #9 sv==pv and ev==pv
            A[ps-1], A[s], A[pe+1], A[e] = A[s], A[ps-1], A[e], A[pe+1]
            ps-=1
            pe+=1
        s-=1
        e+=1
        
    while s>=start:
        sv = A[s]
        if sv<pv:
            pass
        elif sv==pv:
            A[ps-1], A[s] = A[s], A[ps-1]
            ps-=1
        else:
            A[pe], A[s], A[ps-1] = A[s], A[ps-1], A[pe]
            ps-=1
            pe-=1
        s-=1
    while e<=end:
        ev = A[e]
        if ev>pv:
            pass
        elif ev==pv:
            A[pe+1], A[e] = A[e], A[pe+1]
            pe+=1
        else:
            A[ps], A[e], A[pe+1] = A[e], A[pe+1], A[ps]
            ps+=1
            pe+=1
        e+=1
    # left_pivot = int(start+(ps-1-start)/2)
    # flagsort_helper(A, start, ps-1, left_pivot)
    # right_pivot = int(end-(end-pe-1)/2)
    # flagsort_helper(A, pe+1, end, right_pivot)

    
def flagsort(A):
    flagsort_helper(A, 0, len(A)-1, len(A)//2)

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    flagsort_helper(A, 0, len(A)-1, pivot_index)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
